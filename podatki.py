import re
import requests
import csv
import os
import orodja

direktorij_destinacij = "/Users/tiakrofel/Documents/faks/year 3/programiranje 1/Projektna-naloga/datoteke"
naenkrat = 18
koncaj = 556
priljubljenost = ["likes", "priljubljenost_destinacij"]
obiskanost = ["visits", "obiskanost_destinacij"]
prvi_del_povezave = "https://www.atlasobscura.com"

vzorec_bloka = re.compile(
    r'<a class="content-card content-card-place"'
    r'(.*?)</been-there-everywhere>',
    flags=re.DOTALL
)

vzorec_destinacije = re.compile(
    r'href="(?P<url>.*?)">.*?'
    r'place-card-location">(?P<lokacija>.*?)</div>.*?'
    r'js-title-content">(?P<destinacija>.*?)</span>.*?'
    r'js-subtitle-content">(?P<opis>.*?)</div>.*?'
    r'data-place-id=(?P<id>\d+?)\s',
    flags=re.DOTALL
)


vzorec_lokacije = re.compile(
    r'aria-hidden="true">.*?(?P<sirina>-?\d+\.\d+),.*?'
    r'\s(?P<dolzina>-?\d+\.\d+).*?'
    r'data-place-city="(?P<mesto>.*?)".*?'
    r'data-place-country="(?P<drzava>.*?)".*?',
    flags=re.DOTALL
)

vzorec_podrobneje = re.compile(
    r'"DDPage__header-dek".*?'
    r'title-md item-action-count">(?P<obiskali>\d+?)</div>.*?'
    r'title-md item-action-count">(?P<zelja>\d+?)</div>',
    flags=re.DOTALL
)

def popravki(slovar):
    for k in slovar.keys():
        slovar[k] = slovar[k].replace("&#39;", "'")
        slovar[k] = slovar[k].replace("amp;", "")
        slovar[k] = slovar[k].replace("&quot;", '"')
    return slovar

def znotraj_destinacije(delna_povezava):
    celotna_povezava = prvi_del_povezave + delna_povezava


def naslov(stran, seznam):
    return f'https://www.atlasobscura.com/places?page={stran}&sort={seznam[0]}_count'


def znotraj(url_podrobneje):
    return f'https://www.atlasobscura.com{url_podrobneje}'


def posamezna_destinacija(blok):
    destinacija = re.search(vzorec_destinacije, blok)
    destinacija = destinacija.groupdict()
    popravki(destinacija)
    destinacija['id'] = int(destinacija['id'])
    destinacija['url'] = znotraj(destinacija['url'])
    
    lokacija = re.search(vzorec_lokacije, blok)
    lokacija = lokacija.groupdict()
    popravki(lokacija)
    destinacija['sirina'] = float(lokacija.pop('sirina'))
    destinacija['dolzina'] = float(lokacija.pop('dolzina'))
    destinacija['mesto'] = lokacija['mesto']
    destinacija['drzava'] = lokacija['drzava']

    return destinacija

def ureditev_destinacije(destinacije):
    lokacije = []
    dodane_lokacije = set()
    for destinacija in destinacije:
        if destinacija['lokacija'] not in dodane_lokacije:
            dodane_lokacije.add(destinacija['lokacija'])
            lokacije.append({
                'lokacija': destinacija['lokacija'].strip(),
                'mesto': destinacija.pop('mesto'),
                'drzava': destinacija.pop('drzava'),
            })
    
    lokacije.sort(key=lambda lokacija: lokacija['lokacija'])

    return lokacije


def obiski_in_priljubljenost(blok):
    obiskovalci = re.search(vzorec_podrobneje, blok)
    obiskovalci = obiskovalci.groupdict()
    popravki(obiskovalci)
    obiskovalci['obiskali'] = int(obiskovalci['obiskali'])
    obiskovalci['zelja'] = int(obiskovalci['zelja'])
    return obiskovalci


def posamezna_stran(seznam):
    url = naslov(stran, seznam) 
    name = f'{seznam[1]}_{stran}.html'
    file = os.path.join(direktorij_destinacij, name)
    #orodja.shrani_spletno_stran(url, file)
    besedilo = orodja.vsebina_datoteke(file)
    for blok in re.finditer(vzorec_bloka, besedilo):
        yield posamezna_destinacija(blok.group(0))


priljubljene_destinacije = []
for stran in range(1, koncaj+1):
    for ranking, posamezna in enumerate(posamezna_stran(priljubljenost),1):
        posamezna['priljubljenost'] = 18*(stran-1) + ranking
        priljubljene_destinacije.append(posamezna)


obiskane_destinacije = []
for stran in range(1, koncaj+1):
    for ranking, posamezna in enumerate(posamezna_stran(obiskanost),1):
        posamezna['obiskanost'] = 18*(stran-1) + ranking
        obiskane_destinacije.append(posamezna)

priljubljene_lokacije = ureditev_destinacije(priljubljene_destinacije)
obiskane_lokacije = ureditev_destinacije(obiskane_destinacije)
vse_lokacije = priljubljene_lokacije

[vse_lokacije.append(lokacija) for lokacija in obiskane_lokacije if lokacija not in priljubljene_lokacije]

#orodja.zapisi_csv(priljubljene_destinacije, ['id', 'destinacija', 'lokacija', 'sirina', 'dolzina', 'opis', 'url', 'priljubljenost'], 'obdelani-podatki/priljubljene_destinacije.csv')

#orodja.zapisi_csv(obiskane_destinacije, ['id', 'destinacija', 'lokacija', 'sirina', 'dolzina', 'opis', 'url', 'obiskanost'], 'obdelani-podatki/obiskane_destinacije.csv')

#orodja.zapisi_csv(vse_lokacije, ['lokacija', 'mesto', 'drzava'], 'obdelani-podatki/lokacije.csv')