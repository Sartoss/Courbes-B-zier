from tkinter import *
from tkinter.ttk import Combobox
from math import sqrt
from functools import partial
from tkinter import messagebox

def fBezier(liste):
    if sqrt((liste[0][0]-liste[-1][0])**2+(liste[0][1]-liste[-1][1])**2)<=2:
        return(liste[0][0],liste[0][1])
    l1=liste.copy()
    l2=liste.copy()
    n=len(liste)
    for i in range(n-1):
        for j in range(i+1):
            l1[n+j-i-1]=((l1[n+j-i-2][0]+l1[n+j-i-1][0])/2,(l1[n+j-i-2][1]+l1[n+j-i-1][1])/2)
            l2[i-j]=((l2[i-j][0]+l2[i-j+1][0])/2,(l2[i-j][1]+l2[i-j+1][1])/2)
    return(fBezier(l1)+fBezier(l2))

def fSpline(liste):
    if len(liste)==2:
        return(liste[0][0],liste[0][1],liste[1][0],liste[1][1])
    points=[]
    if varTangente.get()==1 and CurvType.get()==1:
        for i in range(-varBoucle.get(),len(liste)-1):
            tax=liste[i][4]
            tay=liste[i][5]
            tbx=-liste[i+1][2]
            tby=-liste[i+1][3]
            a1=2*liste[i][0]-2*liste[i+1][0]+tax+tbx
            b1=-3*liste[i][0]+3*liste[i+1][0]-2*tax-tbx
            a2=2*liste[i][1]-2*liste[i+1][1]+tay+tby
            b2=-3*liste[i][1]+3*liste[i+1][1]-2*tay-tby
            t=0
            while t<1:
                points.append(a1*t**3+b1*t**2+tax*t+liste[i][0])
                points.append(a2*t**3+b2*t**2+tay*t+liste[i][1])
                t+=0.01
    else:
        if varBoucle.get()==1:
            for i in range(-2,len(liste)-2):
                tax=liste[i+1][0]-liste[i-1][0]
                tay=liste[i+1][1]-liste[i-1][1]
                tbx=liste[i+2][0]-liste[i][0]
                tby=liste[i+2][1]-liste[i][1]
                a1=2*liste[i][0]-2*liste[i+1][0]+tax+tbx
                b1=-3*liste[i][0]+3*liste[i+1][0]-2*tax-tbx
                a2=2*liste[i][1]-2*liste[i+1][1]+tay+tby
                b2=-3*liste[i][1]+3*liste[i+1][1]-2*tay-tby
                t=0
                while t<1:
                    points.append(a1*t**3+b1*t**2+tax*t+liste[i][0])
                    points.append(a2*t**3+b2*t**2+tay*t+liste[i][1])
                    t+=0.01
        else:
            for i in range(len(liste)-1):
                if i==0:
                    tx=liste[i+2][0]-liste[i][0]
                    ty=liste[i+2][1]-liste[i][1]
                    a1=liste[i][0]/2-liste[i+1][0]/2+tx/2
                    c1=-3*liste[i][0]/2+3*liste[i+1][0]/2-tx/2
                    a2=liste[i][1]/2-liste[i+1][1]/2+ty/2
                    c2=-3*liste[i][1]/2+3*liste[i+1][1]/2-ty/2
                    t=0
                    while t<1:
                        points.append(a1*t**3+c1*t+liste[i][0])
                        points.append(a2*t**3+c2*t+liste[i][1])
                        t+=0.01
                elif i==len(liste)-2:
                    tx=liste[i+1][0]-liste[i-1][0]
                    ty=liste[i+1][1]-liste[i-1][1]
                    a1=liste[i][0]/2-liste[i+1][0]/2+tx/2
                    b1=-3*liste[i][0]/2+3*liste[i+1][0]/2-3*tx/2
                    a2=liste[i][1]/2-liste[i+1][1]/2+ty/2
                    b2=-3*liste[i][1]/2+3*liste[i+1][1]/2-3*ty/2
                    t=0
                    while t<1:
                        points.append(a1*t**3+b1*t**2+tx*t+liste[i][0])
                        points.append(a2*t**3+b2*t**2+ty*t+liste[i][1])
                        t+=0.01
                else:
                    tax=liste[i+1][0]-liste[i-1][0]
                    tay=liste[i+1][1]-liste[i-1][1]
                    tbx=liste[i+2][0]-liste[i][0]
                    tby=liste[i+2][1]-liste[i][1]
                    a1=2*liste[i][0]-2*liste[i+1][0]+tax+tbx
                    b1=-3*liste[i][0]+3*liste[i+1][0]-2*tax-tbx
                    a2=2*liste[i][1]-2*liste[i+1][1]+tay+tby
                    b2=-3*liste[i][1]+3*liste[i+1][1]-2*tay-tby
                    t=0
                    while t<1:
                        points.append(a1*t**3+b1*t**2+tax*t+liste[i][0])
                        points.append(a2*t**3+b2*t**2+tay*t+liste[i][1])
                        t+=0.01
            points.append(liste[-1][0])
            points.append(liste[-1][1])
    return(tuple(points))

