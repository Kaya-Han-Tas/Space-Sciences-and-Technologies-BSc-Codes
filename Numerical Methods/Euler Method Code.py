h=float(input("Adım aralığını giriniz: "))
x=0.0
y=1.0
def f(x,y):
    return float((y*pow(x,2))-(1.2*y))
while x<2.000001:
    print(y)
    y=y+(f(x,y)*h)
    x=x+h