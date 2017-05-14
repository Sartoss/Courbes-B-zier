from tkinter import *

def f(liste):
	points=[]
	for i in range(len(liste)-1):
		if i==0:
			tx=liste[i+2][0]-liste[i][0]
			ty=liste[i+2][1]-liste[i][1]
			a1=liste[i][0]/2-liste[i+1][0]/2+tx/2
			c1=-3*liste[i][0]/2+3*liste[i+1][0]/2-tx/2
			a2=liste[i][1]/2-liste[i+1][1]/2+ty/2
			c2=-3*liste[i][1]/2+3*liste[i+1][1]/2-ty/2
			t=0
			while t<1:
				points.append(a1*t**3+c1*t+liste[i][0])
				points.append(a2*t**3+c2*t+liste[i][1])
				t+=0.01
		elif i==len(liste)-2:
			tx=liste[i+1][0]-liste[i-1][0]
			ty=liste[i+1][1]-liste[i-1][1]
			a1=liste[i][0]/2-liste[i+1][0]/2+tx/2
			b1=-3*liste[i][0]/2+3*liste[i+1][0]/2-3*tx/2
			a2=liste[i][1]/2-liste[i+1][1]/2+ty/2
			b2=-3*liste[i][1]/2+3*liste[i+1][1]/2-3*ty/2
			t=0
			while t<1:
				points.append(a1*t**3+b1*t**2+tx*t+liste[i][0])
				points.append(a2*t**3+b2*t**2+ty*t+liste[i][1])
				t+=0.01
		else:
			tax=liste[i+1][0]-liste[i-1][0]
			tay=liste[i+1][1]-liste[i-1][1]
			tbx=liste[i+2][0]-liste[i][0]
			tby=liste[i+2][1]-liste[i][1]
			a1=2*liste[i][0]-2*liste[i+1][0]+tax+tbx
			b1=-3*liste[i][0]+3*liste[i+1][0]-2*tax-tbx
			a2=2*liste[i][1]-2*liste[i+1][1]+tay+tby
			b2=-3*liste[i][1]+3*liste[i+1][1]-2*tay-tby
			t=0
			while t<1:
				points.append(a1*t**3+b1*t**2+tax*t+liste[i][0])
				points.append(a2*t**3+b2*t**2+tay*t+liste[i][1])
				t+=0.01
	points.append(liste[-1][0])
	points.append(liste[-1][1])
	return(tuple(points))

liste=[(10,10),(100,200),(200,100),(300,250),(400,200)]

fen=Tk()
can=Canvas(fen,height=500,width=500)
can.pack()
for i in liste:
	can.create_oval(i[0]-5,i[1]-5,i[0]+5,i[1]+5)
can.create_line(f(liste))

fen.mainloop()
