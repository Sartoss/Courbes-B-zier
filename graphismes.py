# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:50:02 2017

@author: piroulasau

"""
from tkinter import *
from functools import partial

fen=Tk()
fen.title('Curve drawer')
fen['bg']='bisque'

FrameCanvas=Frame(fen,padx=5,pady=5,bg='bisque')
FrameCanvas.grid(row=0,column=0)

can=Canvas(FrameCanvas,height=500,width=500,bg="white")
can.grid()

Framesettings = Frame()
Framesettings.grid(row=0,column=1)

Ajoutpoint=LabelFrame(Framesettings,text="Ajouter un nouveau point", padx=5)
Ajoutpoint.grid(row=0)

ajouteX = Label(Ajoutpoint, text = 'X=', fg = 'black', justify='center', padx=5, pady=5)
ajouteX.grid(row=0,column=0)

EntreeX = Entry(Ajoutpoint)
EntreeX.grid(row=0,column=1)

ajouteY = Label(Ajoutpoint, text = 'Y=', fg = 'black', justify='center', padx=5, pady=5)
ajouteY.grid(row=1,column=0)

EntreeY = Entry(Ajoutpoint)
EntreeY.grid(row=1,column=1)

Valider=Button(Ajoutpoint, text = 'Valider!')
Valider.grid(row=2,column=1)

ListePoints=Frame(Framesettings, padx=5, pady=5)
ListePoints.grid(row=1)

lstpts=[]

for i in range(1,len(liste)+1):
    lstpts.append(Label(ListePoints,text="Point "+str(i)+" : x=",pady=5))
    lstpts[-1].grid(row=i,column=1)
    
    lstpts.append(Entry(ListePoints,textvariable=liste[i-1][0],width=5))
    lstpts[-1].grid(row=i,column=2)
    
    lstpts.append(Label(ListePoints,text=" y=",pady=5))
    lstpts[-1].grid(row=i,column=3)
    
    lstpts.append(Entry(ListePoints,textvariable=liste[i-1][1],width=5))
    lstpts[-1].grid(row=i,column=4)

    lstpts.append(Button(ListePoints,text="X",command=lambda:supprime(i),pady=5, padx=4))
    lstpts[-1].grid(row=i,column=5)

var=IntVar()
Traitscons=Checkbutton(Framesettings, text="Traits de construction ?", variable=var, pady=5)
Traitscons.grid(row=2)

FramePreci=Frame(Framesettings, pady=5)
FramePreci.grid(row=3)

Label1=Label(FramePreci,text="Précision de la courbe:")
Label1.grid(column=0,row=0)

ChoixPreci=Entry(FramePreci, width=10)
ChoixPreci.grid(column=1,row=0)

FrameCurvType=LabelFrame(Framesettings,text="Type de courbe désirée")
FrameCurvType.grid(row=4)

CurvType = IntVar()
Radiobutton(FrameCurvType, text="Bézier", variable=CurvType, value=1).grid(row=0)
Radiobutton(FrameCurvType, text="Type2", variable=CurvType, value=2).grid(row=1)

fen.mainloop()

#ajout point OK
#label nbr point OK
#checkbox traits de construction OK
#entry précision désirée (de base à 0.1) OK
#choix du curvtype OK
