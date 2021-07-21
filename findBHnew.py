import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

newArray=[21,3]
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
print(BHhalos)
for i in range(len(BH)):
    if BHhalos[i] ==0:
        continue
    #print(BHhalos[i])
    pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
    x=BH['pos'][[i],0]
    y=BH['pos'][[i],1]
    z=BH['pos'][[i],2]
    distance = (x**2+y**2+z**2)**0.5
    data = BH['iord'][i], BHhalos[i], distance[0]
    print(data)

# BH?, BHhalos, distance 
#df2 = pd.DataFrame(data=newArray, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)'])
#print(df2)
#print(BH)

