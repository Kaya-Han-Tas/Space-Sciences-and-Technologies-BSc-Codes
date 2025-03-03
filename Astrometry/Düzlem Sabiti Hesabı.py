from astropy.io import fits
from pylab import *
import numpy as np
import scipy.linalg as la

table=fits.open('D:\\UBT\\Astrometri\\Final ödevi\\Fits dosyası + çözümler\\6567_0054_R_corr.fits')[1].data

#astronomy.net'ten alınan center coordinates
RA0X=326.617 #degree
DEC0X=-2.934 #degree
RA0=np.deg2rad(RA0X)
DEC0=np.deg2rad(DEC0X)

#corr uzantılı dosyamızda bulunan referans yıldızlarının Right Ascension ve Declination değerleri
RAX=table.index_ra #degree
DECX=table.index_dec #degree
RA=np.deg2rad(RAX)
DEC=np.deg2rad(DECX)

#Her bir referans yıldızının X ve Y standart koordinatları
Xi=((np.cos(DEC)*np.sin(RA-RA0))/((np.sin(DEC0)*np.sin(DEC))+(np.cos(DEC0)*np.cos(DEC)*np.cos(RA-RA0))))
Yi=(((np.cos(DEC0)*np.sin(DEC))-(np.sin(DEC0)*np.cos(DEC)*np.cos(RA-RA0)))/((np.sin(DEC0)*np.sin(DEC))+(np.cos(DEC0)*np.cos(DEC)*np.cos(RA-RA0))))

#corr uzantılı dosyamızda bulunan referans yıldızlarının x ve y piksel koordinatları
xi=table.index_x
yi=table.index_y

#3 tane değer seçilerek düzlem sabiti bulmak için çözeceğimiz matris
#Bunun için direkt olarak corr dosyasından ilk üç yıldızın değerlerini kullanabiliriz.
x1=1315.22075134
x2=923.39167225
x3=611.27501263

y1=594.125792
y2=1875.60105074
y3=1800.01706754

X1=0.04724024
X2=-0.01736039
X3=-0.07145815

Y1=0.07483216
Y2=-0.14734924
Y3=-0.13411347

a=b=c=d=e=f=0

#Matris sistemimizi oluşturabiliriz.
A=np.array([[X1],[X2],[X3]])
B=np.array([[Y1],[Y2],[Y3]])
C=np.array([[x1,y1,1],[x2,y2,1],[x3,y3,1]])
P1=np.array([[a],[b],[c]])
P2=np.array([[d],[e],[f]])
PC1=np.dot(C,P1)
PC2=np.dot(C,P2)


plateconstants1=np.linalg.solve(A,PC1)
plateconstants2=np.linalg.solve(B,PC2)

print("Corr dosyasında bulunan değerler: ","\n", table)
print(60*"*")
print(60*"*")
print(60*"*")
print("Referans Yıldızlarının Sağ Açıklığı (Right Ascension)","\n", RAX)
print(60*"-")
print("Referans Yıldızlarının Dik Açıklığı (Declination)","\n", DECX)
print(60*"*")
print("Referans Yıldızlarının X standart koordinatları","\n", Xi)
print(60*"-")
print("Referans Yıldızlarının Y standart koordinatları","\n", Yi)
print(60*"*")
print("Referans Yıldızlarının x piksel koordinatları","\n", xi)
print(60*"-")
print("Referans Yıldızlarının y piksel koordinatları","\n", yi)
print(60*"*")
print(plateconstants1)
print(plateconstants2)