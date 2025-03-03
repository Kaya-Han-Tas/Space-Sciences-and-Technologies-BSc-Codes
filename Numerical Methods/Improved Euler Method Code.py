h=float(input("Adim araligini giriniz: "))
x=0.0
y=1.0
y_half=0.0
x2=0.0
def f(x,y):
    return float((y*pow(x,2))-(1.2*y))
while x<2.000001:
    print("2. iterasyon denkleminde kullanilan y fonksiyonu degeri:",y_half)
    print("2. iterasyon denkleminde kullanilan y fonksiyonunun x degeri: ",x2)
    print("Yaklasilan kok degeri:",y)
    print("Yaklasilan kokun fonksiyonunun x degeri: ",x)
    print(40*"-")
    y_half=y+(f(x,y)*(h/2))
    y=y+(f((x+(h/2)),y_half)*h)
    x2=x+(h/2)
    x=x+h