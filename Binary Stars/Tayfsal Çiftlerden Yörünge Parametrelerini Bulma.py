import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.linalg as la

#Gözlem Zamanları (JD)
t=[2441906.8096, 2441906.8372, 2441908.7903, 2441908.8294, 2441908.8655,
2441909.8123, 2441909.8682, 2441910.6062, 2441911.6921, 2441912.8074, 
2441912.8528, 2441913.7048, 2441913.7841, 2441914.5405, 2441914.7231, 
2441914.7805, 2441916.7730, 2441916.8059, 2441917.8003, 2441917.8357,
2441927.5161, 2441929.5015, 2441929.5127, 2441929.5246, 2441929.7136,
2441929.7376, 2441930.5396, 2441930.5691, 2441930.6694, 2441930.6892,
2441931.4899, 2441931.5591, 2441931.5664, 2441931.6924, 2441933.5308,
2441933.7288, 2441933.8306]

#Gözlem Zamanlarına Karşılık Dikine Hızlar
vr=[-83.9, -83.2, 31.0, 43.9, 55.9, -81.0, -90.3, 100.4, -46.3, -41.4, -58.9,
92.9, 94.7, -78.0, -82.4, -70.5, 67.3, 77.8, -81.4, -79.8, -26.6, 104.8, 105.5,
107.7, 94.1, 92.6, -66.8, -53.3, -27.5, -22.9, 51.1, 11.4, 7.2, -39.3, -84.4,
-60.3, -24.0]

#Yörünge Dönemi
P=1.575531 #gün

#Enberiden Geçiş Zamanı
T0=2426160.500 #JD

#Evre Hesabı
Phase=[]
print(60*"-")
print("Evre Değerleri: ")
for i in range(len(t)):
    Evre=((t[i]-T0)/(P))
    Evre_sbtrct=round(Evre,0)
    if Evre<Evre_sbtrct:
        Evre_sbtrct=Evre_sbtrct-1
        Evre=Evre-Evre_sbtrct
    else:
        Evre=Evre-Evre_sbtrct
    print(Evre)
    Phase.append(Evre)
print(60*"-")

#Dikine Hız Eğrisinin Çizimi
plt.xlabel('Evre')
plt.ylabel('Dikine Hız Değerleri (km/s)')
plt.title('DV Agr Çift Sisteminin Gözlem Verilerinden Elde Edilen Dikine Hız Eğrisi\n (T0=2426160.500, P=1.575531)')
plt.plot(Phase,vr,".")
plt.show()

#Eğriye en iyi uyan fiti bulma çabası
v_gama=0
K=0
om_deg=0
e=0
true_anom=0
#vr=v_gama+K*[(e*math.cos(math.radians(om_deg)))+(math.cos(math.radians(true_anom)+math.radians(om_deg)))]

print("Başlangıç Parametre Seti: ")
#Omega yaklaşık olarak 90 derece olmalıdır çünkü enberi noktasından harekete
#başlanmış olup iniş düğümüne, enöteye ve çıkış düğümüne doğru ilerleme var.
#Buradan yörünge çizilirse sonucunda omeganın 90 derece (veya ona yakın) bir
#değere sahip olması gerektiği anlaşılacaktır.
om_deg=90
om_rad=math.radians(om_deg)
print(60*"*")
print("-> Enberinin Argümanı:", om_deg, "derece", "(", om_rad, "radyan)")
print(60*"*")
#Evrenin 0 ve 1 olduğu noktalar direkt olarak enberi olarak kabul edilebilir.
#Bu nedenle bu noktaların konumundan yola çıkarak sistem hızı da bulunabilir.
#Sonuçta enberi noktasında yıldızın dikine hızı sıfır veya sistemin hızına eşit olacaktır.
#Buradan yola çıkarsak öncelikle minimum evre ve maksimum evre değerlerini bulmamız gerekir.
#Sonrasında bu evre değerlerine karşılık gelen hızlardan Enberi Hızlarını elde ederiz.
evre_min=min(Phase)
enberi_hız_1=vr[Phase.index(min(Phase))]
evre_max=max(Phase)
enberi_hız_2=vr[Phase.index(max(Phase))]
print(60*"'")
print("Minimum Evre:", evre_min)
print("Maksimum Evre:", evre_max)
print("1. Enberi Hızı:", enberi_hız_1, "km/s")
print("2. Enberi Hızı:", enberi_hız_2, "km/s")

