import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.title('h=0.1 adım aralığı için grafik karşılaştırması')
x1=np.array([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
             1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
y1=np.array([1.0,0.88743,0.78916,0.70460,0.63289,0.57304,
             0.52405,0.48502,0.45520,0.43407,0.42141,0.41734,
             0.42246,0.43795,0.46588,0.50953,0.57402,0.66735,
             0.80215,0.99861,1.28982])
plt.plot(x1,y1,'ro',label="Nümerik Çözüm")
x2=np.linspace(0,2)
y2=np.exp((pow(x2,3)/3)-(1.2*x2))
plt.plot(x2,y2,'b',label="Analitik Çözüm")
plt.legend(loc='upper left')