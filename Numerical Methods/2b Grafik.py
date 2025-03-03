import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.title('h=0.25 adım aralığı için grafik karşılaştırması')
x1=np.array([0.00,0.25,0.50,0.75,1.0,1.25,1.50,1.75,2.00])
y1=np.array([1.0,0.74832,0.57831,0.47519,0.42770,0.43454,
             0.51297,0.72196,1.23722])
plt.plot(x1,y1,'ro',label="Nümerik Çözüm")
x2=np.linspace(0,2)
y2=np.exp((pow(x2,3)/3)-(1.2*x2))
plt.plot(x2,y2,'b',label="Analitik Çözüm")
plt.legend(loc='upper left')