from random import randint
from time import time

def easterEgg():
    global lstEE
    global regles
    global temps
    if messagebox.askquestion("Easter egg", "En continuant, vous acceptez de nous donnez 20/20 pour ce projet :)\nContinuer ?")=="no":
        return()
    can.unbind("<ButtonPress-1>")
    can.unbind("<ButtonRelease-1>")
    can.unbind("<B1-Motion>")
    can.unbind("<ButtonPress-3>")
    can.bind("<Motion>",deplacementEasterEgg)
    fen.bind("<Escape>",quitter)
    Framesettings.grid_forget()
    fen.attributes("-fullscreen",1)
    fen.update()
    regles=Label(fen, text='Evitez les points !', fg = 'red', justify='center', padx=5, pady=5)
    regles.grid(row=1,column=0)
    lstEE=[[indic[i][0],[[randint(0,can.winfo_width()),randint(0,can.winfo_height())] for j in range(4)]] for i in range(len(liste))]
    for i in range(len(liste)):
        lstEE[i][1][1][0]=liste[i][0].get()
        lstEE[i][1][1][1]=liste[i][1].get()
    for i in lstEE:
        tax=i[1][2][0]-i[1][0][0]
        tay=i[1][2][1]-i[1][0][1]
        tbx=i[1][3][0]-i[1][1][0]
        tby=i[1][3][1]-i[1][1][1]
        i.append([2*i[1][1][0]-2*i[1][2][0]+tax+tbx,-3*i[1][1][0]+3*i[1][2][0]-2*tax-tbx,tax,i[1][1][0]])
        i.append([2*i[1][1][1]-2*i[1][2][1]+tax+tbx,-3*i[1][1][1]+3*i[1][2][1]-2*tax-tbx,tax,i[1][1][1]])
        i.append(0)
    temps=time()
    prog[0]=fen.after(30,update)
    prog[1]=fen.after(5000,ajouter)

def deplacementEasterEgg(event):
    global coordX
    global coordY
    coordX=event.x
    coordY=event.y

def update():
    global coordX
    global coordY
    global temps
    prog[0]=fen.after(30,update)
    for i in lstEE:
        if i[4]>=1:
            del(i[1][0])
            i[1].append([randint(0,can.winfo_width()),randint(0,can.winfo_height())])
            tax=i[1][2][0]-i[1][0][0]
            tay=i[1][2][1]-i[1][0][1]
            tbx=i[1][3][0]-i[1][1][0]
            tby=i[1][3][1]-i[1][1][1]
            i[2]=[2*i[1][1][0]-2*i[1][2][0]+tax+tbx,-3*i[1][1][0]+3*i[1][2][0]-2*tax-tbx,tax,i[1][1][0]]
            i[3]=[2*i[1][1][1]-2*i[1][2][1]+tax+tbx,-3*i[1][1][1]+3*i[1][2][1]-2*tax-tbx,tax,i[1][1][1]]
            i[4]=0
        i[4]+=0.03
        x=i[2][0]*i[4]**3+i[2][1]*i[4]**2+i[2][2]*i[4]+i[2][3]
        y=i[3][0]*i[4]**3+i[3][1]*i[4]**2+i[3][2]*i[4]+i[3][3]
        can.coords(i[0],x-rayon,y-rayon,x+rayon,y+rayon)
        if (x-coordX)**2+(y-coordY)**2<=rayon**2:
            temps=int(time()-temps)
            quitter(None)
            messagebox.showinfo("Fin","Vous avez perdu en touchant un point au bout de :\n"+str(temps//60)+"m"+str(temps%60)+"s")
            break

def ajouter():
    prog[1]=fen.after(5000,ajouter)
    p=lstEE[randint(0,len(lstEE)-1)]
    lstEE.append([can.create_oval(-1,-1,-1,-1,fill="yellow",outline="red",width=2),[[i[0],i[1]] for i in p[1]],p[2][:],p[3][:],p[4]])

def quitter(event):
    fen.after_cancel(prog[0])
    fen.after_cancel(prog[1])
    fen.attributes("-fullscreen",0)
    can.unbind("<Motion>")
    fen.unbind("<Escape>")
    can.bind("<ButtonPress-1>",clique)
    can.bind("<ButtonRelease-1>",relache)
    can.bind("<B1-Motion>",deplacement)
    can.bind("<ButtonPress-3>",clicdrt)
    Framesettings.grid(row=0,column=1,sticky='nsew',pady=5,padx=5)
    regles.grid_forget()
    for i in range(len(liste)):
        can.coords(indic[i][0],liste[i][0].get()-rayon,liste[i][1].get()-rayon,liste[i][0].get()+rayon,liste[i][1].get()+rayon)
    for i in range(len(liste),len(lstEE)):
        can.delete(lstEE[i][0])

global coordX
global coordY
global regles
global temps

lstEE=[]
prog=[0,0]
coordX=0
coordY=0