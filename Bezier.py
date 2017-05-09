from tkinter import *
from tkinter.ttk import Combobox
from math import sqrt,factorial as fact

def f(t,liste):
    n=len(liste)
    return(sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][0] for i in range(n)),sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][1] for i in range(n)))

def affiche(liste,pas,coeff):
    p=f(0,liste)
    points=p[0]*coeff,p[1]*coeff
    t=pas
    while t<=1:
        p2=f(t,liste)
        p=p2
        points+=p[0]*coeff,p[1]*coeff
        t+=pas
    can.coords(5,points)

def clique(event):
    x=event.x
    y=event.y
    for i in liste:
        if sqrt((i[0]*100-x)**2+(i[1]*100-y)**2)<=10:
            global select
            select=indic[liste.index(i)]
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
    liste[indic.index(select)]=(x/100,y/100,liste[indic.index(select)][2])
    can.coords(select,x-10,y-10,x+10,y+10)
    affiche(liste,0.01,100)

    
def nvpts():
    indic.append(can.create_oval(240,240,260,260))
    can.itemconfig(indic[-1],fill="yellow",outline="red",width=2)
    liste.append((2.50,2.50))
    for i in range(len(liste)):
        liste[i]=(liste[i][0],liste[i][1],fact(len(liste)-1)//(fact(i)*fact(len(liste)-i-1)))
    affiche(liste,0.01,100)    
    

fen=Tk()
can=Canvas(height=500,width=500,bg="white")
can.pack(side=LEFT)
sf=Frame(fen)
sf.pack(side=RIGHT)
lab=Label(sf,text="")
lab.pack()

lstbtn=[]
lstbtn.append(Button(sf,text="Nouveau point",command=nvpts))
lstbtn[0].pack()

rayon=10

liste=[(0,0),(0,5),(3,0),(5,5)]
indic=[1,2,3,4]
liste=[(liste[i][0],liste[i][1],fact(len(liste)-1)//(fact(i)*fact(len(liste)-i-1))) for i in range(len(liste))]

coeff=100
pas=t=0.01
p=f(0,liste)

for i in liste:
    can.create_oval(i[0]*coeff-rayon,i[1]*coeff-rayon,i[0]*coeff+rayon,i[1]*coeff+rayon)
    can.itemconfig(liste.index(i)+1,fill="yellow",outline="red",width=2)
points=p[0]*100,p[1]*100
while t<=1:
        p2=f(t,liste)
        p=p2
        points+=p[0]*100,p[1]*100
        t+=pas
can.create_line(points,fill="blue",width=2)


can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)

fen.mainloop()
