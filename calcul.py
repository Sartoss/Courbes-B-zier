from math import sqrt

def fBezier(liste):
	if sqrt((liste[0][0]-liste[-1][0])**2+(liste[0][1]-liste[-1][1])**2)<=2:
		return(liste[0][0],liste[0][1])
	l1=liste.copy()
	l2=liste.copy()
	n=len(liste)
	for i in range(n-1):
		for j in range(i+1):
			l1[n+j-i-1]=((l1[n+j-i-2][0]+l1[n+j-i-1][0])/2,(l1[n+j-i-2][1]+l1[n+j-i-1][1])/2)
			l2[i-j]=((l2[i-j][0]+l2[i-j+1][0])/2,(l2[i-j][1]+l2[i-j+1][1])/2)
	return(fBezier(l1)+fBezier(l2))

def fSpline(liste):
	if len(liste)==2:
		return(liste[0][0],liste[0][1],liste[1][0],liste[1][1])
	points=[]
	if varTangente.get()==1 and CurvType.get()==1:
		for i in range(-varBoucle.get(),len(liste)-1):
			tax=liste[i][4]
			tay=liste[i][5]
			tbx=-liste[i+1][2]
			tby=-liste[i+1][3]
			a1=2*liste[i][0]-2*liste[i+1][0]+tax+tbx
			b1=-3*liste[i][0]+3*liste[i+1][0]-2*tax-tbx
			a2=2*liste[i][1]-2*liste[i+1][1]+tay+tby
			b2=-3*liste[i][1]+3*liste[i+1][1]-2*tay-tby
			t=0
			while t<1:
				points.append(a1*t**3+b1*t**2+tax*t+liste[i][0])
				points.append(a2*t**3+b2*t**2+tay*t+liste[i][1])
				t+=0.01
	else:
		if varBoucle.get()==1:
			for i in range(-2,len(liste)-2):
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
		else:
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

def fBspline(liste):
	n=degree.get()
	m=len(liste)+n
	nd=[i.get() for i in noeud]
	points=[]
	t=nd[n]
	while t<=nd[m-n]:
		x=0
		y=0
		for i in range(m-n):
			a=Bspline(i,n,t,nd)
			x+=a*liste[i][0]
			y+=a*liste[i][1]
		points.append(x)
		points.append(y)
		t+=0.01
	return(tuple(points))

def Bspline(j,n,t,noeud):
	if n==0:
		if noeud[j]<=t<noeud[j+1]:
			return(1)
		else:
			return(0)
	else:
		if noeud[j+n]==noeud[j]:
			a=0
		else:
			a=(t-noeud[j])*Bspline(j,n-1,t,noeud)/(noeud[j+n]-noeud[j])
		if noeud[j+n+1]==noeud[j+1]:
			c=0
		else:
			c=(noeud[j+n+1]-t)*Bspline(j+1,n-1,t,noeud)/(noeud[j+n+1]-noeud[j+1])
		return(a+c)
