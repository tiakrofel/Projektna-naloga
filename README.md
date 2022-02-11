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

Po analizi obdelanih podatkov smo prišli do ugotovitev, da:
* destinacije, ki se na lestvici priljubljenosti uvrščajo najvišje, ne dosegajo primerljivo visokih mest na lestvici obiskanosti;
* je v veliki večini število obiskovalcev spletne strani, ki si posamezno destinacijo še želijo obiskati, večje od tistih, ki so tam že bili in da je odklon med tema številoma še posebej velik pri destinacijah, ki na lestvici priljubljenosti zasedajo najvišja mesta;
* se največ priljubljenih nenavadnih destinacij, ki so dosegle najvišje uvrstitve na analiziranem seznamu, nahaja v mestih Združenih držav amerike, in da večina vseh leži bodisi v ZDA bodisi v Evropi, drugje po svetu pa jih je občutno manj;
* so glede na imena in opise naših nenavadnih destinacij daleč najbolj priljubljeni muzeji, sledijo pa jim parki, hiše in domovi, ki jih lahko najpogosteje opišemo s pridevniki kot so zapuščen, največji, skrit in zgodovinski, če jih omenimo le nekaj.  


*Opomba*: zaradi razporeditve destinacij po posameznih straneh na Atlas Obscura smo na vsakem izmed seznamov pridobili podatke za 8 destinacij več, torej 10.008.
