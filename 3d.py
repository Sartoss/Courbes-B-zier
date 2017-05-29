from tkinter import *
from math import *
from functools import partial
from tkinter import messagebox
from time import time
fichier=open("calcul.py","r")
exec(fichier.read())
fichier.close()
fichier=open("interaction.py","r")
exec(fichier.read())
fichier.close()
fichier=open("parametres.py","r")
exec(fichier.read())
fichier.close()

def affiche(liste):
	global can
	global fonction
	can.coords(1,fonction[CurvType.get()]([(i[0].get(),i[1].get(),i[2].get(),i[3].get(),i[4].get(),i[5].get()) for i in liste]))

def conv3d(liste):
    points=[]
    ang=pdv[4].get()
    ang2=pdv[3].get()
    x1=pdv[0].get()
    y1=pdv[1].get()
    z1=pdv[2].get()
    for i in range(len(liste)):
        x2=liste[i][0]
        y2=liste[i][1]
        z2=liste[i][2]
        a=3*pi/4-ang-atan2(z2-z1,x2-x1)
        b=3*pi/4-ang2-atan2(z2-z1,y2-y1)
        points.append((2*a/pi*500,2*b/pi*500))
    return points

global rayon
global fonction

fen=Tk()

rayon=10
rayonTan=5
fonction=[fBezier,fSpline,fBspline]

posr=[]
pospix=[]
noeud=[]
indic=[]
menu=[]
lstpts=[]
lstnoeuds=[]
select=[IntVar(),IntVar()]
x=DoubleVar()
y=DoubleVar()
z=DoubleVar()
degree=IntVar()
CurvType=IntVar()
varBoucle=IntVar()
varTangente=IntVar()
pdv=[DoubleVar() for i in range(6)]


#valeurs par défaut

pdv[0].set(1)
pdv[1].set(1.5)
pdv[2].set(-5)

x.set(250)
y.set(250)
for i in [(1,1.50,-1),(1,-1.5,98),(2.5,2.5,-2),(1,-3,8)]:
    posr.append((DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()))
    posr[-1][0].set(i[0])
    posr[-1][1].set(i[1])
    posr[-1][2].set(i[2])
    posr[-1][3].set(-50)
    posr[-1][4].set(0)
    posr[-1][5].set(50)
    
pospix=conv3d([(i[0].get(),i[1].get(),i[2].get()) for i in posr])

for i in range(4):
	noeud.append(DoubleVar())
	noeud[-1].set(0)
for i in range(4):
	noeud.append(DoubleVar())
	noeud[-1].set(1)
degree.set(3)
CurvType.set(0)
select[0].set(-1)
select[1].set(-1)

fen.columnconfigure(0,weight=1)
fen.columnconfigure(1,weight=0)
fen.rowconfigure(0,weight=1)
fen.title('Curve drawer')
fen['bg']='bisque'

FrameCanvas=Frame(fen,padx=5,pady=5,bg='bisque')
FrameCanvas.grid(row=0,column=0,sticky='nsew')
FrameCanvas.columnconfigure(0,weight=1)
FrameCanvas.rowconfigure(0,weight=1)

can=Canvas(FrameCanvas,height=500,width=500,bg="white")
can.grid(row=0,column=0,sticky='nsew')
#print(fBezier([(i[0],i[1]) for i in pospix]))
can.create_line(fBezier([(i[0],i[1]) for i in pospix]),fill="blue",width=2)
can.create_line(conv3d([(0,0,0),(0,0,1)]),fill="red",width=2,arrow=LAST)
can.create_line(conv3d([(0,0,0),(0,1,0)]),fill="blue",width=2,arrow=LAST)
can.create_line(conv3d([(0,0,0),(1,0,0)]),fill="green",width=2,arrow=LAST)

for i in pospix:
	p=can.create_oval(i[0]-rayon,i[1]-rayon,i[0]+rayon,i[1]+rayon,fill="yellow",outline="red",width=2)
	indic.append([p,-1,-1,-1,-1])

Framesettings = Frame(fen)
Framesettings.grid(row=0,column=1,sticky='nsew',pady=5,padx=5)

Ajoutpoint=LabelFrame(Framesettings,text="Ajouter un nouveau point", padx=5)
Ajoutpoint.grid(row=0)

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
ListePoints.grid(row=1)

for i in range(len(pospix)):
    lstpts.append([])
    lstpts[-1].append(Label(ListePoints,text="Point "+str(i+1)+" : x="))
    lstpts[-1][-1].grid(row=i,column=0)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=posr[i][0],width=5))
    lstpts[-1][-1].grid(row=i,column=1)
    lstpts[-1][-1].bind("<Return>",valider)
    
    lstpts[-1].append(Label(ListePoints,text=" y="))
    lstpts[-1][-1].grid(row=i,column=2)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=posr[i][1],width=5))
    lstpts[-1][-1].grid(row=i,column=3)
    lstpts[-1][-1].bind("<Return>",valider)
    
    lstpts[-1].append(Button(ListePoints,text="X",command=partial(supprime,indic[i][0])))
    lstpts[-1][-1].grid(row=i,column=4)

FramePreci=Frame(Framesettings, pady=5)
FramePreci.grid(row=3)

Label(FramePreci,text="Précision de la courbe:").grid(column=0,row=0)

ChoixPreci=Entry(FramePreci, width=10)
ChoixPreci.grid(column=1,row=0)

Label(FramePreci, text="Degré de la courbe: ").grid(column=0,row=1)

Entrydegre=Entry(FramePreci, width=10,textvariable=degree,state="disabled")
Entrydegre.grid(row=1,column=1)
Entrydegre.bind("<Return>",changeDegree)

FrameCurvType=LabelFrame(Framesettings,text="Type de courbe désirée")
FrameCurvType.grid(row=4)

Radiobutton(FrameCurvType, text="Bézier", variable=CurvType, value=0, command=changeType).grid(row=0)
Radiobutton(FrameCurvType, text="Spline", variable=CurvType, value=1, command=changeType).grid(row=1)
Radiobutton(FrameCurvType, text="B-Spline", variable=CurvType, value=2, command=changeType).grid(row=2)

FrameSpline=Frame(Framesettings,pady=5)

Courbefermee=Checkbutton(FrameSpline, text="Courbe fermée ?", variable=varBoucle, pady=5,command=changeType)
Courbefermee.grid()

tangentes=Checkbutton(FrameSpline, text="Tangentes manuelles ?", variable=varTangente, pady=5,command=changeType)
tangentes.grid()

FrameBSpline=Frame(Framesettings,pady=5)

ListeNoeuds=Frame(FrameBSpline, padx=5, pady=5)
ListeNoeuds.grid(row=0,column=0)

for i in range(8):
    lstnoeuds.append([])
    
    lstnoeuds[-1].append(Label(ListeNoeuds,text="Noeud "+str(i+1)+" :"))
    lstnoeuds[-1][-1].grid(row=i,column=0)
    
    lstnoeuds[-1].append(Entry(ListeNoeuds,textvariable=noeud[i],width=15))
    lstnoeuds[-1][-1].grid(row=i,column=1)
    lstnoeuds[-1][-1].bind("<Return>",valider)

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)
can.bind("<ButtonPress-3>",clicdrt)

fen.mainloop()