def affiche(liste):
    global can
    global fonction
    can.coords(1,fonction[CurvType.get()]([(i[0].get(),i[1].get(),i[2].get(),i[3].get(),i[4].get(),i[5].get()) for i in liste]))

def clique(event):
    global select
    x=event.x
    y=event.y
    while []!=menu:
        menu[0].destroy()
        del(menu[0])
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()-x)**2+(liste[i][1].get()-y)**2)<=rayon:
            select[0].set(i)
            select[1].set(0)
            break
        elif sqrt((liste[i][0].get()+liste[i][2].get()-x)**2+(liste[i][1].get()+liste[i][3].get()-y)**2)<=rayonTan:
            select[0].set(i)
            select[1].set(1)
            break
        elif sqrt((liste[i][0].get()+liste[i][4].get()-x)**2+(liste[i][1].get()+liste[i][5].get()-y)**2)<=rayonTan:
            select[0].set(i)
            select[1].set(2)
            break
def relache(event):
    global select
    select[0].set(-1)
    select[1].set(-1)
    
def deplacement(event):
    global select
    if select[0].get()==-1:return
    x=min(max(event.x,0),500)
    y=min(max(event.y,0),500)
    m=select[0].get()
    n=select[1].get()
    if n==0:
        liste[m][0].set(x)
        liste[m][1].set(y)
        can.coords(indic[m][0],x-rayon,y-rayon,x+rayon,y+rayon)
    else:
        liste[m][2*n].set(x-liste[m][0].get())
        liste[m][2*n+1].set(y-liste[m][1].get())
        can.coords(indic[m][n],x-rayonTan,y-rayonTan,x+rayonTan,y+rayonTan)
        can.coords(indic[m][n+2],liste[m][0].get(),liste[m][1].get(),liste[m][0].get()+liste[m][2*n].get(),liste[m][1].get()+liste[m][2*n+1].get())
    if varTangente.get()==1 and n==0:
        can.coords(indic[m][1],x+liste[m][2].get()-rayonTan,y+liste[m][3].get()-rayonTan,x+liste[m][2].get()+rayonTan,y+liste[m][3].get()+rayonTan)
        can.coords(indic[m][2],x+liste[m][4].get()-rayonTan,y+liste[m][5].get()-rayonTan,x+liste[m][4].get()+rayonTan,y+liste[m][5].get()+rayonTan)
        can.coords(indic[m][3],liste[m][0].get(),liste[m][1].get(),liste[m][0].get()+liste[m][2].get(),liste[m][1].get()+liste[m][3].get())
        can.coords(indic[m][4],liste[m][0].get(),liste[m][1].get(),liste[m][0].get()+liste[m][4].get(),liste[m][1].get()+liste[m][5].get())
    affiche(liste)

def nvpts(x,y):
    if type(x)==IntVar:x=x.get()
    if type(y)==IntVar:y=y.get()
    global rayon
    degree.set(len(liste))
    indic.append([can.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill="yellow",outline="red",width=2),-1,-1,-1,-1])
    if varTangente.get()==1 and CurvType.get()==1:
        indic[-1][1]=can.create_oval(x-50-rayonTan,y-rayonTan,x-50+rayonTan,y+rayonTan)
        indic[-1][2]=can.create_oval(x+50-rayonTan,y-rayonTan,x+50+rayonTan,y+rayonTan)
        indic[-1][3]=can.create_line(x,y,x-50,y)
        indic[-1][4]=can.create_line(x,y,x+50,y)
    liste.append((DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()))
    liste[-1][0].set(x)
    liste[-1][1].set(y)
    liste[-1][2].set(-50)
    liste[-1][3].set(0)
    liste[-1][4].set(50)
    liste[-1][5].set(0)

    affiche(liste)
       
    lstpts.append([])
    lstpts[-1].append(Label(ListePoints,text="Point "+str(indic[-1][0]-1)+" : x="))
    lstpts[-1][-1].grid(row=indic[-1][0],column=1)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[-1][0],width=5))
    lstpts[-1][-1].grid(row=indic[-1][0],column=2)
    
    lstpts[-1].append(Label(ListePoints,text=" y="))
    lstpts[-1][-1].grid(row=indic[-1][0],column=3)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[-1][1],width=5))
    lstpts[-1][-1].grid(row=indic[-1][0],column=4)

    lstpts[-1].append(Button(ListePoints,text="X",command=partial(supprime,indic[-1][0])))
    lstpts[-1][-1].grid(row=indic[-1][0],column=5)
    

