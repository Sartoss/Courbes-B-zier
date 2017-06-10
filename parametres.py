def nvpts(x,y):
    global rayon
    X=x.get()
    Y=y.get()
    x,y=convp(X,Y)
    if X==Y==42:
        easterEgg()
        return()
    if CurvType.get()==0:
        degree.set(len(liste))
    indic.append([can.create_oval(x-rayon,y-rayon,x+rayon,y+rayon,fill="yellow",outline="red",width=2),-1,-1,-1,-1])
    if varTangente.get()==1 and CurvType.get()==1:
        indic[-1][1]=can.create_oval(x-50-rayonTan,y-rayonTan,x-50+rayonTan,y+rayonTan)
        indic[-1][2]=can.create_oval(x+50-rayonTan,y-rayonTan,x+50+rayonTan,y+rayonTan)
        indic[-1][3]=can.create_line(x,y,x-50,y)
        indic[-1][4]=can.create_line(x,y,x+50,y)
    liste.append((DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar(),DoubleVar()))
    liste[-1][0].set(X)
    liste[-1][1].set(Y)
    liste[-1][2].set(-1)
    liste[-1][3].set(0)
    liste[-1][4].set(1)
    liste[-1][5].set(0)
    liste[-1][6].set(1)
    
    n=len(liste)-1
    
    lstpts.append([])
    lstpts[-1].append(Label(ListePoints,text="Point "+str(n+1)+" : x="))
    lstpts[-1][-1].grid(row=n,column=0)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[-1][0],width=5))
    lstpts[-1][-1].grid(row=n,column=1)
    lstpts[-1][-1].bind("<Return>",valider)
    
    lstpts[-1].append(Label(ListePoints,text=" y="))
    lstpts[-1][-1].grid(row=n,column=2)
    
    lstpts[-1].append(Entry(ListePoints,textvariable=liste[-1][1],width=5))
    lstpts[-1][-1].grid(row=n,column=3)
    lstpts[-1][-1].bind("<Return>",valider)

    lstpts[-1].append(Button(ListePoints,text="X",command=partial(supprime,indic[-1][0])))
    lstpts[-1][-1].grid(row=n,column=4)
    
    lstpts[-1].append(Label(ListePoids,text="poids="))
    lstpts[-1][-1].grid(row=n,column=0)
    
    lstpts[-1].append(Entry(ListePoids,textvariable=liste[-1][6],width=5))
    lstpts[-1][-1].grid(row=n,column=1,pady=4)
    lstpts[-1][-1].bind("<Return>",valider)
    
    noeud.append(DoubleVar())
    d=len(noeud)-len(liste)-1
    for i in range(d+1):
        noeud[i].set(0)
    n=len(noeud)-2*d-2
    for i in range(n):
        noeud[i+d+1].set((i+1)/(n+1))
    for i in range(d+1):
        noeud[i+d+n+1].set(1)
    
    n=len(noeud)-1
    
    lstnoeuds.append([])
    
    lstnoeuds[-1].append(Label(ListeNoeuds,text="Noeud "+str(n+1)+" :"))
    lstnoeuds[-1][-1].grid(row=n,column=0)
    
    lstnoeuds[-1].append(Entry(ListeNoeuds,textvariable=noeud[-1],width=15))
    lstnoeuds[-1][-1].grid(row=n,column=1)
    lstnoeuds[-1][-1].bind("<Return>",valider)
    
    affiche(liste)

def supprime(n):
    if len(liste)>2:
        for i in range(len(indic)):
            if indic[i][0]==n:
                m=i
                break
        del(liste[m])
        can.delete(indic[m][0])
        if indic[m][1]!=-1:
            can.delete(indic[m][1])
            can.delete(indic[m][2])
            can.delete(indic[m][3])
            can.delete(indic[m][4])
        del(indic[m])
        for i in range(6,-1,-1):
            lstpts[m][i].destroy()
        del(lstpts[m])
        for i in range(1,-1,-1):
            lstnoeuds[-1][i].destroy()
        del(lstnoeuds[-1])
        del(noeud[-1])
        if len(liste)==degree.get():
            degree.set(len(liste)-1)
            for i in range(1,-1,-1):
                lstnoeuds[-1][i].destroy()
            del(lstnoeuds[-1])
            del(noeud[-1])
        d=len(noeud)-len(liste)-1
        for i in range(d+1):
            noeud[i].set(0)
        n=len(noeud)-2*d-2
        for i in range(n):
            noeud[i+d+1].set((i+1)/(n+1))
        for i in range(d+1):
            noeud[i+d+n+1].set(1)
        for i in range(m,len(liste)):
            for j in range(5):
                lstpts[i][j].grid_forget()
                lstpts[i][j].grid(row=i,column=j)
            for j in range(2):
                lstpts[i][j+5].grid_forget()
                lstpts[i][j+5].grid(row=i,column=j,pady=4)
            lstpts[i][0].config(text="Point "+str(i+1)+" : x=")
        if CurvType.get()==0:
            degree.set(len(liste)-1)
        affiche(liste)
    else:
        messagebox.showerror("Erreur","Il ne peut pas y avoir moins de deux points")

