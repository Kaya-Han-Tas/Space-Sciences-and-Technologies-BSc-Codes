import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('Dalgaboyu (nm)')
plt.ylabel('Işınım Şiddeti (W/m^2*nm)')
plt.title('Dalgaboyu-Işınım Şiddeti karşılaştırması')
h=6.6261E-34
c=3.0E8
k=1.38E-23
def f(lmbd, T):
    ust = 2*h*pow(c,2)
    eustu = (h*c)/(lmbd*k*T)
    blmbd = ust/((pow(lmbd,5))*(np.exp(eustu)-1.0))
    return blmbd
xekseni=np.arange(1e-9,6e-6,1e-9)
sonuc = f(xekseni,5000)
sonuc2= f(xekseni,6000)
plt.plot(xekseni*1e9, sonuc, 'b', label="T=5000 K")
plt.plot(xekseni*1e9,sonuc2, 'r', label='T=6000 K')
plt.legend(loc='upper right')
plt.show()