def supprime(n):
    if len(liste)>2:
        for i in range(len(indic)):
            if indic[i][0]==n:
                m=i
        del(liste[m])
        can.delete(indic[m][0])
        if indic[m][1]!=-1:
            can.delete(indic[m][1])
            can.delete(indic[m][2])
            can.delete(indic[m][3])
            can.delete(indic[m][4])
        del(indic[m])
        for i in range(4,-1,-1):
            lstpts[m][i].destroy()
        del(lstpts[m])
        if CurvType.get()==0:
            degree.set(len(liste)-1)
        affiche(liste)
    else:
        messagebox.showerror("Erreur","Il ne peut pas y avoir moins de deux points")

def clicdrt(event):
    x=event.x
    y=event.y
    while []!=menu:
        menu[0].destroy()
        del(menu[0])
    menu.append(Menu(can,tearoff=0))
    menu[0].add_command(label="Ajouter un point",command=partial(nvpts,x,y))
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()-x)**2+(liste[i][1].get()-y)**2)<=10:
            menu[0].add_command(label="Supprimer le point "+str(indic[i][0]-1),command=partial(supprime,indic[i][0]))
    menu[0].post(event.x_root,event.y_root)

def changeType():
    if CurvType.get()==1:
        FrameSpline.grid(row=5)
        Entrydegre["state"]="normal"
        degree.set(3)
    else:
        FrameSpline.grid_forget()
        Entrydegre["state"]="disabled"
        degree.set(len(liste)-1)
    if varTangente.get()==1 and CurvType.get()==1 and indic[0][1]==-1:
        for i in range(len(liste)):
            indic[i][1]=can.create_oval(liste[i][0].get()+liste[i][2].get()-rayonTan,liste[i][1].get()+liste[i][3].get()-rayonTan,liste[i][0].get()+liste[i][2].get()+rayonTan,liste[i][1].get()+liste[i][3].get()+rayonTan)
            indic[i][2]=can.create_oval(liste[i][0].get()+liste[i][4].get()-rayonTan,liste[i][1].get()+liste[i][5].get()-rayonTan,liste[i][0].get()+liste[i][4].get()+rayonTan,liste[i][1].get()+liste[i][5].get()+rayonTan)
            indic[i][3]=can.create_line(liste[i][0].get(),liste[i][1].get(),liste[i][0].get()+liste[i][2].get(),liste[i][1].get()+liste[i][3].get())
            indic[i][4]=can.create_line(liste[i][0].get(),liste[i][1].get(),liste[i][0].get()+liste[i][4].get(),liste[i][1].get()+liste[i][5].get())
    elif (varTangente.get()==0 or CurvType.get()!=1) and indic[0][1]!=-1:
        for i in range(len(liste)):
            can.delete(indic[i][1])
            can.delete(indic[i][2])
            can.delete(indic[i][3])
            can.delete(indic[i][4])
            indic[i][1]=-1
            indic[i][2]=-1
            indic[i][3]=-1
            indic[i][4]=-1
    affiche(liste)

global rayon
global fonction
rayon=10
rayonTan=5

fonction=[fBezier,fSpline]
f=0

fen=Tk()
fen.title('Curve drawer')
fen['bg']='bisque'

FrameCanvas=Frame(fen,padx=5,pady=5,bg='bisque')
FrameCanvas.grid(row=0,column=0)

can=Canvas(FrameCanvas,height=500,width=500,bg="white")
can.grid()

Framesettings = Frame(fen)
Framesettings.grid(row=0,column=1,sticky="n",pady=5,padx=5)

Ajoutpoint=LabelFrame(Framesettings,text="Ajouter un nouveau point", padx=5)
Ajoutpoint.grid(row=0)

