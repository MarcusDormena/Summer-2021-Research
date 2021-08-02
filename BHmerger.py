import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

#Mergers 1 and 2
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225')

#Mergers 3 and 4
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347')

#Merger 5
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000384/h242.cosmo50PLK.3072gst5HbwK1BH.000384')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000456/h242.cosmo50PLK.3072gst5HbwK1BH.000456')

#Merger 6
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000637/h242.cosmo50PLK.3072gst5HbwK1BH.000637')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000672/h242.cosmo50PLK.3072gst5HbwK1BH.000672')

#Merger 7
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001269/h242.cosmo50PLK.3072gst5HbwK1BH.001269')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001344/h242.cosmo50PLK.3072gst5HbwK1BH.001344')

#Merger 8
s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001536/h242.cosmo50PLK.3072gst5HbwK1BH.001536')


h=s.halos()
s.physical_units()
print(pynbody.analysis.cosmology.age(s),"Gyrs old")
print("Redshift:",s.properties['z'])
#function to find black holes:
def findBH(s):
    #BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BHfilter = np.where((s.stars['iord']==75288553)|(s.stars['iord']==75289347))
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
#print("The number of Black Holes is",len(BH))

#Function to find which halo (galaxy) the BH is in:
def findBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos

BHhalos = findBHhalos(s)
#print("These are the galaxies:", BHhalos)

#distance=np.zeros(len(BH))
#BHhalos_array=np.zeros(len(BH))
#BH_iord=np.zeros(len(BH))
#For data, the number before len is the number of columns you want
data=np.zeros((4,len(BH)))
#print(data.shape)
              
#This will skip all of the "0" galaxies because the zeros will mess the code up
f = open("findingBH.txt", "a")
for i in range(len(BH)):
    if BHhalos[i] ==0:
        continue
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
    x=BH['pos'][[i],0]
    y=BH['pos'][[i],1]
    z=BH['pos'][[i],2]
    starmass = h[BHhalos[i]].s['mass'].sum()
    data[0][i] = BH['iord'][i]
    data[1][i] = BHhalos[i]
    data[2][i] = ((x**2+y**2+z**2)**0.5)[0]
    data[3][i] = starmass
data=np.transpose(data)
df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass'])
df=df[df['Host Galaxy']!=0]
df=str(df)
print(df)
f.write(df)
f.close()
