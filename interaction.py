def clique(event):
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
    print(select[0].get(),select[1].get())
def relache(event):
    global select
    select[0].set(-1)
    select[1].set(-1)
    
def deplacement(event):
    global select
    if select[0].get()==-1:return
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
        liste[m][2*n].set(x-liste[m][0].get())
        liste[m][2*n+1].set(y-liste[m][1].get())
        b=convp(liste[m][0].get()+liste[m][2*n].get(),liste[m][1].get()+liste[m][2*n+1].get())
        can.coords(indic[m][n],x-rayonTan,y-rayonTan,x+rayonTan,y+rayonTan)
        can.coords(indic[m][n+2],a[0],a[1],b[0],b[1])
    if varTangente.get()==1 and n==0:
        b=convp(liste[m][2].get(),liste[m][3].get())
        c=convp(liste[m][4].get(),liste[m][5].get())
        can.coords(indic[m][1],x+b[0]-rayonTan,y+b[1]-rayonTan,x+b[0]+rayonTan,y+b[1]+rayonTan)
        can.coords(indic[m][2],x+c[0]-rayonTan,y+c[1]-rayonTan,x+c[0]+rayonTan,y+c[1]+rayonTan)
        can.coords(indic[m][3],a[0],a[1],a[0]+b[0],a[1]+b[1])
        can.coords(indic[m][4],a[0],a[1],a[0]+c[0],a[1]+c[1])
    affiche(liste)

def clicdrt(event):
    x.set(event.x)
    y.set(event.y)
    if []!=menu:
        menu[0].destroy()
        del(menu[0])
    menu.append(Menu(can,tearoff=0))
    menu[0].add_command(label="Ajouter un point",command=partial(nvpts,x,y))
    for i in range(len(liste)):
        if sqrt((liste[i][0].get()-x.get())**2+(liste[i][1].get()-y.get())**2)<=10:
            menu[0].add_command(label="Supprimer le point "+str(i+1),command=partial(supprime,indic[i][0]))
    menu[0].post(event.x_root,event.y_root)
