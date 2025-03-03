import matplotlib.pyplot as plt
import math
import numpy as np

#ρ değerleri
rho=[0.17,0.16,0.13,0.11,0.11,0.14,0.16,0.17,0.15,0.09,0.08,0.14,0.17,0.14,
     0.11,0.11,0.11,0.11,0.13,0.16,0.16,0.17,0.16,0.15,0.09,0.14,0.15,0.17,
     0.17,0.16,0.11,0.17,0.15,0.1] #arcsec

#θ değerleri
tetha=[354.5,339.1,317.4,293.8,257.6,225.0,206.5,194.3,178.0,147.1,047.6,
       011.7,355.2,322.0,295.8,287.0,255.1,251.1,226.0,207.8,204.0,191.5,
       181.0,175.2,150.4,013.8,009.9,357.8,355.8,342.1,259.4,194.4,175.3,
       152.7] #degree

#Gözlem Tarihleri
t=[1961.06,1962.16,1963.26,1964.00,1965.12,1966.13,1967.08,1967.9,1968.99,
   1970.27,1971.16,1972.15,1973.17,1975.15,1976.12,1976.84,1977.23,1977.36,
   1978.24,1979.12,1979.36,1980.22,1980.97,1981.27,1982.12,1984.17,1984.36,
   1985.11,1985.25,1986.21,1989.23,1992.26,1993.38,1994.20] #Yıl

x=[]
y=[]

#0''.1 direkt olarak 5 cm alınmakta
#x=ρ cos⁡θ ve y=ρ sin⁡θ dönüşümleri
for i in range(len(rho)):
    xvalue=(rho[i]*50*(math.cos(math.radians(tetha[i]))))
    yvalue=(rho[i]*50*(math.sin(math.radians(tetha[i]))))
    x.append(round(xvalue,8))
    y.append(round(yvalue,8))


print(60*"-")
print("x değerleri:","\n")
print(*x,sep ="\n")
print(60*"-")
print("y değerleri:","\n")
print(*y,sep ="\n")
print(60*"-")

#Yoldaş yıldızın başyıldız etrafındaki göreli yörüngesinin çizimi (Yatay Hali)
plt.xlabel('y değerleri')
plt.ylabel('x değerleri')
plt.title('Elde edilen x ve y değerleri ile yoldaş yıldızın yörüngesinin çizimi (Yatay Hali)')
plt.plot(y,x,'x') #x ve y değerlerinin grafikte gösterimi
plt.plot(0,0,marker='*') #Başyıldızın Konumu
plt.axis([-6.0,3.5,-20.0,20.0])
plt.show()

#Yoldaş yıldızın başyıldız etrafındaki göreli yörüngesinin çizimi (Dikey Hali)
plt.xlabel('x değerleri')
plt.ylabel('y değerleri')
plt.title('Elde edilen x ve y değerleri ile yoldaş yıldızın yörüngesinin çizimi (Dikey Hali)')
plt.plot(x,y,'x') #x ve y değerlerinin grafikte gösterimi
plt.plot(0,0,marker='*') #Başyıldızın Konumu
plt.axis([-25.0,25.0,-6.0,3.5])
plt.show()

#A,B,H,G,F Katsayılarını elde etme
#y=0 durumunda elde edilen 2 tane x değeri (yaklaşık)
x1=-7.99878156 #23
x2=8.49373479 #28

#x=0 durumunda elde edilen 2 tane y değeri (yaklaşık)
y1=-5.40614442 #31
y2=2.95382136 #11

#A ve G katsayılarını bulma işlemi
A=1/(x1*x2)
G=-((x1+x2)/(2*x1*x2))

#B ve F katsayılarını bulma işlemi
B=1/(y1*y2)
F=-((y1+y2)/(2*y1*y2))

#H katsayısını bulma işlemi
Hvalues=[]
Hvaluestotal=0
for i in range(len(x)):
    Hv=-((((A*pow(x[i],2))+((B*pow(y[i],2))+(2*G*x[i])+(2*F*y[i])+1))/(2*x[i]*y[i])))
    Hvalues.append(Hv)
    Hvaluestotal=Hvaluestotal+Hv
    
H=Hvaluestotal/len(Hvalues)

print("A:",A)
print("B:",B)
print("G:",G)
print("F:",F)
print("H:",H)
print(60*"-")

#Büyük Omega Bulma İşlemi (rad ve derece cinsinden)
OM_rad=math.atan(-2*(((F*G)-H)/(pow(F,2)-pow(G,2)+A-B)))/2
OM_deg=math.degrees(OM_rad)
print("Büyük Omega:", OM_deg, "derece")
print(60*"-")

#tani^2/p^2 değerini Bulma İşlemi
tanibolup=-((2*((F*G)-H))/(math.sin((2*OM_rad))))
print("tani^2/p^2 değeri:", tanibolup)
print(60*"-")

