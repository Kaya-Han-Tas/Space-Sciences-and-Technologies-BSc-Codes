from astropy.io import fits
from pylab import *
table=fits.open('D:\\UBT\\Astrometri\\Final ödevi\\Fits dosyası + çözümler\\6567_0054_R_corr.fits')[1].data
image=fits.open('D:\\UBT\\Astrometri\\Final ödevi\\Fits dosyası + çözümler\\6567_0054_R_new-image.fits')[0].data

RMSerror= sqrt(mean((table.index_x-table.field_x)**2+(table.index_y-table.field_y)**2))
print('RMSerror =', RMSerror, 'pixel') #pixel

pixelscale=0.618 #arcsec/pixel
print('Pixel Scale (astrometry.net) =', pixelscale, "arcsec/pixel")

RMS=RMSerror*pixelscale
print('RMS =', RMS, '"')