ajouteX = Label(Ajoutpoint, text = 'X=', fg = 'black', justify='center', padx=5, pady=5)
ajouteX.grid(row=0,column=0)

x=IntVar()
x.set(250)

EntreeX = Entry(Ajoutpoint,textvariable=x)
EntreeX.grid(row=0,column=1)

ajouteY = Label(Ajoutpoint, text = 'Y=', fg = 'black', justify='center', padx=5, pady=5)
ajouteY.grid(row=1,column=0)

y=IntVar()
y.set(250)

EntreeY = Entry(Ajoutpoint,textvariable=y)
EntreeY.grid(row=1,column=1)

Valider=Button(Ajoutpoint, text = 'Valider!',command=lambda:nvpts(x,y))
Valider.grid(row=2,column=1)

liste=[]
for i in range(4):
    liste.append((DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()))
liste[0][0].set(100)
liste[0][1].set(50)
liste[0][2].set(-50)
liste[0][3].set(0)
liste[0][4].set(50)
liste[0][5].set(0)
liste[1][0].set(200)
liste[1][1].set(450)
liste[1][2].set(-50)
liste[1][3].set(0)
liste[1][4].set(50)
liste[1][5].set(0)
liste[2][0].set(250)
liste[2][1].set(250)
liste[2][2].set(-50)
liste[2][3].set(0)
liste[2][4].set(50)
liste[2][5].set(0)
liste[3][0].set(450)
liste[3][1].set(100)
liste[3][2].set(-50)
liste[3][3].set(0)
liste[3][4].set(50)
liste[3][5].set(0)

ListePoints=Frame(Framesettings, padx=5, pady=5)
ListePoints.grid(row=1)


FramePreci=Frame(Framesettings, pady=5)
FramePreci.grid(row=3)

Label1=Label(FramePreci,text="Précision de la courbe:")
Label1.grid(column=0,row=0)

ChoixPreci=Entry(FramePreci, width=10)
ChoixPreci.grid(column=1,row=0)

Label2=Label(FramePreci, text="Degré de la courbe: ")
Label2.grid(column=0,row=1)

degree=StringVar()
degree.set(3)
Entrydegre=Entry(FramePreci, width=10,textvariable=degree,state="disabled")
Entrydegre.grid(row=1,column=1)


FrameCurvType=LabelFrame(Framesettings,text="Type de courbe désirée")
FrameCurvType.grid(row=4)

CurvType = IntVar()
CurvType.set(0)
Radiobutton(FrameCurvType, text="Bézier", variable=CurvType, value=0, command=changeType).grid(row=0)
Radiobutton(FrameCurvType, text="Spline", variable=CurvType, value=1, command=changeType).grid(row=1)

FrameSpline=Frame(Framesettings,pady=5)

varBoucle=IntVar()
Courbefermee=Checkbutton(FrameSpline, text="Courbe fermée ?", variable=varBoucle, pady=5,command=changeType)
Courbefermee.grid()

varTangente=IntVar()
tangentes=Checkbutton(FrameSpline, text="Tangentes manuelles ?", variable=varTangente, pady=5,command=changeType)
tangentes.grid()

can.create_line(fBezier([(i[0].get(),i[1].get()) for i in liste]),fill="blue",width=2)
indic=[]
for i in liste:
    p=can.create_oval(i[0].get()-rayon,i[1].get()-rayon,i[0].get()+rayon,i[1].get()+rayon,fill="yellow",outline="red",width=2)
    indic.append([p,-1,-1,-1,-1])

lstpts=[]
    
for i in range(2,len(liste)+2):
    lstpts.append([])
    lstpts[-1].append(Label(ListePoints,text="Point "+str(indic[i-2][0]-1)+" : x="))
    lstpts[-1][-1].grid(row=i,column=1)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[i-2][0],width=5))
    lstpts[-1][-1].grid(row=i,column=2)
    
    lstpts[-1].append(Label(ListePoints,text=" y="))
    lstpts[-1][-1].grid(row=i,column=3)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[i-2][1],width=5))
    lstpts[-1][-1].grid(row=i,column=4)

    lstpts[-1].append(Button(ListePoints,text="X",command=partial(supprime,indic[i-2][0])))
    lstpts[-1][-1].grid(row=i,column=5)

select=[IntVar(),IntVar()]
select[0].set(-1)
select[1].set(-1)

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)
menu=[]
can.bind("<ButtonPress-3>",clicdrt)

fen.mainloop()
