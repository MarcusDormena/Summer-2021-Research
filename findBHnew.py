import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array

s=pynbody.load('/mnt/data0/jillian/h258/stampedetesting/glenna/take2/h258.cosmo50cmb.3072gst1bwdK1BH.000048')
h=s.halos()
s.physical_units()

#function to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of Black Holes is: ",len(BH))

#Function to find which halo (galaxy) the BH is in
def findBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos
BHhalos = findBHhalos(s)
print("Here are the Black Hole locations: ",BHhalos)
