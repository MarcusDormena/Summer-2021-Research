import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225')
h=s.halos()
s.physical_units()
print(pynbody.analysis.cosmology.age(s),"Gyrs old")
print("Redshift:",s.properties['z'])
#function to find black holes:
def findBH(s):
    #BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BHfilter = np.where((s.stars['iord']==75289317)|(s.stars['iord']==75289686))
    #BHfilter = np.where((s.stars['iord']==75289317)|(s.stars['iord']==75289686))
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