#0'a veya 1'e en yakın olan değer yani "1. Enberi Hızı" ve "Evre Min" değerini kullanmamız uygun olacaktır.
print(60*"'")
print("Minimum Evre Enberi Evresine Daha Yakın Olduğundan; ")
print("Enberi Evresi: ", evre_min)
print("Enberi Hızı: ", enberi_hız_1)
print(60*"'")

#Sistemin Hızı Enberinin Hızına eşit olduğundan başlangıç olarak sistem hızı aşağıdaki gibi seçilebilir.
print("Enberi Hızı Sistemin Hızına eşit olduğundan; ")
v_gama=enberi_hız_1
print(60*"*")
print("-> Sistemin Hızı: ", v_gama, "km/s")
print(60*"*")

#Görmede kolaylık olması açısından Dikine Hız Eğrisini sistem hızını gösterecek şekilde çiziyoruz.
#Dikine Hız Eğrisinin Sistem Hızı ile Çizimi
plt.xlabel('Evre')
plt.ylabel('Dikine Hız Değerleri (km/s)')
plt.title('DV Agr Çift Sisteminin Gözlem Verilerinden Elde Edilen Dikine Hız Eğrisi\n (T0=2426160.500, P=1.575531)')
plt.plot(Phase,vr,".")
plt.plot([0,1],[7.2,7.2],'--', label='Sistem Hızı')
plt.legend(loc='upper left')
plt.show()

#Grafikten görüleceği üzere Dikine Hız Eğrimiz Sinüsoidal bir eğriye benzerdir.
#Buradan anlaşılacağı üzere yörünge basıklığı da 0'a yakındır.
#Yaklaşık olarak 0.1 olarak alıp başlayabiliriz.
e=0.1
print(60*"*")
print("-> Yörünge Basıklığı: ", e)
print(60*"*")
#Yarı-Genlik Değeri de A+B/2 olarak yazılabilmekteydi.
#Burada A çıkış düğümünün, B ise iniş düğümünün genliğidir.
#Bu genlikleri bulmak için minimum ve maksimum dikine hızlar gereklidir.
#Maksimum ve Minimum dikine hızlardan sistem hızını çıkartarak iki genliği de bulabiliriz.
#Bileşen A yani çıkış düğümünde max hız, B yani iniş düğümünde min hıza sahip olur.
vr_max=max(vr)
vr_min=min(vr)
A=max(vr)-v_gama
B=v_gama-min(vr) #Negatif değerlerle uğraşıldığından eksili yazdık
K=(A+B)/2
print(60*"'")
print("Çıkış Düğümü Genliği: ", A)
print("İniş Düğümü Genliği: ", B)
print(60*"'")
print(60*"*")
print("-> Yarı-Genlik Değeri: ", K)
print(60*"*")

#Gerçek Ayrıklık değerlerini bulma
#Burada her bir noktadaki E değerini iterasyon yaparak bulmamız gerekiyor.
#Bunun için iteratif yaklaşım olarak E_0=M yaklaşımı yapıyoruz yani E_1=M+esinM
#Sonrası için E_i+1=M+sinE_i şeklinde iterasyonumuzu yazabiliriz.
#Burada önemli olan M değerini bulurken t-T0 değerinin GÜN cinsinden olması gerektiğidir.
#Bulunan evrelerden yola çıkarak 1 evre 1.575531 gün olduğundan herhangi bir evrede
#Enberiden geçişten sonra kaç gün geçtiğini bulabilmemiz mümkündür.
#Önce bununla uğraşıyoruz.
t_days=[]
for i in range(len(Phase)):
    day=P*Phase[i]
    t_days.append(day)
print(60*"-")
print("t-T0 (Enberi geçişinden sonra geçen gün) değerleri: ")
print(*t_days, sep="\n")
print(60*"-")

