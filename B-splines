# -*- coding: utf-8 -*-
"""
Created on Thu May 11 11:12:56 2017

@author: lemeurquen
"""
from tkinter import *
from time import time

def S(noeud,points,m,n):
    liste=[]
    t=0
    while t<=1:
        x=0
        y=0
        for i in range(m-n):
            #print("n")
            a=b(i,n,t,noeud)
            x+=a*points[i][0]
            y+=a*points[i][1]
        liste.append(x+130)
        liste.append(700-(y+130))
        t+=0.001
    #print(liste)
    return(liste)

def b(j,n,t,noeud):
    if j==6:print(j)
    if n==0:
        if noeud[j]<=t<noeud[j+1]:
            return(1)
        else:
            return(0)
    else:
        '''if noeud[j+n]==noeud[j]:
            a=0
        else:
            a=(t-noeud[j])*b(j,n-1,t,noeud)/(noeud[j+n]-noeud[j])
        if noeud[j+n+1]==noeud[j+1]:
            c=0
        else:
            c=(noeud[j+n+1]-t)*b(j+1,n-1,t,noeud)/(noeud[j+n+1]-noeud[j+1])
        return(a+c)'''
        return(w(t,j,n,noeud)*b(j,n-1,t,noeud)+(1-w(t,j+1,n,noeud))*b(j+1,n-1,t,noeud))

def w(t,i,k,noeud):
    if noeud[i]<noeud[i+k]:
        return((t-noeud[i])/(noeud[i+k]-noeud[i]))
    else:
        return(0)

fen=Tk()
can=Canvas(fen,height=700,width=700,bg='#ffffff')
can.pack()
m=7
n=3
points=[(-100,-100),(-50,100),(50,-100),(100,100)]
noeud=[0,0,0,0,0.501,1,1,1]

can.create_line(S(noeud,points,m,n))
ti=time()
can.coords(1,tuple(S(noeud,points,m,n)))
print(time()-ti)
for i in points:
    can.create_oval(i[0]-5,i[1]-5,i[0]+5,i[1]+5)
fen.mainloop()
