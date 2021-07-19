import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array

s=pynbody.load('/mnt/data0/jillian/h258/stampedetesting/glenna/take2/h258.cosmo50cmb.3072gst1bwdK1BH.000048')
h=s.halos()
s.physical_units

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
print("Here are the Black Hole locations:",BHhalos)

#This will find the distance BH is from galaxy center:
with pynbody.analysis.halo.center(h[4], mode='hyb'):
    print(h[4]['pos'][0])
    print(h[4]['pos'][1])
    print(h[4]['pos'][2])

print('pos')

#position of BH:
BHposition = BH['pos']
print("The Black Hole's position is", BHposition)

#To put x,y, and z values into columns:
BHx1 = BHposition[[0],0]
BHx2 = BHposition[[1],0]

BHy1 = BHposition[[0],1]
BHy2 = BHposition[[1],1]

BHz1 = BHposition[[0],2]
BHz2 = BHposition[[1],2]

#Distance formula for absolute magnitude
distance = ((BHx2-BHx1)**2+(BHy2-BHy1)**2+(BHz2-BHz1)**2)**0.5
print("The distance from the Black Hole and the Galaxy center is ", distance, "kiloparsecs.")

#Table with BH ID#, Host Galaxy, and Distance from Center
