from tkinter import *
from math import sqrt
from functools import partial
from tkinter import messagebox
from platform import system

fichier=open("calcul.py","r")
exec(fichier.read()) #permet de récupérer le contenu du fichier auxiliaire calcul.py
fichier.close()
fichier=open("interaction.py","r")
exec(fichier.read())
fichier.close()
fichier=open("parametres.py","r")
exec(fichier.read())
fichier.close()
fichier=open("easterEgg.py","r")
exec(fichier.read())
fichier.close()

def affiche(liste):
    """
    Fonction qui affiche la courbe
    """
    l=[]
    for i in liste:
        a=convp(i[0].get(),i[1].get())
        b=convp(i[0].get()+i[2].get(),i[1].get()+i[3].get())
        c=convp(i[0].get()+i[4].get(),i[1].get()+i[5].get())
        l.append((a[0],a[1],b[0]-a[0],b[1]-a[1],c[0]-a[0],c[1]-a[1],i[6].get()))
    l=fonction[CurvType.get()](l)
    if CurvType.get()!=1 or varBoucle.get()!=1:
        l+=(a[0],a[1])
    can.coords(1,l)

global rayon
global fonction

fen=Tk() #initialise fen comme une fenêtre Tkinter

#initialisation des variables et des constantes
rayon=10
rayonTan=5
fonction=[fBezier,fSpline,fBspline,fNurbs]

liste=[]
noeud=[]
indic=[]
menu=[]
lstpts=[]
lstnoeuds=[]
select=[IntVar(),IntVar(),DoubleVar(),DoubleVar()]
x=DoubleVar()
y=DoubleVar()
degree=IntVar()
transRot=IntVar()
CurvType=IntVar()
varBoucle=IntVar()
varTangente=IntVar()
xrep=DoubleVar()
yrep=DoubleVar()
ang=DoubleVar()
zoom=DoubleVar()

#valeurs par défaut
x.set(0)
y.set(0)
for i in [(-4.0,0.0),(-2.0,-4.0),(4.0,4.0),(1.5,-3.5)]:
    liste.append((DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()))
    liste[-1][0].set(i[0])
    liste[-1][1].set(i[1])
    liste[-1][2].set(-1)
    liste[-1][3].set(0)
    liste[-1][4].set(1)
    liste[-1][5].set(0)
    liste[-1][6].set(1)
for i in range(4):
    noeud.append(DoubleVar())
    noeud[-1].set(0)
for i in range(4):
    noeud.append(DoubleVar())
    noeud[-1].set(1)
degree.set(3)
transRot.set(0)
CurvType.set(0)
select[0].set(-1)
select[1].set(-1)
xrep.set(250)
yrep.set(250)
ang.set(0)
zoom.set(50)

fen.columnconfigure(0,weight=1)
fen.columnconfigure(1,weight=0)
fen.rowconfigure(0,weight=1)
fen.title('Curve drawer')
fen['bg']='bisque'

#place les premiers éléments de la fenêtre
FrameCanvas=Frame(fen,padx=5,pady=5,bg='bisque')
FrameCanvas.grid(row=0,column=0,sticky='nsew')
FrameCanvas.columnconfigure(0,weight=1)
FrameCanvas.rowconfigure(0,weight=1)

can=Canvas(FrameCanvas,height=500,width=500,bg="white")
can.grid(row=0,column=0,sticky='nsew')

can.create_line(fBezier([(i[0].get(),i[1].get()) for i in liste]),fill="blue",width=2)
rep=convp(0,0)
a=convp(1,0)
b=convp(0,1)
can.create_line(rep[0],rep[1],a[0],a[1],fill="red",width=2,arrow="last")
can.create_line(rep[0],rep[1],b[0],b[1],fill="green",width=2,arrow="last")

for i in liste:
    i=convp(i[0].get(),i[1].get())
    p=can.create_oval(i[0]-rayon,i[1]-rayon,i[0]+rayon,i[1]+rayon,fill="yellow",outline="red",width=2)
    indic.append([p,-1,-1,-1,-1])

#crée le menu des paramètres
Framesettings = Frame(fen)
Framesettings.grid(row=0,column=1,sticky='nsew',pady=5,padx=5)

Ajoutpoint=LabelFrame(Framesettings,text="Ajouter un nouveau point", padx=5)
Ajoutpoint.grid(row=0,columnspan=2)

ajouteX = Label(Ajoutpoint, text = 'X=', fg = 'black', justify='center', padx=5, pady=5)
ajouteX.grid(row=0,column=0)

EntreeX = Entry(Ajoutpoint,textvariable=x)
EntreeX.grid(row=0,column=1)

ajouteY = Label(Ajoutpoint, text = 'Y=', fg = 'black', justify='center', padx=5, pady=5)
ajouteY.grid(row=1,column=0)

EntreeY = Entry(Ajoutpoint,textvariable=y)
EntreeY.grid(row=1,column=1)

