import matplotlib.pyplot as plt
import numpy as np
h=float(input("Adim araligini giriniz: "))
x=0.0
y=1.0
xlist=[0.0]
ylist=[1.0]
def f(x,y):
    return float((y*pow(x,2))-(1.2*y))
print("Numerik cozumlerden elde edilen y degerleri asagidaki gibidir: ")
print(50*"-")
print("y degerleri")
print(50*"-")
while x<2.0:
    k1=f(x,y)
    k2=f((x+(h/2)),(y+(1/2*k1*h)))
    k3=f((x+(h/2)),(y+(1/2*k2*h)))
    k4=f(x+h,(y+k3*h))
    y=y+(1/6*(k1+2*k2+2*k3+k4)*h)
    print(y)
    print(50*"-")
    x=x+h
    ylist.append(y)
    xlist.append(x)
plt.xlabel('x degerleri')
plt.ylabel('y degerleri')
plt.title('h=0.5 adim araligi icin Runge-Kutta grafik karsilastirmasi')
x1=np.array(xlist)
y1=np.array(ylist)
plt.plot(x1,y1,'ro',label="Numerik Cozum")
x2=np.linspace(0,2)
y2=np.exp((pow(x2,3)/3)-(1.2*x2))
plt.plot(x2,y2,'b',label="Analitik Cozum")
plt.legend(loc='upper left')
plt.show()