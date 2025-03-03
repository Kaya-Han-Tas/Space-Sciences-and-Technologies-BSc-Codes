import matplotlib.pyplot as plt
import numpy as np
plt.xlabel('Frekans (Hz)')
plt.ylabel('Işınım Şiddeti (W/s*m^2)')
plt.title('Frekans-Işınım Şiddeti karşılaştırması')
h=6.6261E-34
c=3.0E8
k=1.38E-23
def f(nu, T):
    ust = 2*h*pow(nu,3)
    eustu = (h*nu)/(k*T)
    bnu = ust/((pow(c,2))*(np.exp(eustu)-1.0))
    return bnu
xekseni=np.arange(1e12,2000e12,10e12)
sonuc = f(xekseni,5000)
sonuc2= f(xekseni,6000)
plt.plot(xekseni*1e9, sonuc, 'b', label="T=5000 K")
plt.plot(xekseni*1e9,sonuc2, 'r', label='T=6000 K')
plt.legend(loc='upper right')
plt.show()