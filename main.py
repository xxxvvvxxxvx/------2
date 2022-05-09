#OOP
#class
#__init__
#self
#def - metode

#Autobusu saraksts

import sqlite3

class AOsist():
  def __init__(self, sakumpunkts, galapunkts):
    self.sakumpunkts = sakumpunkts
    self.galapunkts = galapunkts
    
  def Marsruti(self):
    if self.sakumpunkts == "Rīga" and self.galapunkts == "Berlin":
      self.cena = 56
      self.ilgums = 23
      
  def Laiks_cela(self):
    return f"Maršruta {self.sakums} - {self.galapunkts} ilgums ir {self.ilgums} h, cena - {self.cena} EUR"

  def Cena(self):
    return "Šeit būs cena"

  def Pakalpojuma_info(self):
    return "Šeit būs izvēlētais maršruts, ilgums, sākuma laiks, beigu laiks, cena"

  def Pakalpojuma_infoprint(self):
    db = sqlite3.connect('datti.db')
    db.execute(
  """
  CREATE TABLE IF NOT EXISTS marsruti
  (id   INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
  sakumpunkts   TEXT,
  galapunkts   TEXT,
  cena FLOAT,
  laiks FLOAT
  )
  """
  )
    db.execute("""
           INSERT INTO marsruti
           (sakumpunkts,galapunkts,cena,laiks)
           VALUES(:sakumpunkts,:galapunkts,:cena,:laiks)
           """,{'sakumpunkts':self.sakums,'galapunkts':self.galapunkts,'cena':self.cena,'laiks':self.ilgums})

    db.commit()

  def Klients_info(self,vards,uzvards,per_kods,tel_nr):
    self.vards = vards
    self.uzvards = uzvards
    self.per_kods = per_kods
    self.tel_nr = tel_nr
    
    return f"Vārds: {self.vards}, uzvārds: {self.uzvards}, personas kods: {self.per_kods}, telefona numurs: {self.tel_nr}"

  def Klients_infoprint(self):
    db = sqlite3.connect('dati.db')
    db.execute(
  """
  CREATE TABLE IF NOT EXISTS klients
  (id   INTEGER   PRIMARY KEY AUTOINCREMENT   NOT NULL,
  vards   TEXT,
  uzvards   TEXT,
  per_kods TEXT,
  tel_nr INT
  )
  """
  )
    db.execute("""
           INSERT INTO klients
           (vards,uzvards,per_kods,tel_nr)
           VALUES(:vards,:uzvards,:per_kods,:tel_nr)
           """,{'vards':self.vards,'uzvards':self.uzvards,'per_kods':self.per_kods,'tel_nr':self.tel_nr})

    db.commit()

  def datuIzvade(self):
    db = sqlite3.connect('dati.db')
    dati = db.execute("""
               SELECT * FROM marsruti
               JOIN klients
                ON marsruti.id = klients.id
                  """)
    rezultats = dati.fetchall()
    return rezultats

import PySimpleGUI as sg

sg.theme('DarkRed')   
layout = [  [sg.Text('AO informācijas sistēma')],
            [sg.Text('Sākums:'), sg.InputText()],
            [sg.Text('Galamērķis:'), sg.InputText()],
            [sg.Button('Meklēt')],  #Meklēšana failā
            [sg.Text('Laiks', key='-LAIKS-')]] 

layout2 = [[sg.Text("Maršruts:", key = '-MARSRUTS-')],
            [sg.Text('Vārds:'), sg.InputText()],
            [sg.Text('Uzvārds:'), sg.InputText()],
           [sg.Text('Personas kds:'), sg.InputText()],
            [sg.Text('Telefona numurs:'), sg.InputText()],
            [sg.Button('Nopirkt')],
            [sg.Text('Personas dati', key='-DATI-')]]

layout3 = [[sg.Text("Dati", key = '-DATUB-')]]

tabgrp = [
  [
    sg.TabGroup([[
      sg.Tab('Maršruts',layout ), 
      sg.Tab('Pirkt biļeti',layout2),
      sg.Tab('Dati',layout3)
    ]]),
    sg.Button('Aizvērt')
  ]
]
 
window = sg.Window('InfoSistēma', tabgrp)
while True:             
  event, values = window.read()
  if event == "Meklēt":
      sakumpunkts = values[0]
      galapunkts = values[1]
      #Izveidojam mainīgo, kuram tiek piedēvēta klase (ar visām metodēm)
      marsruts = DzInfSistema(sakumpunkts,galapunkts)
      marsruts.Marsruti()
      window['-LAIKS-'].update(marsruts.Laiks_cela())
      window['-MARSRUTS-'].update(marsruts.Laiks_cela())

  if event == "Pirkt":
    vards = values[2]
    uzvards = values[3]
    per_kods = values[4]
    tel_nr = values[5]

    window['-DATI-'].update(marsruts.Klients_info(vards,uzvards,per_kods,tel_nr))

    marsruts.Pakalpojuma_info_print()
    marsruts.Klients_info_print()

    window['-DATUB-'].update(marsruts.datuIzvade())
    
  if event in (sg.WIN_CLOSED, 'Aizvērt'):
      break

window.close()