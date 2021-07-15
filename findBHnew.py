import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt

s=pynbody.load('/mnt/data0/jillian/h258/stampedetesting/glenna/take2/h258.cosmo50cmb.3072gst1bwdK1BH.000048')

s.physical_units()

#function to find black holes
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)
print(BH)

#To find the number of BH's
def findBH(s):
    BHfilter = np.where((s.stars['iord']==60352791)|
                        (s.stars['iord']==60354588))
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print("The number of Black Holes is: ",len(BH))

