import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist = ['/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000384/h242.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000456/h242.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000637/h242.cosmo50PLK.3072gst5HbwK1BH.000637','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000672/h242.cosmo50PLK.3072gst5HbwK1BH.000672','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001269/h242.cosmo50PLK.3072gst5HbwK1BH.001269','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001344/h242.cosmo50PLK.3072gst5HbwK1BH.001344','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001536/h242.cosmo50PLK.3072gst5HbwK1BH.001536','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001632/h242.cosmo50PLK.3072gst5HbwK1BH.001632','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002400/h242.cosmo50PLK.3072gst5HbwK1BH.002400','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002496/h242.cosmo50PLK.3072gst5HbwK1BH.002496','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003840/h242.cosmo50PLK.3072gst5HbwK1BH.003840','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003936/h242.cosmo50PLK.3072gst5HbwK1BH.003936']

nfilenames = len(filenamelist)
BHiordlist = [75288848,75289477,75289317,75289686,75288553,75288848,75288614,75288740,75288565,75288831,75288505,75289109,75288553,75288953,75288553,75289347,75288614,75288843,75288505,75288553,75288505,75288614,75288505,75289317]

k=-2
#Function to find which halo (galaxy) the BH is in:     
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    return BH

def findBHhalos(s, BH):
    BHhalos = BH['amiga.grp']
    return BHhalos

for j in range(nfilenames):
    if j%2==0:
        k=k+2
        print("                                                                                       Merger #", (2+k)/2)
        print("                                                                   Before Merger")
        print(" ")
        print("Primary BH: ", BHiordlist[k])
        print("Secondary BH: ", BHiordlist[k+1])
        
    if j%2==1:
        print("                                                                   After Merger")
        print(" ")
        print("Merged BH: ", BHiordlist[k])

    s = pynbody.load(filenamelist[j])
    h=s.halos()
    s.physical_units()
    BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
    BH =  s.stars[BHfilter]
    BHhalos = findBHhalos(s, BH)
    #For data, the number before len is the number of columns you want
    data=np.zeros((5,len(BH)))
    #This will skip all of the "0" galaxies because the zeros will mess the code up                                                                                                 
    f = open("findBH.txt", "a")
    for i in range(len(BH)):
         if BHhalos[i] == 0:
             continue
         pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
         x=BH['pos'][[i],0]
         y=BH['pos'][[i],1]
         z=BH['pos'][[i],2]
         distance=((x**2+y**2+z**2)**0.5)
         starmass = h[BHhalos[i]].s['mass'].sum()
         redshift = s.properties['z']
#         mass ratio = 

         data[0,i] = BH['iord'][i]
         data[1,i] = BHhalos[i]
         data[2,i] = distance[0]
         data[3,i] = starmass
         data[4,i] = redshift
#         data[5,i] = mass ratio         
    #Data should be transposed here because I have 4 columns, not 4 rows                                                                                                            
    data=np.transpose(data)
    #Name each successive column, must be same number as you put for in data!
    df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass'])
    df=df[df['Host Galaxy']!=0]
    df=str(df)
    print(df)
    f.write(df)
f.close()