Valider=Button(Ajoutpoint, text = 'Valider!',command=lambda:nvpts(x,y))
Valider.grid(row=2,column=1)

ListePoints=Frame(Framesettings, padx=5, pady=5)
ListePoints.grid(row=1,column=0)

ListePoids=Frame(Framesettings, padx=5, pady=5)

#crée la liste des points du menu paramètres
for i in range(len(liste)):
    lstpts.append([])
    lstpts[-1].append(Label(ListePoints,text="Point "+str(i+1)+" : x="))
    lstpts[-1][-1].grid(row=i,column=0)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[i][0],width=5))
    lstpts[-1][-1].grid(row=i,column=1)
    lstpts[-1][-1].bind("<Return>",valider)
    
    lstpts[-1].append(Label(ListePoints,text=" y="))
    lstpts[-1][-1].grid(row=i,column=2)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[i][1],width=5))
    lstpts[-1][-1].grid(row=i,column=3)
    lstpts[-1][-1].bind("<Return>",valider)
    
    lstpts[-1].append(Button(ListePoints,text="X",command=partial(supprime,indic[i][0])))
    lstpts[-1][-1].grid(row=i,column=4)
    
    lstpts[-1].append(Label(ListePoids,text="poids="))
    lstpts[-1][-1].grid(row=i,column=0)
    
    lstpts[-1].append(Entry(ListePoids,textvariable=liste[i][6],width=5))
    lstpts[-1][-1].grid(row=i,column=1,pady=4)
    lstpts[-1][-1].bind("<Return>",valider)

FramePreci=Frame(Framesettings, pady=5)
FramePreci.grid(row=3,columnspan=2, padx=5, pady=5)

Label(FramePreci, text="Degré de la courbe :").grid(column=0,row=1)

Entrydegre=Entry(FramePreci, width=10,textvariable=degree,state="disabled")
Entrydegre.grid(row=1,column=1)
Entrydegre.bind("<Return>",changeDegree)

FrameTransRot=Frame(Framesettings)
FrameTransRot.grid(row=4,columnspan=2)

Radiobutton(FrameTransRot, text="Translation", variable=transRot, value=0).grid(row=0,column=0)
Radiobutton(FrameTransRot, text="Rotation", variable=transRot, value=1).grid(row=0,column=1)

Label(FrameTransRot,text="Zoom (px) :").grid(row=1,column=0)

EntryZoom=Entry(FrameTransRot,textvariable=zoom)
EntryZoom.grid(row=1,column=1)
EntryZoom.bind("<Return>",valider)

ButtonCentrer=Button(FrameTransRot,text="Centrer", command=centrer)
ButtonCentrer.grid(row=2,column=0,columnspan=2)

FrameCurvType=LabelFrame(Framesettings,text="Type de courbe désirée")
FrameCurvType.grid(row=5,columnspan=2)

Radiobutton(FrameCurvType, text="Bézier", variable=CurvType, value=0, command=changeType).grid(row=0)
Radiobutton(FrameCurvType, text="Spline", variable=CurvType, value=1, command=changeType).grid(row=1)
Radiobutton(FrameCurvType, text="B-Spline", variable=CurvType, value=2, command=changeType).grid(row=2)
Radiobutton(FrameCurvType, text="Nurbs", variable=CurvType, value=3, command=changeType).grid(row=3)

FrameSpline=Frame(Framesettings,pady=5)

Courbefermee=Checkbutton(FrameSpline, text="Courbe fermée ?", variable=varBoucle, pady=5,command=changeType)
Courbefermee.grid()

tangentes=Checkbutton(FrameSpline, text="Tangentes manuelles ?", variable=varTangente, pady=5,command=changeType)
tangentes.grid()

FrameBSpline=Frame(Framesettings,pady=5)

ListeNoeuds=Frame(FrameBSpline, padx=5, pady=5)
ListeNoeuds.grid(row=0,column=0)

#crée le menu des noeuds pour les B-splines
for i in range(8):
    lstnoeuds.append([])
    
    lstnoeuds[-1].append(Label(ListeNoeuds,text="Noeud "+str(i+1)+" :"))
    lstnoeuds[-1][-1].grid(row=i,column=0)
    
    lstnoeuds[-1].append(Entry(ListeNoeuds,textvariable=noeud[i],width=15))
    lstnoeuds[-1][-1].grid(row=i,column=1)
    lstnoeuds[-1][-1].bind("<Return>",valider)

affiche(liste)

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)
can.bind("<ButtonPress-3>",clicdrt)
if system()=="Windows":
    fen.bind("<MouseWheel>",partial(molette,"W"))
elif system()=="Linux":
    fen.bind("<Button-4>",partial(molette,"Lu"))
    fen.bind("<Button-5>",partial(molette,"Ld"))
fen.bind("<KeyPress>",clavier)

fen.mainloop()
