from tkinter import *
from functools import partial

fen=Tk()
fen.title('Curve drawer')
fen['bg']='bisque'

can=Canvas(height=500,width=500,bg="white")
can.grid(row=0,column=0)

Framesettings = Frame(bg='grey')
Framesettings.grid(row=0,column=1)

Ajoutpoint=LabelFrame(Framesettings,text="Ajouter un nouveau point", padx=5)
Ajoutpoint.grid(row=0)

ajouteX = Label(Ajoutpoint, text = 'X=', fg = 'black', justify='center', padx=5, pady=5)
ajouteX.grid(row=0,column=0)

EntreeX = Entry(Ajoutpoint)
EntreeX.grid(row=0,column=1)

ajouteY = Label(Ajoutpoint, text = 'Y=', fg = 'black', justify='center', padx=5, pady=5)
ajouteY.grid(row=1,column=0)

EntreeY = Entry(Ajoutpoint)
EntreeY.grid(row=1,column=1)

Valider=Button(Ajoutpoint, text = 'Valider!')
Valider.grid(row=2,column=1)


fen.mainloop()
