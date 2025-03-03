import math

#Verilenler
paralaks=0.076 #arcsec
ozhareket=0.20 #arcsec
vr=3 #km/s
m1=2.0 #kadir
m2=2.8 #kadir
a_arcsec=6.06 #arcsec
P=306 #yıl
#Sıcaklıklar aynı verilmiştir.

#Önce Uzaklığı bulmamız gerekmekte
d=1/paralaks
print(60*"-")
print("Sistemin Uzaklığı (d): ", d, "pc")

#Teğetsel Hız formülü
vt=4.74*ozhareket*d #km/s
print(60*"-")
print("Sistemin Teğetsel Hızı (vt): ", vt, "km/s")

#Uzay Hızı hesabı
v=math.sqrt(pow(vr,2)+pow(vt,2))
print(60*"-")
print("Sistemin Uzay Hızı (v): ", v, "km/s", "(Soruda İstenen)")

#Sıcaklıklar Aynı olduğundan bolometrik=görünür parlaklık
Mbol1=m1
Mbol2=m2

#Pogson Formülünden Işıtmalar Oranı
x=(Mbol1-Mbol2)/-2.5
L1_bolu_L2=pow(10,x)
print(60*"-")
print("Işıtmalar Oranı (L1/L2): ", L1_bolu_L2, "(Soruda İstenen)")

#Kütle Işıtma Bağıntısından Kütleler Oranı
M1_bolu_M2=pow((L1_bolu_L2),1/3)
print(60*"-")
print("Kütleler Oranı (M1/M2): ", M1_bolu_M2)

#a'nın Astronomik Birim cinsinden eldesi
a=a_arcsec/paralaks
print(60*"-")
print("Yarı-Büyük Eksen Uzunluğu (a): ", a, "AB")

#Kepler Formülünden Kütleler Toplamı
M1_arti_M2=pow(a,3)/pow(P,2)
print(60*"-")
print("Kütleler Toplamı (M1+M2): ", M1_arti_M2, "Mgüneş")

#Ayrı Ayrı Kütlelerin Bulunması
#M1=1.2783997194630237 M2 olduğundan -> M1+M2=2.2783997194630237 M2'dir.
#Buradan yola çıkarak aşağıdaki ifade yazılabilir.
M2=M1_arti_M2/2.2783997194630237
M1=1.2783997194630237*M2
print(60*"-")
print("1. Yıldızın Kütlesi (M1): ", M1, "Mgüneş", "(Soruda İstenen)")
print("2. Yıldızın Kütlesi (M2): ", M2, "Mgüneş", "(Soruda İstenen)")

#Yarıçaplar Oranını Bulma
#L=4*pi*R^2*Sigma*Tetkin^4 olarak yazılabilir.
#İki yıldızın sıcaklıkları aynı olduğundan Işıtma oranlarının karekökü bize yarıçap oranını verir.
R1_bolu_R2=pow((L1_bolu_L2),1/2)
print(60*"-")
print("Yarıçaplar Oranı (R1/R2): ", R1_bolu_R2, "(Soruda İstenen)")