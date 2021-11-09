# Najbolj priljubljene nenavadne destinacije po svetu

Analizirala bom prvih 10.000 najbolj priljubljenih nenavadnih destinacij po svetu, objavljenih na spletni strani [Atlas Obscura](https://www.atlasobscura.com/places?sort=likes_count).

Za vsako destinacijo sem pridobila:
* ime destinacije,
* koordinate,
* kraj,
* državo,
* kratek opis,
* uvrstitev na seznamu najbolj priljubljenih destinacij,
* število obiskovalcev spletne strani, ki so jo obiskali,
* število obiskovalcev spletne strani, ki si jo želijo obiskati.

Obenem si bom ogledala še 10.000 najbolj obiskanih destinacij, za katere sem pridobila:
* ime destinacije,
* koordinate,
* kraj,
* državo,
* kratek opis,
* uvrstitev na seznamu najbolj obiskanih destinacij.

Datoteka `podatki.py` vsebuje postopek zajema, v mapi `datoteke` so relevantne HTML datoteke, v mapi `obdelani-podatki` pa so CSV datoteke s podatki, ki jih bom analizirala.

Natančneje:
* datoteka *priljubljene_destinacije.csv* vsebuje id, ime destinacije, njeno lokacijo, zemljepisno širino in dolžino, kratek opis, url in uvrstitev na lestvici priljubljenosti za vsako izmed prvih 10.000 najbolj priljubljenih destinacij;
* datoteka *obiskane_destinacije.csv* vsebuje id, ime destinacije, njeno lokacijo, zemljepisno širino in dolžino, kratek opis, url in uvrstitev na lestvici obiskanosti za vsako izmed prvih 10.000 najbolj obiskanih destinacij;
* datoteka *lokacije.csv* vsebuje ime lokacije ter mesto in državo vsake lokacije, ki se pojavi bodisi med obiskanimi bodisi med priljubljenimi destinacijami, kar je relevantno za nadaljno analizo pri npr. ameriških destinacijah, kjer je v imenu lokacije navedena le zvezna država, šele kot država pa so izpostavljene ZDA;
* datoteka *glasovi.csv* vsebuje id destinacije, število obiskovalcev spletne strani, ki si jo želijo obiskati in število tistih, ki so jo že obiskali, in sicer za vsako izmed prvih 10.000 najbolj priljubljenih destinacij, ki jih bom na podlagi tega lahko podrobneje analizirala.

Delovne hipoteze:
* Ali so najbolj priljubljene destinacije tudi med najbolj obiskanimi glede na splošno uvrstitev na seznamih?
* Kakšna je povezava med številom obiskovalcev spletne strani, ki so posamezno destinacijo že obiskali, in številom tistih, ki si jo želijo obiskati? Ali se glede na uvrstitev na seznamu priljubljenosti destinacij razmerje med tema številoma spreminja?
* V katerih mestih in državah se nahaja največ priljubljenih nenavadnih destinacij?
* Ali obstaja kakšen tip destinacije, ki je še posebej priljubljen (npr. pokopališča, muzeji, ruševine...)?


