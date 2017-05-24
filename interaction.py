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
	x=event.x
	y=event.y
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
