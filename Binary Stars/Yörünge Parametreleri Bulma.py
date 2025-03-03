import math
#saat yönünde dönen yoldaş yıldız için hesap
A=-39.26853425
B=-156.5554215
G=0.3920193
F=-3.8392446
H=10.7265217

OM=math.atan(-(((F*G)-H)/(pow(F,2)-pow(G,2)+A-B)))
print("Büyük Omega:", OM)
print(60*"-")

tanibolup=-((2*((F*G)-H))/(math.sin(math.radians(2*OM))))
print("tani^2/p^2 değeri:", tanibolup)
print(60*"-")

PL=math.sqrt((2*tanibolup)/(pow(F,2)+pow(G,2)-(A+B)))
print("Parametre Uzunluğu:", PL)
print(60*"-")

tani=(math.sqrt((-2*((F*G)-H)*pow(PL,2))/math.sin(math.radians(2*OM))))
i=math.atan(-tani)
print("Yörünge Eğikliği:", i)
print(60*"-")

tanom=-((((G*math.sin(OM))-(F*math.cos(OM)))*math.cos(i))/((G*math.cos(OM))+(F*math.sin(OM))))
om=math.atan(tanom)
print("Enberinin Boylamı:", om+360)
print(60*"-")

e=(PL*((G*math.sin(OM))-(F*math.cos(OM)))*math.cos(i))/math.sin(om+360)
print("Yörünge Basıklığı:", e)
print(60*"-")

a=PL/(1-pow(e,2))
print("Yörünge Yarı-Büyük Eksen Uzunluğu:", a)
print(60*"-")

tetha1=354.5
tetha2=339.1
GA1=math.atan((math.tan(tetha1-OM))*((1/math.cos(i))-om))
GA2=math.atan((math.tan(tetha2-OM))*((1/math.cos(i))-om))
print("1. Gerçek Açıklık Değeri", GA1)
print("2. Gerçek Açıklık Değeri", GA2)
print(60*"-")

E1=math.atan((2*math.tan(GA1/2))/(math.sqrt(1+e/1-e)))
E2=math.atan((2*math.tan(GA2/2))/(math.sqrt(1+e/1-e)))
print("1. E değeri", E1)
print("2. E Değeri", E2)