#Artık İterasyona Geçebiliriz.
Ei_old=0
Ei_new=0
E_values=[]
for i in range(len(t)):
    M=((2*math.pi)/P)*(t_days[i])
    Ei_old=M
    x=abs(math.degrees(Ei_new)-math.degrees(Ei_old))
    while x>0.001:
        Ei_new=M+(e*math.sin(Ei_old))
        x=abs(math.degrees(Ei_new)-math.degrees(Ei_old))
        Ei_old=Ei_new
    E_values.append(math.degrees(Ei_new))

print(60*"-")
print("E Değerleri: ")
print(*E_values, sep="\n")
print(60*"-")

#Gerçek Ayrıklık Değerleri bulunur
nu_values=[]
for i in range(len(E_values)):
    nu=2*math.atan((math.sqrt((1+e)/(1-e)))*math.tan(math.radians(E_values[i]/2)))
    nu=math.degrees(nu)
    if nu<0:
        nu=360+nu
    nu_values.append(nu)

print(60*"-")
print("Gerçek Ayrıklık (nü) Değerleri: ")
print(*nu_values, sep="\n")
print(60*"-")

#Şimdi de bunun sonucunda fit edilebilecek eğrinin genel resmi için
#dikine hız formülü kullanarak bir eğri fiti çiziyoruz.
#Önce Dikine Hız Formülünden dikine hız değerlerimizi elde ediyoruz.
vr_fit=[]
for i in range(len(nu_values)):
    vr_fit_val=v_gama+K*((e*math.cos(math.radians(om_deg)))+(math.cos(math.radians(nu_values[i])+math.radians(om_deg))))
    vr_fit.append(vr_fit_val)

print(60*"-")
print("Eğri Fiti için elde edilen Dikine Hız Değerleri: ")
print(*vr_fit, sep="\n")
print(60*"-")

#Şimdi de eğrimizi buna göre çizdiriyoruz.
plt.xlabel('Evre')
plt.ylabel('Dikine Hız Değerleri (km/s)')
plt.title('DV Agr Çift Sisteminin Gözlem Verilerinden Elde Edilen Dikine Hız Eğrisi\n (T0=2426160.500, P=1.575531)')
plt.plot(Phase,vr,".", label='Orijinal Dikine Hız Eğrisi')
plt.plot(Phase,vr_fit, "r.", label='Eğri Fiti Değerleri')
plt.plot([0,1],[7.2,7.2],'--', label='Sistem Hızı')
plt.legend(loc='upper left')
plt.show()

#Artık Diferansiyel Düzeltme yöntemine geçiyoruz.
#Öncelikle seçtiğimiz Başlangıç Parametrelerini yazıyoruz.
om_old=90 #degree
om_new=0
om_old_rad=math.radians(om_old)
v_gama_old=7.2
v_gama_new=0
e_old=0.1
e_new=0
K_old=99.0
K_new=0
i=0 #sadece çıktıda numaralandırma amacı ile koyulmuştur.
hata_vgama=1
hata_K=1
hata_e=1
hata_om=1
print(60*"-")
print(60*"-")

#Şimdi de her bir parametrenin başında bulunan "sayısal değerleri" belirlemek
#için teker teker katsayıları hesaplıyoruz. Bunun için de her bir gözlem noktası
#için katsayıları teker teker hesaplamamız gerekir.
#Bunları da aşağıdaki döngüler ile gerçekleştirebiliriz.

