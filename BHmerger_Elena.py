import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist = ['/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.000139/h329.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.000188/h329.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.000864/h329.cosmo50PLK.3072gst5HbwK1BH.000864','/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.000960/h329.cosmo50PLK.3072gst5HbwK1BH.000960','/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.001632/h329.cosmo50PLK.3072gst5HbwK1BH.001632','/mnt/data0/jillian/h329/h329.cosmo50PLK.3072gst5HbwK1BH.001740/h329.cosmo50PLK.3072gst5HbwK1BH.001740']

MassRatio_list = [0.34992, 0.00762192, 0.0163273]

nfilenames = len(filenamelist)

BHiordlist = [40810844, 40811189, 40810270, 40810454, 40810270, 40811872]

k=-2
#Function to find which halo (galaxy) the BH is in:     
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform', 0.0)
    BH = s.stars[BHfilter]
    return BH

def findBHhalos(s, BH):
    BHhalos = BH['amiga.grp']
    return BHhalos

for j in range(nfilenames):
    if j%2==0:
        k=k+2
        l = k//2
        MassRatio = MassRatio_list[l]
        print("                                                                                          Merger #", (2+k)//2)
        print("                                                                   Before Merger")
        print("Primary BH: ", BHiordlist[k])
        print("Secondary BH: ", BHiordlist[k+1])
        
    if j%2==1:
        print("")
        print("                                                                   After Merger")
        print("Merged BH: ", BHiordlist[k])

    s = pynbody.load(filenamelist[j])
    h=s.halos()
    s.physical_units()
    BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
    BH =  s.stars[BHfilter]
    BHhalos = findBHhalos(s, BH)
    
    #For data, the number before len is the number of columns you want
    data=np.zeros((7,len(BH)))
    #This will skip all of the "0" galaxies because the zeros will mess the code up                                                                                                 
    f = open("findBH_Elena.txt", "w")
    for i in range(len(BH)):
         if BHhalos[i] == 0:
             print("Skiping because Halo = 0")
             continue
         pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
         x=BH['pos'][[i],0]
         y=BH['pos'][[i],1]
         z=BH['pos'][[i],2]
         distance=((x**2+y**2+z**2)**0.5)
         starmass = h[BHhalos[i]].s['mass'].sum()
         print(starmass)
         redshift = s.properties['z']
         data[0,i] = BH['iord'][i]
         data[1,i] = BHhalos[i]
         data[2,i] = distance[0]
         data[3,i] = starmass
         data[4,i] = redshift
         data[5,i] = MassRatio
         data[6,i] = BH["mass"][i]
    #Data should be transposed here because I have 4 columns, not 4 rows                                                                                                       
    data=np.transpose(data)
    #Name each successive column, must be same number as you put for in data!
    df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass','Redshift','Mass Ratio', 'BH Mass'])
    df=df[df['Host Galaxy']!=0]
    df=str(df)
    print(df)
    f.write(df)
f.close()
