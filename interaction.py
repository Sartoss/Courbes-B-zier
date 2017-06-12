def clique(event):
    """
    Fonction qui gere le clic gauche
    """
    global select
    x=event.x
    y=event.y
    X,Y=convr(x,y)
    while []!=menu:
        menu[0].destroy()
        del(menu[0])
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()-X)**2+(liste[i][1].get()-Y)**2)<=rayon/zoom.get():
            select[0].set(i)
            select[1].set(0)
            break
        elif sqrt((liste[i][0].get()+liste[i][2].get()-X)**2+(liste[i][1].get()+liste[i][3].get()-Y)**2)<=rayonTan/zoom.get():
            select[0].set(i)
            select[1].set(1)
            break
        elif sqrt((liste[i][0].get()+liste[i][4].get()-X)**2+(liste[i][1].get()+liste[i][5].get()-Y)**2)<=rayonTan/zoom.get():
            select[0].set(i)
            select[1].set(2)
            break
    if select[0].get()==-1:
        select[0].set(-2)
        if transRot.get()==0:
            select[2].set(xrep.get()-x)
            select[3].set(yrep.get()-y)
        else:
            select[2].set(ang.get()-atan2((yrep.get()-y)/zoom.get(),(x-xrep.get())/zoom.get()))

def relache(event):
    global select
    select[0].set(-1)
    
def deplacement(event):
    """
    Fonction qui gere le déplacement des items sur le canvas
    """
    global select
    if select[0].get()==-1:
        return
    if select[0].get()==-2:
        if transRot.get()==0:
            xrep.set(event.x+select[2].get())
            yrep.set(event.y+select[3].get())
        else:
            ang.set(atan2((yrep.get()-event.y)/zoom.get(),(event.x-xrep.get())/zoom.get())+select[2].get())
        valider(None)
        return
    x=event.x
    y=event.y
    X,Y=convr(x,y)
    m=select[0].get()
    n=select[1].get()
    a=convp(liste[m][0].get(),liste[m][1].get())
    if n==0:
        liste[m][0].set(X)
        liste[m][1].set(Y)
        can.coords(indic[m][0],x-rayon,y-rayon,x+rayon,y+rayon)
    else:
        liste[m][2*n].set(X-liste[m][0].get())
        liste[m][2*n+1].set(Y-liste[m][1].get())
        b=convp(liste[m][0].get()+liste[m][2*n].get(),liste[m][1].get()+liste[m][2*n+1].get())
        can.coords(indic[m][n],x-rayonTan,y-rayonTan,x+rayonTan,y+rayonTan)
        can.coords(indic[m][n+2],a[0],a[1],b[0],b[1])
    if varTangente.get()==1 and n==0:
        b=convp(liste[m][0].get()+liste[m][2].get(),liste[m][1].get()+liste[m][3].get())
        c=convp(liste[m][0].get()+liste[m][4].get(),liste[m][1].get()+liste[m][5].get())
        can.coords(indic[m][1],b[0]-rayonTan,b[1]-rayonTan,b[0]+rayonTan,b[1]+rayonTan)
        can.coords(indic[m][2],c[0]-rayonTan,c[1]-rayonTan,c[0]+rayonTan,c[1]+rayonTan)
        can.coords(indic[m][3],a[0],a[1],b[0],b[1])
        can.coords(indic[m][4],a[0],a[1],c[0],c[1])
    affiche(liste)

def clicdrt(event):
    """
    Fonction qui gere le clic droit
    """
    X,Y=convr(event.x,event.y)
    x.set(X)
    y.set(Y)
    if []!=menu:
        menu[0].destroy()
        del(menu[0])
    menu.append(Menu(can,tearoff=0))
    menu[0].add_command(label="Ajouter un point",command=partial(nvpts,x,y))
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()-X)**2+(liste[i][1].get()-Y)**2)<=rayon/zoom.get():
            menu[0].add_command(label="Supprimer le point "+str(i+1),command=partial(supprime,indic[i][0]))
    menu[0].post(event.x_root,event.y_root)

def molette(os,event):
    """
    Fonction qui gere la molette selon l'OS
    """
    a=convr(event.x,event.y)
    if system()=="Windows":
        zoom.set(zoom.get()*1.1**(event.delta//120))
    elif system()=="Linux":
        if os=="Lu":
            zoom.set(zoom.get()*1.1)
        else:
            zoom.set(zoom.get()/1.1)
    a=convp(a[0],a[1])
    xrep.set(xrep.get()+event.x-a[0])
    yrep.set(yrep.get()+event.y-a[1])
    valider(None)

def clavier(event):
    """
    Fonction qui gere les translations par le clavier
    """
    t=event.keysym
    if t=="Up":
        yrep.set(yrep.get()-10)
    elif t=="Right":
        xrep.set(xrep.get()+10)
    elif t=="Down":
        yrep.set(yrep.get()+10)
    elif t=="Left":
        xrep.set(xrep.get()-10)
    else:
        return
    valider(None)
