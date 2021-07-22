import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

data=[21,3]
s=pynbody.load('/mnt/data0/jillian/h258/stampedetesting/glenna/take2/h258.cosmo50cmb.3072gst1bwdK1BH.000048')
h=s.halos()
s.physical_units()

#function to find black holes:
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of Black Holes is",len(BH))

#Function to find which halo (galaxy) the BH is in:
def findBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos

BHhalos = findBHhalos(s)
print("These are the galaxies:", BHhalos)

#distance=np.zeros(len(BH))
#BHhalos_array=np.zeros(len(BH))
#BH_iord=np.zeros(len(BH))
data=np.zeros((3,len(BH)))
print(data.shape)
              
#This will skip all of the "0" galaxies because the zeros will mess the code up
for i in range(len(BH)):
    if BHhalos[i] ==0:
        continue
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
#Will print the successive galaxies's coordinates
    x=BH['pos'][[i],0]
    y=BH['pos'][[i],1]
    z=BH['pos'][[i],2]
    data[2][i] = ((x**2+y**2+z**2)**0.5)[0]
    data[0][i]= BH['iord'][i]
    data[1][i]=BHhalos[i]

    
data=np.transpose(data)
df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)'])
df=df[df['Host Galaxy']!=0]
print(df)


