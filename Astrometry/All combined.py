from astropy.io import fits
from pylab import *
import numpy as np
import scipy.linalg as la

image=fits.open('D:\\UBT\\Astrometri\\Final ödevi\\Fits dosyası + çözümler\\6567_0054_R_new-image.fits')[0].data
table=fits.open('D:\\UBT\\Astrometri\\Final ödevi\\Fits dosyası + çözümler\\6567_0054_R_corr.fits')[1].data

#astrometry.net'ten alınan center coordinates
RA0X=326.617 #degree
DEC0X=-2.934 #degree
RA0=np.deg2rad(RA0X)
DEC0=np.deg2rad(DEC0X)

#astrometry.net'ten alınan asteroidin x ve y piksel koordinatları
xast=1209.625
yast=1252.625

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
    
print("Corr dosyasında bulunan değerler: ","\n",(60*"-"), "\n", table)
print(60*"*")
print(60*"*")
print(60*"*")
print("Referans Yıldızlarının Sağ Açıklığı (Right Ascension)","\n",(60*"-"), "\n", RAX)
print(60*"*")
print("Referans Yıldızlarının Dik Açıklığı (Declination)","\n",(60*"-"), "\n", DECX)
print(60*"*")
print("Referans Yıldızlarının X standart koordinatları","\n",(60*"-"), "\n", Xi)
print(60*"*")
print("Referans Yıldızlarının Y standart koordinatları","\n",(60*"-"), "\n", Yi)
print(60*"*")
print("Referans Yıldızlarının x piksel koordinatları","\n",(60*"-"), "\n", xi)
print(60*"*")
print("Referans Yıldızlarının y piksel koordinatları","\n",(60*"-"), "\n", yi)
print(60*"*")

#Düzlem Sabitleri bulunmadan önce RMS hatalarımız
print("Düzlem Sabitleri bulunmadan önce RMS hataları: ")
#astrometry.net'ten okuduğumuz pixel scale değeri
pixelscale=0.618
print('Pixel Scale (astrometry.net) =', pixelscale, "arcsec/pixel")

RMSerror= sqrt(mean((table.index_x-table.field_x)**2+(table.index_y-table.field_y)**2))
RMSerror_radec= sqrt(mean((table.index_ra-table.field_ra)**2+(table.index_dec-table.field_dec)**2))
print('RMSerror =', RMSerror, 'pixel')
print('RMSerror for RA and DEC = ', RMSerror_radec, 'degree')

RMS=RMSerror*pixelscale
RMS_radec=RMSerror_radec*3600
print('RMS =', RMS, 'arcsec')
print('RMS_radec =', RMS_radec, 'arcsec')
print(60*"*")
print(60*"*")
print(60*"*")

#Düzlem Sabitlerini hesaplıyoruz
#Referans yıldızlarının X ve Y standart koordinatlarını barındıracak iki liste tanımlıyoruz.
#Bunları sonrasında matrise çevirecek olup, bu iki liste X1,X2... ve Y1,Y2... şeklinde standart koordinatları içeren matrislerdir.
X_std=list()
Y_std=list()
X_std.append(Xi)
Y_std.append(Yi)
Xf=np.column_stack(X_std)
Yf=np.column_stack(Y_std)

#x1a+y1b+c tarzı matrisimizi oluşturuyoruz
k=list()
k.append(table.field_x)
k.append(table.field_y)
k.append(np.ones(len(Xf)))

#Şimdi de bu değerleri istediğimiz matris formuna çevirmek için aşağıdaki numpy fonksiyonunu kullanıyoruz.
A=np.column_stack(k)

#Elde ettiğimiz matrisleri tekrardan belirtmemiz uygun olacaktır.
print("Referans yıldızlarının X standart koordinatlarının bulunduğu matris; ","\n",(60*"-"), "\n", Xf)
print(60*"*")
print("Referans yıldızlarının Y standart koordinatlarının bulunduğu matris; ","\n",(60*"-"), "\n", Yf)
print(60*"*")
print("Referans yıldızlarının piksel koordinatlarının bulunduğu matris; ", "\n",(60*"-"), "\n", A)
print(60*"*")
print(60*"*")
print(60*"*")

#Artık gerekli üç matrisi de oluşturduğumuza göre düzlem sabitlerini hesaplayabiliriz.
#Bunun için Least Square Method (En küçük kareler yöntemi) kullanılmaktadır.
xcozum, residx, rankx, sx = la.lstsq(A,Xf)
ycozum, residy, ranky, sy = la.lstsq(A,Yf)

