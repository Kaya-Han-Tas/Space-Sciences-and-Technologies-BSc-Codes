import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.title('h=0.5 adım aralığı için grafik karşılaştırması')
x1=np.array([0.0,0.5,1.0,1.5,2.0])
y1=np.array([1.0,0.60187,0.45559,0.53404,1.16191])
plt.plot(x1,y1,'ro',label="Nümerik Çözüm")
x2=np.linspace(0,2)
y2=np.exp((pow(x2,3)/3)-(1.2*x2))
plt.plot(x2,y2,'b',label="Analitik Çözüm")
plt.legend(loc='upper left')