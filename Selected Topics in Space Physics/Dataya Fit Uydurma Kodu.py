from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
import numpy as np
import csv
#Dataların bulunduğu dosyayı açıyoruz. (Comma Seperated Values (CSV) ile çalışıyoruz)
#Datalar .txt uzantılı dosyaya x,y,x,y,x,y,x,y... formatında tek satırda yazılmalıdır.
datafile=open(r"D:\UBT 4. SINIF\UBT\Uzay Fiziğinde Seçilmiş Konular\Ödevler\Data Set.txt",'r')

#Dataları dosyalardan çekiyoruz.
dataextract=csv.reader(datafile)

#Şimdi de datalarımızı bir listeye çekiyoruz.
data=[]
for row in dataextract:
    data.append(row)

datafile.close()
#İstenirse print(data) ile hangi dataların olduğunda bakabiliriz.
#Şimdi de x ve y datalarını ayrı ayrı listelere çekiyoruz.
data=data.pop()
xdata=[]
ydata=[]
count=-1
#Burada % parametresi bölmeden kalan ile alakalıdır.
#Bu sayede tek sayıya sahip indextekiler y dataları olur.
#Aynı şekilde çift sayıya sahip indextekiler de x dataları olur.
for i in data:
    count+=1
    if count%2==0:
        xdata.append(i)
    else:
        ydata.append(i)

#Şimdi liste içindekilerin tamamını sayıya çeviriyoruz.
for i in range(0,len(xdata)):
    xdata[i]=int(xdata[i])
    ydata[i]=int(ydata[i])

#Şimdi datalarımızı array'e çevirerek işimizi kolaylaştırabiliriz.
xdata=np.asarray(xdata)
ydata=np.asarray(ydata)
plt.plot(xdata,ydata,'o')

#Öncelikle Parabolik Fiti tanımlıyoruz. (y=ax^2+bx+c)
def Parabolic(xdata,a,b,c):
    y=a*(pow(xdata,2))+b*(xdata)+c
    return y

#Burada eğri fiti fonksiyonu 3 tane girdi istemektedir.
#Aynı şekilde eğri fiti de 2 tane çıktı vermektedir.
#Birinci çıktı parametreler için en uygun değerleri verir.
#İkinci çıktı ise parametrelerin hatalarını hesaplamak için kullanılan tahmini olasılıklardan oluşan matristir.
parameters_parabolic, covariance_parabolic = curve_fit(Parabolic, xdata, ydata)

#Artık a,b,c parametrelerini yazdırabiliriz.
a_value=parameters_parabolic[0]
b_value=parameters_parabolic[1]
c_value=parameters_parabolic[2]

print("Parabolik Fit: ", 50*"-")
print("a parametresinin değeri: ", a_value)
print("b parametresinin değeri: ", b_value)
print("c parametresinin değeri: ", c_value)
print(60*"-")

#Şimdi de fitimizin uygunluğunu görmek için parametrelerini belirlediğimiz denklemi kullanıyoruz.
#Buradan y değerlerini hesaplıyoruz.
#Sonrasında da datamızı bu fit ile karşılaştırıyoruz.
fit_parabolic=Parabolic(xdata,a_value,b_value,c_value)
plt.plot(xdata,ydata,'o',label='Data')
plt.plot(xdata,fit_parabolic, '-', label='Parabolic Fit',color='red')
plt.legend(loc='upper right')

#Hatayı hesaplamak için de matristeki köşegen değerlerin karekökü alınır.
error=np.sqrt(np.diag(covariance_parabolic))
a_error=error[0]
b_error=error[1]
c_error=error[2]
print("a parametresinin hatası: ",a_error)
print("b parametresinin hatası: ",b_error)
print("c parametresinin hatası: ",c_error)
print(60*"-")

#Buradan da Ki Kare değerini hesaplayabiliriz.
#Ki Kare değeri için ihtiyacımız olan y değerleridir.
#Bunun için hem ydata hem de fit_parabolic kullanılacaktır.
chi_squared_parabolic=0
for i in ydata:
    chi_squared_parabolic+=pow((ydata[i-1]-fit_parabolic[i-1]),2)/(fit_parabolic[i-1])

print("Ki Kare Değeri (Parabolik Fit): ", chi_squared_parabolic)
print(60*"*")

#Aynısını lineer fonksiyon fiti için de yapabiliriz. (y=ax+b)
#Önce Lineer Fiti tanımlıyoruz.
def Linear(xdata,a,b):
    y=(a*xdata)+b
    return y

#Şimdi de yine Curve Fit fonksiyonu ile fitimizi yapıyoruz.
parameters_linear, covariance_linear = curve_fit(Linear, xdata, ydata)

#Buradan a,b parametrelerini bulabiliriz.
a_value_linear=parameters_linear[0]
b_value_linear=parameters_linear[1]
print("Lineer Fit: ",50*"-")
print("a parametresinin değeri: ", a_value_linear)
print("b parametresinin değeri: ", b_value_linear)
print(60*"-")

#Şimdi de fitimizin uygunluğunu görmek için y değerlerini bulduğumuz denklemden hesaplıyoruz.
#Datamızı fit ile karşılaştırıyoruz.
fit_linear=Linear(xdata,a_value_linear,b_value_linear)
plt.plot(xdata,fit_linear,'-',label='Linear Fit',color='blue')
plt.legend(loc='upper right')

#Hatalar yine matristeki köşegen değerlerin karekökünü alarak bulunur.
error=np.sqrt(np.diag(covariance_linear))
a_error_linear=error[0]
b_error_linear=error[1]
print("a parametresinin hatası: ",a_error_linear)
print("b parametresinin hatası: ",b_error_linear)
print(60*"-")

#Lineer Fit için de Ki Kare değeri aşağıdaki gibi olacaktır.
chi_squared_linear=0
for i in ydata:
    chi_squared_linear+=pow((ydata[i-1]-fit_linear[i-1]),2)/(fit_linear[i-1])

print("Ki Kare Değeri (Lineer Fit): ", chi_squared_linear)
print(60*"*")