#Plate constantları ayrı ayrı gösterebilmek için de çözümleri aşağıda bulunan komutla bir eksene sıralayabiliriz.
PC=np.concatenate((xcozum,ycozum))

#Sonuç olarak Düzlem Sabitlerini printleyebiliriz.
print("Düzlem Sabitleri; ","\n",(60*"-"), "\n", PC)
print(60*"*")
print(60*"*")
print(60*"*")

#Şimdi tüm referans yıldızlarının sağ açıklık ve dik açıklıklarını bulabiliriz.
#Önce bu yıldızların sağ açıklık ve dik açıklıkları için iki tane liste tanımlıyoruz.
Ref_ra_final=list()
Ref_dec_final=list()

#Şimdi her yıldız için sağ açıklık ve dik açıklığı hesaplayıp bu listelere atıyoruz.
for i in range(len(table.index_x)):
    X=0
    Y=0
    Xref=(PC[0]*table.field_x[i])+(PC[1]*table.field_y[i])+PC[2]
    Yref=(PC[3]*table.field_x[i])+(PC[4]*table.field_y[i])+PC[5]
    Ref_ra=RA0+np.arctan((-Xref)/((np.cos(DEC0))-(Yref-np.sin(DEC0))))
    Ref_dec=np.arcsin(((np.sin(DEC0))+(Yref*np.cos(DEC0)))/(sqrt(1+(Xref**2)+(Yref**2))))
    Ref_ra_final.append(np.rad2deg(Ref_ra))
    Ref_dec_final.append(np.rad2deg(Ref_dec))
    
Ref_ra_final=np.array(Ref_ra_final)
Ref_dec_final=np.array(Ref_dec_final)

print("Referans yıldızlarının düzlem sabitleri ile elde edilen sağ açıklık (RA) değerleri: ","\n",(60*"-"),"\n", Ref_ra_final)
print(60*"*")
print("Referans yıldızlarının düzlem sabitleri ile elde edilen dik açıklık (DEC) değerleri: ","\n",(60*"-"),"\n", Ref_dec_final)
print(60*"*")
print(60*"*")
print(60*"*")

#Son olarak bu yıldızların RMS hatalarını hesaplayabiliriz.
print("Düzlem Sabitleri bulunduktan sonra RMS hataları: ","\n",(60*"-"))
RMSerror_radec_final= sqrt(mean((Ref_ra_final-table.index_ra)**2+(Ref_dec_final-table.index_dec)**2))
print('RMSerror for RA and DEC = ', RMSerror_radec_final, 'degree')

RMS_radec_final=RMSerror_radec_final*3600
print('RMS_radec =', RMS_radec_final, 'arcsec')
print(60*"*")
print(60*"*")
print(60*"*")

#Elimizde hem asteroidin piksel koordinatları hem de düzlem sabitleri bulunduğundan aşağıdaki gibi asteroidin standart koordinatları X ve Y'i elde edebiliriz.
Xast=(PC[0]*xast)+(PC[1]*yast)+PC[2]
Yast=(PC[3]*xast)+(PC[4]*yast)+PC[5]

print("Asteroidin X standart koordinatı","\n",(60*"-"), "\n", Xast)
print(60*"*")
print("Asteroidin Y standart koordinatı","\n",(60*"-"), "\n", Yast)
print(60*"*")
print(60*"*")
print(60*"*")

#Son olarak artık aşağıdaki denklemler kullanılarak Asteroidin Sağ açıklığı (RA) ve Dik Açıklığı (DEC) hesaplanır.
RAast=RA0+np.arctan((-Xast)/((np.cos(DEC0))-(Yast-np.sin(DEC0))))
DECast=np.arcsin(((np.sin(DEC0))+(Yast*np.cos(DEC0)))/(sqrt(1+(Xast**2)+(Yast**2))))

FinalRA=np.rad2deg(RAast)
FinalDEC=np.rad2deg(DECast)

print("Asteroidin Sağ Açıklığı (RA/Right Ascension): ","\n",(60*"-"), "\n", FinalRA)
print("Asteroidin Dik Açıklığı (DEC/Declination): ","\n",(60*"-"), "\n", FinalDEC)
print(60*"*")
print(60*"*")
print(60*"*")