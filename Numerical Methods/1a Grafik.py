import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.title('h=0.1 adım aralığı için grafik karşılaştırması')
x1=np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
             1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
y1=np.array([1.0,0.88000,0.77528,0.68535,0.60927,0.54591,
             0.49405,0.45255,0.42042,0.39687,0.38140,0.37377,
             0.37414,0.38312,0.40189,0.43244,0.47784,0.54283,
             0.63457,0.76402,0.94815])
plt.plot(x1,y1,'ro',label="Nümerik Çözüm")
x2=np.linspace(0,2)
y2=np.exp((pow(x2,3)/3)-(1.2*x2))
plt.plot(x2,y2,'b',label="Analitik Çözüm")
plt.legend(loc='upper left')
