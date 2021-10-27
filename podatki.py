import re
import requests
import csv
import os

vzorec_bloka = re.compile(
    r'<div class="content-card-text">'
    r'(.*?)</been-there-everywhere>',
    flags=re.DOTALL
)

vzorec_destinacije = re.compile(
    r'href="(?P<url_konec>.*?)">.*?'
    r'place-card-location">(?P<lokacija>.*?)</div>.*?'
    r'js-title-content">(?P<destinacija>.*?)</span>.*?'
    r'js-subtitle-content">(?P<opis>.*?)</div>.*?'
    r'aria-hidden="true">.*?(?P<zem_sirina>-?\d+\.\d+),.*?'
    r'\s(?P<zem_dolzina>-?\d+\.\d+).*?'
    r'data-place-city="(?P<mesto>.*?)".*?'
    r'data-place-country="(?P<drzava>.*?)".*?'
    r'data-place-id=(?P<id>\d+?)\s',
    flags=re.DOTALL
)

vzorec_znotraj = re.compile(
    r'"DDPage__header-dek".*?'
    # r'htlbid\.setTargeting\("tags",\s\[(?P<kljucne_besede>.+?)\]\)'
    r'title-md item-action-count">(?P<obiskali>\d+?)</div>.*?'
    r'title-md item-action-count">(?P<zelijo_obiskati>\d+?)</div>'
    r'<a class="itemTags__link js-item-tags-link" href="/categories/(?P<kljucne_besede>.*?)"',
    flags=re.DOTALL
)
