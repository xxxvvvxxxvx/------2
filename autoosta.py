#opp
#class
#__init__
#self
#def - metode

#Autoostas_saraksts

class AOsist():
  def __init__(self):
    pass

import requests
from bs4 import BeautifulSoup

lapa = requests.get("")

#print(lapa)

saturs=BeautifulSoup(lapa.content, 'html.parser')
print(saturs)