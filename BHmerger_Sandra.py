import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

#Merger info for Merger # 1. It has no data:
#########Snapshots: '/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000107/h148.cosmo50PLK.3072g3HbwK1BH.000107','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000139/h148.cosmo50PLK.3072g3HbwK1BH.000139'
############  Primary: 101863741, Secondary: 101863762
#########     Mass ratio: 0.0391214

filenamelist = ['/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000974/h148.cosmo50PLK.3072g3HbwK1BH.000974','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.001024/h148.cosmo50PLK.3072g3HbwK1BH.001024','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.001408/h148.cosmo50PLK.3072g3HbwK1BH.001408','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.001740/h148.cosmo50PLK.3072g3HbwK1BH.001740','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.001740/h148.cosmo50PLK.3072g3HbwK1BH.001740','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.002048/h148.cosmo50PLK.3072g3HbwK1BH.002048','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.002688/h148.cosmo50PLK.3072g3HbwK1BH.002688','/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.002816/h148.cosmo50PLK.3072g3HbwK1BH.002816']

MassRatio_list = [0.00894852, 0.518367, 0.920125, 0.257822]

nfilenames = len(filenamelist)

BHiordlist = [101863565, 101863705, 101863741, 101863769, 101863510, 101863741, 101863565, 101863727]

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
    f = open("findBH.txt", "a")
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
         redshift = s.properties['z']
         data[0,i] = BH['iord'][i]
         data[1,i] = BHhalos[i]
         data[2,i] = distance[0]
         data[3,i] = starmass
         data[4,i] = redshift
         data[5,i] = MassRatio
         data[6,i] = BHMass
    #Data should be transposed here because I have 4 columns, not 4 rows                                                                                                       
    data=np.transpose(data)
    #Name each successive column, must be same number as you put for in data!
    df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass','Redshift','Mass Ratio'])
    df=df[df['Host Galaxy']!=0]
    df=str(df)
    print(df)
    f.write(df)
f.close()
