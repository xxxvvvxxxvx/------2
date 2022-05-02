#opp
#class
#__init__
#self
#def - metode

#Autoostas_saraksts

import sqlite3

class AOSistema():
  def __init__(self, sakumpunkts, galapunkts):
    self.sakumpunkts = sakumpunkts
    self.galapunkts = galapunkts



import PySimpleGUI as sg

sg.theme("DarkAmber")
layout= [ sg.TEXT('Autoostas informācijas sistēma')],
        [sg.Text('Sākumpunkts:'), sg.InputText()],
        [sg.Text ('Galapunkts:'), sg.InputText()],
        [sg.Button ('Meklēt')],

layout2=[(sg.Text('kks text'))]

tabgrp = [
  [
    sg.TabGroup([[
      sg.Tab('Maršruti', layout),
      sg.Tab ('Biļetes', layout2 )
    ]])
    sg.Button('Aizvērt')
  ]
]

window = sg.window('AOSistema', tabgrp)
while True:
  event, values =window.read()
  if event == "Meklēt":
    

  
  
  













































if event in (sg.WIN_CLOSED, 'Aizvert'):
    break


windows.close()