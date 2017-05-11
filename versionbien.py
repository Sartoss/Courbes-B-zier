from tkinter import *
from tkinter.ttk import Combobox
from math import sqrt,factorial as fact

def f(t,liste):
    n=len(liste)
    return(sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][0].get() for i in range(n)),sum(liste[i][2]*(t**i)*((1-t)**(n-i-1))*liste[i][1].get() for i in range(n)))

def affiche(liste,pas,coeff):
    p=f(0,liste)
    points=p[0]*coeff,p[1]*coeff
    t=pas
    while t<=1:
        p2=f(t,liste)
        p=p2
        points+=p[0]*coeff,p[1]*coeff
        t+=pas
    points+=liste[-1][0].get()*100,liste[-1][1].get()*100
    can.coords(1,points)

def clique(event):
    x=event.x
    y=event.y
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()*100-x)**2+(liste[i][1].get()*100-y)**2)<=10:
            global select
            select.set(indic[i])
            break
def relache(event):
    global select
    select.set(0)
    
def deplacement(event):
    if select.get()==0:return
    x=event.x
    y=event.y
    lab.config(text="x,y="+str(x)+" , "+str(y)+" "+str(select.get()))
    liste[indic.index(select.get())][0].set(x/100)
    liste[indic.index(select.get())][1].set(y/100)
    can.coords(select.get(),x-10,y-10,x+10,y+10)
    affiche(liste,0.01,100)

    
def nvpts():
    indic.append(can.create_oval(240,240,260,260))
    can.itemconfig(indic[-1],fill="yellow",outline="red",width=2)
    liste.append((DoubleVar(),DoubleVar()))
    liste[-1][0].set(2.50)
    liste[-1][1].set(2.50)

    for i in range(len(liste)):
        liste[i]=(liste[i][0],liste[i][1],fact(len(liste)-1)//(fact(i)*fact(len(liste)-i-1)))
    affiche(liste,0.01,100)
    
    lstpts.append(Label(ssf,text="Point "+str(len(liste))+" : x="))
    lstpts[-1].grid(row=len(liste),column=1)
    
    lstpts.append(Entry(ssf,textvariable=liste[-1][0],width=5))
    lstpts[-1].grid(row=len(liste),column=2)
    
    lstpts.append(Label(ssf,text=" y="))
    lstpts[-1].grid(row=len(liste),column=3)
    
    lstpts.append(Entry(ssf,textvariable=liste[-1][1],width=5))
    lstpts[-1].grid(row=len(liste),column=4)

    lstpts.append(Button(ssf,text="X",command=lambda:supprime(len(liste))))
    lstpts[-1].grid(row=len(liste),column=5)

def supprime(n):
    print(n)
    del(liste[n-1])
    for i in range(len(liste)):
        liste[i]=(liste[i][0],liste[i][1],fact(len(liste)-1)//(fact(i)*fact(len(liste)-i-1)))
    can.delete(indic[n-1])
    del(indic[n-1])
    for i in range(5):
        lstpts[5*n-5].destroy()
        del(lstpts[5*(n-1)])
    affiche(liste,0.01,coeff)
    
        

fen=Tk()
fen.config(bg="bisque")
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

liste=[]
for i in range(4):
    liste.append((DoubleVar(),DoubleVar()))
liste[0][0].set(1)
liste[0][1].set(0)
liste[1][0].set(2)
liste[1][1].set(5)
liste[2][0].set(3)
liste[2][1].set(2.5)
liste[3][0].set(5)
liste[3][1].set(1)

indic=[2,3,4,5]
liste=[(liste[i][0],liste[i][1],fact(len(liste)-1)//(fact(i)*fact(len(liste)-i-1))) for i in range(len(liste))]

lstpts=[]
ssf=Frame(sf)
ssf.pack()

for i in range(1,len(liste)+1):
    lstpts.append(Label(ssf,text="Point "+str(i)+" : x="))
    lstpts[-1].grid(row=i,column=1)
    
    lstpts.append(Entry(ssf,textvariable=liste[i-1][0],width=5))
    lstpts[-1].grid(row=i,column=2)
    
    lstpts.append(Label(ssf,text=" y="))
    lstpts[-1].grid(row=i,column=3)
    
    lstpts.append(Entry(ssf,textvariable=liste[i-1][1],width=5))
    lstpts[-1].grid(row=i,column=4)

    lstpts.append(Button(ssf,text="X",command=lambda:supprime(i  )))
    lstpts[-1].grid(row=i,column=5)

coeff=100#IntVar()
#coeff.set(100)
pas=t=0.01
p=f(0,liste)


points=p[0]*100,p[1]*100
while t<=1:
        p2=f(t,liste)
        p=p2
        points+=p[0]*100,p[1]*100
        t+=pas
can.create_line(points,fill="blue",width=2)

for i in liste:
    can.create_oval(i[0].get()*coeff-rayon,i[1].get()*coeff-rayon,i[0].get()*coeff+rayon,i[1].get()*coeff+rayon)
    can.itemconfig(liste.index(i)+2,fill="yellow",outline="red",width=2)

select=IntVar()
select.set(0)

can.bind("<ButtonPress-1>",clique)
can.bind("<ButtonRelease-1>",relache)
can.bind("<B1-Motion>",deplacement)

fen.mainloop()
