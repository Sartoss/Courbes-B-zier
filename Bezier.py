from tkinter import *
from tkinter.ttk import Combobox
from math import sqrt,factorial as fact

def f(liste):
    if sqrt((liste[0][0]-liste[-1][0])**2+(liste[0][1]-liste[-1][1])**2)<1:
        return(liste[0][0],liste[0][1])
    l1=liste.copy()
    l2=liste.copy()
    n=len(liste)
    for i in range(n-1):
        for j in range(i+1):
            l1[n+j-i-1]=((l1[n+j-i-2][0]+l1[n+j-i-1][0])/2,(l1[n+j-i-2][1]+l1[n+j-i-1][1])/2)
            l2[i-j]=((l2[i-j][0]+l2[i-j+1][0])/2,(l2[i-j][1]+l2[i-j+1][1])/2)
    return(f(l1)+f(l2))

def affiche(liste):
    points=f(liste)
    can.coords(1,points)

def clique(event):
    x=event.x
    y=event.y
    for i in range(len(liste)):
        if sqrt((liste[i][0]-x)**2+(liste[i][1]-y)**2)<=10:
            global select
            select=i
            break

def relache(event):
    global select
    select=None

def deplacement(event):
    global select
    if select==None:return
    x=event.x
    y=event.y
    lab.config(text="x,y="+str(x)+" , "+str(y)+" "+str(select))
    liste[select]=(x,y)
    can.coords(select+2,x-10,y-10,x+10,y+10)
    affiche(liste)

def nvpts():
    can.create_oval(240,240,260,260,fill="yellow",outline="red",width=2)
    liste.append((250,250))
    for i in range(len(liste)):
        liste[i]=(liste[i][0],liste[i][1])
    affiche(liste)

H=500
W=500
rayon=10

liste=[(10,10),(10,H-10),(W-10,10),(W-10,H-10)]

fen=Tk()
fen.config(bg="bisque")
fen.title("Courbe de bézier")

sf=Frame(fen)
sf.grid(row=0,column=1)

lab=Label(sf,text="x,y=...")
lab.pack()

boutton=Button(sf,text="Nouveau point",command=nvpts)
boutton.pack()

can=Canvas(height=H,width=W,bg="white")
can.grid(row=0,column=0)

points=f(liste)
can.create_line(points,fill="blue",width=2)

for i in range(len(liste)):
    can.create_oval(liste[i][0]-rayon,liste[i][1]-rayon,liste[i][0]+rayon,liste[i][1]+rayon,fill="yellow",outline="red",width=2)

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)

fen.mainloop()