#Parametre Uzunluğu (p) Bulma İşlemi (cm ve açı saniyesi cinsinden iki değer de bulunmuştur)
PL=math.sqrt(2/((-tanibolup)+pow(F,2)+pow(G,2)-(A+B)))
print("Parametre Uzunluğu:", PL, "cm")
print("Parametre Uzunluğu:", (PL*0.1)/5, "açı saniyesi")
print(60*"-")

#Yoldaş Bileşenin Yönüne bakılmaksızın Yörünge Eğikliği (i) bulma işlemi (rad ve derece cinsinden)
tani=(math.sqrt(pow(PL,2)*tanibolup))
i_rad=(math.atan(tani))
i_deg=math.degrees(i_rad) #Elde edilen yörünge eğikliği değerinin rad ve deg cinsinden ifadesi
print("Bulunan Yörünge Eğikliği:", i_deg, "derece")

#Yoldaş Bileşenin Yönüne göre asıl Yörünge Eğikliği (i) değerini bulma işlemi (rad ve derece cinsinden)
i_deg=180-math.degrees(i_rad)
i_rad=math.pi-(math.atan(tani)) #Yönün dahil edilmesi ile elde edilen yörünge eğikliği değerinin rad ve deg cinsinden ifadesi
print('Yöne bağlı Asıl Yörünge Eğikliği Değeri:', i_deg, "derece")
print(60*"-")

#Yoldaş Bileşenin Yönüne bakılmaksızın Küçük Omega bulma işlemi (rad ve derece cinsinden)
tanom=-((((G*math.sin(OM_rad))-(F*math.cos(OM_rad)))*math.cos(i_rad))/((G*math.cos(OM_rad))+(F*math.sin(OM_rad))))
om_rad=math.atan(tanom)
om_deg=math.degrees(math.atan(tanom))
print("Bulunan Enberinin Boylamı:", om_deg, "derece")

#Yoldaş Bileşenin Yönüne göre asıl Küçük Omega değerini bulma işlemi (rad ve derece cinsinden)
om_rad=(2*math.pi)+math.atan(tanom)
om_deg=360+math.degrees(math.atan(tanom))
print("Yöne bağlı Asıl Enberinin Boylamı Değeri:", om_deg, "derece")
print(60*"-")

#Yörünge Basıklığını Bulma İşlemi
e=(-PL*((G*math.cos(OM_rad))+(F*math.sin(OM_rad))))/math.cos(om_rad)
print("Yörünge Basıklığı:", e, "cm")
print(60*"-")

#Yörünge Yarı-Büyük Eksen Uzunluğunu Bulma İşlemi
a=PL/(1-pow(e,2))
print("Yörünge Yarı-Büyük Eksen Uzunluğu:", a, "cm")
print("Yörünge Yarı-Büyük Eksen Uzunluğu:", (a*0.1)/5, "açı saniyesi")
print(60*"-")

#Gerçek Ayrıklık değerlerini bulma işlemi
sin_val=[]
cos_val=[]
nuartiomega_val=[]

#Sinüs, Kosinüs ve Nü Artı Omega değerlerini bulma işlemi
for i in range(len(tetha)):
    sin=math.sin(math.radians(tetha[i])-OM_rad)
    cos=math.cos(math.radians(tetha[i])-OM_rad)
    sin_val.append(round(math.degrees(sin),8))
    cos_val.append(round(math.degrees(cos),8))
    nuartiomega=math.atan((sin/cos)*(1/math.cos(i_rad)))
    nuartiomega_val.append(math.degrees(nuartiomega))
    
print("Sinüs Değerleri:","\n")
print(*sin_val,sep="\n")
print(60*"-")
print("Kosinüs Değerleri:","\n")
print(*cos_val,sep="\n")
print(60*"-")
print("Nü artı Omega değerleri: ","\n")
print(*nuartiomega_val,sep="\n")
print(60*"-")

