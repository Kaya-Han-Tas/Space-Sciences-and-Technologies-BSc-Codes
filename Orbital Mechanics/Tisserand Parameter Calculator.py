import numpy as np
import math
ag=float(input("Gezegenin yorungesinin yari-buyuk eksen degerini giriniz (AB): "))
#semi-major axis of the object's orbit
a=2.66828
#eccentricity of the object's orbit
e=0.25693
#orbit's inclination in radians
i=0.22674
sqrt=(a/ag)*(1-pow(e,2))*np.cos(i)
prop=ag/a
Tg=prop+(2*math.sqrt(sqrt))
print("Gezegeninizin Tisserand Parametresi: ",Tg)