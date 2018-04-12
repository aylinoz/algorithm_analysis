import math

def ic_carpim(a,b):
    print "ic carpim:",(a[0]*b[0]+a[1]*b[1]+a[2]*b[2])

def dis_carpim(a,b):
    qwe=[]
    qwe.append(a[1]*b[2]-a[2]*b[1])
    qwe.append(a[2]*b[0]-a[0]*b[2])
    qwe.append(a[0]*b[1]-a[1]*b[0])
    print "dis_carpim:",qwe

def cross_uzunlugu(a,b):
    qwe=[]
    qwe.append(a[1]*b[2]-a[2]*b[1])
    qwe.append(a[2]*b[0]-a[0]*b[2])
    qwe.append(a[0]*b[1]-a[1]*b[0])
    print "cross vektörün uzunlugu:",math.sqrt((qwe[0]**2)+(qwe[1]**2)+(qwe[2]**2))

def ucgen_alani(a,b):
    qwe=[]
    qwe.append(a[1]*b[2]-a[2]*b[1])
    qwe.append(a[2]*b[0]-a[0]*b[2])
    qwe.append(a[0]*b[1]-a[1]*b[0])
    k1=math.sqrt((a[0]**2)+(a[1]**2)+(a[2]**2))
    k2=math.sqrt((b[0]**2)+(b[1]**2)+(b[2]**2))
    k3=math.sqrt((qwe[0]**2)+(qwe[1]**2)+(qwe[2]**2))
    c=(k1+k2+k3)/2
    print "olusan ucgenin alani:",math.sqrt(c*(c-k1)*(c-k2)*(c-k3))

def determinant(a,b):
    qwe=[]
    qwe.append(a[1]*b[2]-a[2]*b[1])
    qwe.append(a[2]*b[0]-a[0]*b[2])
    qwe.append(a[0]*b[1]-a[1]*b[0])
    n1=(a[0]*b[1])-(b[0]*a[1])
    n2=(a[0]*b[2])-(b[0]*a[2])
    n3=(a[0]*qwe[1])-(a[1]*qwe[0])
    n4=(a[0]*qwe[2])-(qwe[0]*a[2])
    print "vektörlerin oluþturduðu matrisin determinantý:",((n1*n4)-(n2*n3))/a[0]
    

a1=[]
a2=[]
x = raw_input("Virgül ile ayirarak ilk vektörün katsayilarini giriniz: ")
y = raw_input("Virgül ile ayirarak ikinci vektörün katsayilarini giriniz: ")
a,b,c=x.split(",")
a1.append(int(a))
a1.append(int(b))
a1.append(int(c))
a,b,c=y.split(",")
a2.append(int(a))
a2.append(int(b))
a2.append(int(c))
ic_carpim(a1,a2)
dis_carpim(a1,a2)
cross_uzunlugu(a1,a2)
ucgen_alani(a1,a2)
determinant(a1,a2)
