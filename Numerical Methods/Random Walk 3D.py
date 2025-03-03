from numpy.random import seed, rand 
from random import choice
from datetime import datetime, date, time
import math
N=int(input("Adim sayisini giriniz: "))
xilk=0
yilk=0
zilk=0
xson=0
yson=0
zson=0
R=0
random=rand(N)
for i in range(N):
    datetime=datetime.now()
    seed(datetime.microsecond%1000)
    random=rand()
    if random<0.17:
        xson=xson-1
    elif random<0.34:
        xson=xson+1
    elif random<0.51:
        yson=yson-1
    elif random<0.68:
        yson=yson+1
    elif random<0.85:
        zson=zson-1
    else:
        zson=zson+1
    R=math.sqrt(pow((xson-xilk),2)+pow((yson-yilk),2)+pow((zson-zilk),2))
    print("Adim sayisi: ",int(i))
    print("Orjine olan uzaklik: ",int(R))
    print(50*"-")
print("Bulunulan son nokta: ")
print("x: ", xson)
print("y: ", yson)
print("z: ", zson)