def changeType():
    FrameSpline.grid_forget()
    FrameBSpline.grid_forget()
    ListePoids.grid_forget()
    if CurvType.get()==0:
        Entrydegre["state"]="disabled"
        degree.set(len(liste)-1)
    elif CurvType.get()==1:
        FrameSpline.grid(row=6)
        Entrydegre["state"]="disabled"
        degree.set(3)
    elif CurvType.get()==2:
        FrameBSpline.grid(row=6)
        Entrydegre["state"]="normal"
        degree.set(len(noeud)-len(liste)-1)
    elif CurvType.get()==3:
        FrameBSpline.grid(row=6,columnspan=2)
        ListePoids.grid(row=1,column=1)
        Entrydegre["state"]="normal"
        degree.set(len(noeud)-len(liste)-1)
    if varTangente.get()==1 and CurvType.get()==1 and indic[0][1]==-1:
        for i in range(len(liste)):
            a=convp(liste[i][0].get(),liste[i][1].get())
            b=convp(liste[i][0].get()+liste[i][2].get(),liste[i][1].get()+liste[i][3].get())
            c=convp(liste[i][0].get()+liste[i][4].get(),liste[i][1].get()+liste[i][5].get())
            indic[i][1]=can.create_oval(b[0]-rayonTan,b[1]-rayonTan,b[0]+rayonTan,b[1]+rayonTan)
            indic[i][2]=can.create_oval(c[0]-rayonTan,c[1]-rayonTan,c[0]+rayonTan,c[1]+rayonTan)
            indic[i][3]=can.create_line(a[0],a[1],b[0],b[1])
            indic[i][4]=can.create_line(a[0],a[1],c[0],c[1])
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

def valider(event):
    for i in range(len(liste)):
        a=convp(liste[i][0].get(),liste[i][1].get())
        can.coords(indic[i][0],a[0]-rayon,a[1]-rayon,a[0]+rayon,a[1]+rayon)
        if varTangente.get()==1 and CurvType.get()==1:
            b=convp(liste[i][0].get()+liste[i][2].get(),liste[i][1].get()+liste[i][3].get())
            c=convp(liste[i][0].get()+liste[i][4].get(),liste[i][1].get()+liste[i][5].get())
            can.coords(indic[i][1],b[0]-rayonTan,b[1]-rayonTan,b[0]+rayonTan,b[1]+rayonTan)
            can.coords(indic[i][2],c[0]-rayonTan,c[1]-rayonTan,c[0]+rayonTan,c[1]+rayonTan)
            can.coords(indic[i][3],a[0],a[1],b[0],b[1])
            can.coords(indic[i][4],a[0],a[1],c[0],c[1])
    rep=convp(0,0)
    a=convp(1,0)
    b=convp(0,1)
    can.coords(2,rep[0],rep[1],a[0],a[1])
    can.coords(3,rep[0],rep[1],b[0],b[1])
    affiche(liste)

def changeDegree(event):
    if len(liste)<=degree.get():
        messagebox.showerror("Erreur","Le degree doit etre strictement inferieur au nombre de points")
    else:
        m=len(liste)+degree.get()+1
        while len(noeud)<m:
            noeud.append(DoubleVar())
            
            n=len(noeud)-1
            
            lstnoeuds.append([])
            
            lstnoeuds[-1].append(Label(ListeNoeuds,text="Noeud "+str(n+1)+" :"))
            lstnoeuds[-1][-1].grid(row=n,column=0)
            
            lstnoeuds[-1].append(Entry(ListeNoeuds,textvariable=noeud[-1],width=15))
            lstnoeuds[-1][-1].grid(row=n,column=1)
            lstnoeuds[-1][-1].bind("<Return>",valider)
        while len(noeud)>m:
            for i in range(1,-1,-1):
                lstnoeuds[-1][i].destroy()
            del(lstnoeuds[-1])
            del(noeud[-1])
        d=len(noeud)-len(liste)-1
        for i in range(d+1):
            noeud[i].set(0)
        n=len(noeud)-2*d-2
        for i in range(n):
            noeud[i+d+1].set((i+1)/(n+1))
        for i in range(d+1):
            noeud[i+d+n+1].set(1)
        affiche(liste)
