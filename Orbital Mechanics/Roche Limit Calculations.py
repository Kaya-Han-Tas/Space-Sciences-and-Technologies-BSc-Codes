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
#Density of the Sun
rho_sun=1408 #km m^-3
#Density of Neptune
rho_nep=1638 #km m^-3
#Radius of the Sun
R=696340
#Roche Limit with Density
roche=2.423*R*(rho_sun/rho_nep)**(1/3)
print("Roche Limiti (Yoğunluk): ",roche, "km")
#Minimum period calculation (in seconds unit)
Tmin=math.sqrt(pow(roche,3)*((4*pow(math.pi,2))/GM))
print("Minimum periyot değeri (saniye cinsinden): ",Tmin, "saniye")
#Minimum period in days and years unit
Tmin=Tmin/(60*60*24)
print("Minimum periyot değeri (gün cinsinden): ", Tmin, "gün")
Tmin=Tmin/365
print("Minimum periyot değeri (yıl cinsinden): ", Tmin, "yıl")
print(60*"-")
#Roche Limit with Mass calculations
roche=r*((3*M/m)**(1/3))
print("Roche Limiti (Kütle): ",roche, "km")
#Minimum period calculation (in seconds unit)
Tmin=math.sqrt(pow(roche,3)*((4*pow(math.pi,2))/GM))
print("Minimum periyot değeri (saniye cinsinden): ",Tmin, "saniye")
#Minimum period in days and years unit
Tmin=Tmin/(60*60*24)
print("Minimum periyot değeri (gün cinsinden): ", Tmin, "gün")
Tmin=Tmin/365
print("Minimum periyot değeri (yıl cinsinden): ", Tmin, "yıl")
print(60*"-")