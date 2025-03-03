import math
#Mass of the Sun
M=1.989E30 #kg
#Mass of Neptune
m=1.024E26 #kg
#GM value for Neptune
GM=6834257.92 #km^3 sn^-2
#Semi-major axis of Neptune's orbit
a=4495060000 #km
#Radius of Neptune
r=24622 #km
#Hill Sphere's radius
r_hill=a*pow((m/(3*M)),(1/3))
print(60*"-")
print("Hill küresinin yarıçapı: ",r_hill, "km")
#Maximum period calculation (in seconds unit)
Tmax=math.sqrt(pow(r_hill,3)*((4*pow(math.pi,2))/GM))
print("Maksimum periyot değeri (saniye cinsinden): ",Tmax, "saniye")
#Maximum period in days and years unit
Tmax=Tmax/(60*60*24)
print("Maksimum periyot değeri (gün cinsinden): ", Tmax, "gün")
Tmax=Tmax/365
print("Maksimum periyot değeri (yıl cinsinden): ", Tmax, "yıl")
print(60*"*")
print(60*"*")
#Roche Limit
roche=r*((3*M/m)**(1/3))
print("Roche Limiti: ",roche, "km")
#Minimum period calculation (in seconds unit)
Tmin=math.sqrt(pow(roche,3)*((4*pow(math.pi,2))/GM))
print("Minimum periyot değeri (saniye cinsinden): ",Tmin, "saniye")
#Minimum period in days and years unit
Tmin=Tmin/(60*60*24)
print("Minimum periyot değeri (gün cinsinden): ", Tmin, "gün")
Tmin=Tmin/365
print("Minimum periyot değeri (yıl cinsinden): ", Tmin, "yıl")
print(60*"-")
print(roche*(3*M/m)**(1/3))