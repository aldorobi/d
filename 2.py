# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 15:16:36 2023

@author: Cindy jinnet
"""


from tkinter import *
import requests
import json

spidergame = Tk()
spidergame.title("wasa!")
spidergame.geometry("300x400")
spidergame.configure(background = "midnightblue")

titulo = Label(spidergame,text = "その上！ 映画",bg = ("cyan"),font = ("comic sans",20,"bold") )
titulo.place(relx = 0.5,rely = 0.15,anchor = CENTER)


entry = Entry(spidergame,bg = "whitesmoke")
entry.place(relx = 0.5 , rely = 0.25 , anchor = CENTER)


"""
pais
"""
abe2 = Label(spidergame,text = "国")
abe2.place(relx = 0.3 , rely = 0.45 , anchor = CENTER)

be2 = Label(spidergame,text = "")
be2.place(relx = 0.7 , rely = 0.45 , anchor = CENTER)
"""
region
"""
abeeba = Label(spidergame,text = "領域")
abeeba.place(relx = 0.3 , rely = 0.55 , anchor = CENTER)

bebe = Label(spidergame,text = "")
bebe.place(relx = 0.7 , rely = 0.55 , anchor = CENTER)
"""
sigla
"""
abeebabee = Label(spidergame,text = "イニシャル")
abeebabee.place(relx = 0.3 , rely = 0.65 , anchor = CENTER)

ebeb = Label(spidergame,text = "")
ebeb.place(relx = 0.7 , rely = 0.65 , anchor = CENTER)
"""
poblacion
"""
abeebabee2 = Label(spidergame,text = "人口")
abeebabee2.place(relx = 0.3 , rely = 0.75 , anchor = CENTER)

ebbeeb = Label(spidergame,text = "")
ebbeeb.place(relx = 0.7 , rely = 0.75 , anchor = CENTER)

def Nazenara ():
    
    Apio = requests.get("https://restcountries.com/v3.1/capital/" + entry.get())
    oipA = json.loads(Apio.content)
    Paisan = oipA[0]['name']['common']
    print(Paisan)

    be2['text'] = Paisan
    
    regional = oipA[0]['region']
    print(regional)

    bebe['text'] = regional
    
    Siglanial = oipA[0]['flag']
    print(Siglanial)

    ebeb['text'] = Siglanial
    
    poblacionial = oipA[0]['population']
    print(poblacionial)

    ebbeeb['text'] = poblacionial
    
    
botonMagico2 = Button(spidergame, text = "始める？",bg = "ghost white", command  = Nazenara)
botonMagico2.place(relx = 0.5 , rely = 0.35, anchor = CENTER)





spidergame.mainloop()