#Nü artı Omega değerlerini bölgelere göre düzeltme işlemi
nuartiomega_fix_val=[]
print("Bölgelere Göre Düzeltilmiş Nü artı Omega Değerleri (Bölgeler ile beraber):","\n")
for i in range(len(tetha)):
    x=nuartiomega_val[i] #nü artı omega değerleri için parametre
    #1. Bölge
    if cos_val[i]>0 and sin_val[i]<0:
        if x<0:
            x=x+360
        if x>0 and x<=90:
            nuartiomega_fix_val.append(x)
        elif x>90 and x<=180:
            x-=90
            nuartiomega_fix_val.append(x)
        elif x>180 and x<=270:
            x-=180
            nuartiomega_fix_val.append(x)
        elif x>270 and x<=360:
            x-=270
            nuartiomega_fix_val.append(x)
        print("1. Bölge:", x)
    
    #2. Bölge
    if cos_val[i]<0 and sin_val[i]<0:
        if x<0:
            x=x+360
        if x>0 and x<=90:
            x+=90
            nuartiomega_fix_val.append(x)
        elif x>90 and x<=180:
            nuartiomega_fix_val.append(x)
        elif x>180 and x<=270:
            x-=90
            nuartiomega_fix_val.append(x)
        elif x>270 and x<=360:
            x-=180
            nuartiomega_fix_val.append(x)
        print("2. Bölge:", x)
            
    #3.Bölge
    if cos_val[i]<0 and sin_val[i]>0:
        if x<0:
            x=x+360
        if x>0 and x<=90:
            x+=180
            nuartiomega_fix_val.append(x)
        elif x>90 and x<=180:
            x+=90
            nuartiomega_fix_val.append(x)
        elif x>180 and x<=270:
            nuartiomega_fix_val.append(x)
        elif x>270 and x<=360:
            x-=90
            nuartiomega_fix_val.append(x)
        print("3. Bölge:", x)
    
    #4.Bölge
    if cos_val[i]>0 and sin_val[i]>0:
        if x<0:
            x=x+360
        if x>0 and x<=90:
            x+=270
            nuartiomega_fix_val.append(x)
        elif x>90 and x<=180:
            x+=180
            nuartiomega_fix_val.append(x)
        elif x>180 and x<=270:
            x+=90
            nuartiomega_fix_val.append(x)
        elif x>270 and x<=360:
            nuartiomega_fix_val.append(x)
        print("4. Bölge:", x)

print(60*"-")
#Nü değerlerini bulma işlemi
nu_val=[]
for i in range(len(tetha)):
    nu=nuartiomega_fix_val[i]-om_deg
    if nu<0:
        nu+=360
        nu_val.append(nu)
    else:
        nu_val.append(nu)

print("Gerçek Ayrıklık (nü) değerleri: ","\n")
print(*nu_val,sep="\n")
print(60*"-")

#Dış Ayrıklık (E) değerlerini elde etme
E_val=[]
for i in range(len(tetha)):
    E=2*math.atan((math.tan(nuartiomega_fix_val[i]/2)*(1/(math.sqrt((1+e)/(1-e))))))
    E_val.append(E)

print("Dış Ayrıklık Değerleri (Derece):")
print(*E_val,sep="\n")
print(60*"-")

#Periyot ve Enberiden Geçiş Zamanı Bulma işlemi
T0_val=[]
y=int(0)
#Bütün tarihler arasında enberiden geçiş zamanı adayları bulma
for i in range(len(tetha)-1):
    sin_1=math.sin(math.radians(E_val[y]))
    oran_1=E_val[y]-(e*math.degrees(sin_1))
    y+=1
    sin_2=math.sin(math.radians(E_val[y]))
    oran_2=E_val[y]-(e*math.degrees(sin_2))
    oran=oran_1/oran_2
    T0=((oran*t[y-1])-t[y])/(oran-1)
    T0_val.append(T0)

print("Bulunan Enberi Tarihi Adayları (Yıl Biriminde):","\n")
print(*T0_val,sep="\n")
print(60*"-")

#Bileşenlerin en yakın olduğu, enberi konumunda bulunduğu gözlem noktalarını belirleme
nokta_1=rho.index(min(rho))
nokta_2=nokta_1+1
nokta_3=nokta_1+2
nokta_4=nokta_1+3

print("Bileşenlerin Enberi Noktasına yakın olduğu 4 nokta:","\n")
print("1. nokta:", "\n", "rho:", rho[nokta_1], "\n", "tarih:", t[nokta_1])
print("2. nokta:", "\n", "rho:", rho[nokta_2], "\n", "tarih:", t[nokta_2])
print("3. nokta:", "\n", "rho:", rho[nokta_3], "\n", "tarih:", t[nokta_3])
print("4. nokta:", "\n", "rho:", rho[nokta_4], "\n", "tarih:", t[nokta_4])
print(60*"-")

#Enberiden Geçiş Zamanının Belirlenmesi
print("Bileşenlerin bu noktalarda bulundukları tarihlerden elde edilen Enberiden Geçiş Zamanları:", "\n")
print("1. T0 zamanı = ",T0_val[8], "yıl")
print("2. T0 zamanı = ",T0_val[9], "yıl")
print("3. T0 zamanı = ",T0_val[10], "yıl")

#Periyodun belirlenmesi
sin_P=math.sin(math.radians(E_val[nokta_2]))
P1=(((2*math.pi)*(t[nokta_2]-T0_val[8])/(E_val[nokta_2]-(e*math.degrees(sin_P)))))
P2=(((2*math.pi)*(t[nokta_3]-T0_val[9])/(E_val[nokta_3]-(e*math.degrees(sin_P)))))
P3=(((2*math.pi)*(t[nokta_4]-T0_val[10])/(E_val[nokta_4]-(e*math.degrees(sin_P)))))
print(P1,P2,P3)