deltavr_values=[]
K_coefficient_values=[]
e_coefficient_values=[]
om_coefficient_values=[]
for i in range(len(vr)):
    if hata_e<0.1 and hata_vgama<0.1 and hata_om<0.1:
        break
    
    coefficients=[] #Katsayı Matrisi için oluşturulan denklem
    
    delta_vr=vr[i]-vr_fit[i]
    deltavr_values.append(delta_vr)

    K_coefficient=(e*math.cos(om_old_rad))+(math.cos((math.radians(nu_values[i]))+om_old_rad))
    K_coefficient=math.degrees(K_coefficient)
    K_coefficient_values.append(K_coefficient)

    e_coefficient=K_old*(math.cos(om_old_rad)-((math.sin((math.radians(nu_values[i]))+om_old_rad))*math.sin(math.radians(nu_values[i]))*(2+e*math.cos(math.radians(nu_values[i]))))/(1-pow(e,2)))
    e_coefficient=math.degrees(e_coefficient)
    e_coefficient_values.append(e_coefficient)
    
    om_coefficient=K_old*((e*math.sin(om_old_rad))+(math.sin((math.radians(nu_values[i]))+(om_old_rad))))
    om_coefficient=math.degrees(om_coefficient)
    om_coefficient_values.append(om_coefficient)
    
    deltav_matrix=[] #Delta Vr değerleri için liste/matris oluşturduk.
    deltav_matrix.append(deltavr_values) #Bu listeye bulduğumuz hız değerlerini ekledik.
    deltav_matrix=np.column_stack(deltav_matrix) #Delta vr değerlerini matrise tek sütun olarak sıraladık.
    coefficients.append((np.ones(len(K_coefficient_values)))) #Katsayı Matrisine Sistem Hızı katsayısı 1 olduğundan denklem sayısı kadar 1 ekledik.
    coefficients.append((K_coefficient_values)) #Katsayı Matrisine K'nın katsayılar matrisini ekledik.
    coefficients.append((e_coefficient_values)) #Katsayı Matrisine e'nin katsayılar matrisini ekledik.
    coefficients.append((om_coefficient_values)) #Katsayı Matrisine omega'nın katsayılar matrisini ekledik.
    coefficients_matrix=np.column_stack(coefficients) #Katsayı Matrisine eklediğimiz matrisleri teker teker sütunlar halinde sıraladık.
    
    #En Küçük Kareler Yöntemi Kullanılır
    hatalar, residx, rankx, sx = la.lstsq(deltav_matrix,coefficients_matrix)
    i+=1
    hatalar=np.column_stack(hatalar)
    print(60*"*")
    print(i, ". iterasyonda elde edilen hata değerleri: ")
    print(hatalar)
    
    #Elde edilen hatalar sırasıyla parametrelerimize eklenir.
    v_gama_new=v_gama_old+hatalar[0]
    K_new=K_old+hatalar[1]
    e_new=e_old+hatalar[2]
    om_new_rad=om_old_rad+hatalar[3]
    
    #Yeni Parametreler elde edilmiş olur.
    print(60*"-")
    print(i, ". iterasyonda elde edilen parametre değerleri: ")
    print("Düzeltmilmiş Sistem Hızı: ", v_gama_new, "km/s")
    print("Düzeltilmiş Yarı-Genlik Değeri: ", K_new)
    print("Düzeltilmiş Yörünge Basıklığı Değeri: ", e_new)
    print("Düzeltilmiş Enberinin Argümanı Değeri: ", om_new_rad, "radyan")
    print(60*"*")
    
    #Hata Hassasiyetine Bakılır.
    hata_vgama=abs(v_gama_new-v_gama_old)
    hata_K=abs(K_new-K_old)
    hata_e=abs(e_new-e_old)
    hata_om=abs(om_new_rad-om_old_rad)
    print(hata_vgama,hata_K,hata_e,hata_om)
    
    #Bir sonraki iterasyon için hazırlık yapılır.
    v_gama_old=v_gama_new
    K_old=K_new
    e_old=e_new
    om_old_rad=om_new_rad

#print(60*"-")
#print("Delta Vr değerleri")
#print(*deltavr_values, sep="\n")
#print(60*"-")

#print(60*"-")
#print("K katsayısının değerleri: ")
#print(*K_coefficient_values, sep="\n")
#print(60*"-")

#print(60*"-")
#print("Yörünge Basıklığının (e) katsayısının değerleri: ")
#print(*e_coefficient_values, sep="\n")
#print(60*"-")

#print(60*"-")
#print("Enberinin Argümanının (ω) katsayısının değerleri: ")
#print(*om_coefficient_values, sep="\n")
#print(60*"-")

#print(60*"*")
#print("Delta Vr Matrisi: ")
#print(deltav_matrix)
#print(60*"*")
#print(60*"*")
#print("Katsayılar Matrisi: ")
#print(coefficients_matrix)
#print(60*"*")
