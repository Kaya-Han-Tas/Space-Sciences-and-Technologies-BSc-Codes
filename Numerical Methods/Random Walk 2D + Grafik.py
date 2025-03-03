import matplotlib.pyplot as plt
import numpy as np
from numpy.random import seed, rand 
from random import choice
from datetime import datetime, date, time
import math
N=int(input("Adim sayisini giriniz: "))
xilk=0
yilk=0
xson=0
yson=0
R=0
Rlist=[0]
sqrtNlist=[0]
random=rand(N)
for i in range(N):
    datetime=datetime.now()
    seed(datetime.microsecond%1000)
    random=rand()
    if random<0.25:
        xson=xson-1
    elif random<0.5:
        xson=xson+1
    elif random<0.75:
        yson=yson-1
    else:
        yson=yson+1
    R=math.sqrt(pow((xson-xilk),2)+pow((yson-yilk),2))
    Rlist.append(R)
    sqrtNlist.append(math.sqrt(i))
    print("Adim sayisi: ",int(i))
    print("Orjine olan uzaklik: ",int(R))
    print(50*"-")
print("Bulunulan son nokta: ")
print("x: ", xson)
print("y: ", yson)
plt.xlabel('Adim sayisi (Karekök N)')
plt.ylabel('Orjine olan uzaklık (R)')
plt.title('2D rastgele adım teorisi için R ve Karekök N karşılaştırması')
x1=np.array(sqrtNlist)
y1=np.array(Rlist)
plt.plot(x1,y1,'r')
plt.show()