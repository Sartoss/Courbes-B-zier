from tkinter import *
from math import sqrt,factorial as fact

def f(t,liste):
    n=len(liste)
    return(sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][0] for i in range(n)),sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][1] for i in range(n)))

def clique(event):
    x=event.x
    y=event.y
    for i in liste:
        if sqrt((i[0]*100-x)**2+(i[1]*100-y)**2)<=10:
            global select
            select=liste.index(i)
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
    liste[select]=(x/100,y/100,liste[select][2])
    
    p=f(0,liste)
    points=p[0]*100,p[1]*100
    pas=t=0.01
    while t<=1:
        p2=f(t,liste)
        p=p2
        points+=p[0]*100,p[1]*100
        t+=pas
    can.coords(5,points)
    can.coords(select+1,x-10,y-10,x+10,y+10)

fen=Tk()
can=Canvas(height=500,width=500,bg="white")
can.pack()
lab=Label(fen,text="")
lab.pack()


rayon=10

liste=[(0,0),(0,5),(3,0),(5,5)]
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
    
global select
select=None

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)

fen.mainloop()
