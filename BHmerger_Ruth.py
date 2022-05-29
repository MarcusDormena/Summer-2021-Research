import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist =  ['/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000384/h229.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000456/h229.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000480/h229.cosmo50PLK.3072gst5HbwK1BH.000480','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000576/h229.cosmo50PLK.3072gst5HbwK1BH.000576','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000864/h229.cosmo50PLK.3072gst5HbwK1BH.000864','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000960/h229.cosmo50PLK.3072gst5HbwK1BH.000960','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001056/h229.cosmo50PLK.3072gst5HbwK1BH.001056','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001106/h229.cosmo50PLK.3072gst5HbwK1BH.001106','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001824/h229.cosmo50PLK.3072gst5HbwK1BH.001824','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001920/h229.cosmo50PLK.3072gst5HbwK1BH.001920']


nfilenames = len(filenamelist) # should be 22

BHiordlist = [60352791, 60353219, 60352780, 60353758, 60352791, 60354626, 60352912, 60353166, 60352780, 60353759, 60352780, 60353024, 60352780, 60352867, 60352986, 60354630, 60352780, 60353760, 60352791, 60354588, 60352780, 60352912]

#name these ones after street fighter characters? Ryu, blanka, e. honda, ken, dhalsym, m. bison, guile, chun-li, 

n=0
k=0

def findBHhalos(s):
    BHhalos = BH['amiga.grp']
    return BHhalos

for j in range(nfilenames):
    if j%2==0 and j!=0:
        k=k+2

    print(" ")
    print("Round ",n+1)    
    print ("j = ",j)
    print ("k = ",k)
    n=n+1
    s = pynbody.load(filenamelist[j])
    h=s.halos()
    s.physical_units()
    print("BH #1 =", BHiordlist[k])
    print("BH #2 =", BHiordlist[k+1])
    BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
    BH =  s.stars[BHfilter]

    BHhalos_ruth = findBHhalos(s_ruth)
    
    #This is printing info about the j'th BH
    print(pynbody.analysis.cosmology.age(s),"Gyrs old")
    print("Redshift:",s.properties['z'])

    #For data, the number before len is the number of columns you want
    data=np.zeros((4,len(BH)))
    print(data.shape)

    #This will skip all of the "0" galaxies because the zeros will mess the code up
    f = open("findingBH_NEW.txt", "a")
    print("len(BH) =",len(BH))
    for i in range(len(BH)):
         if BHhalos[i] ==0:
             continue
         print("Data:",data)
         pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
         x=BH['pos'][[i],0]
         y=BH['pos'][[i],1]
         z=BH['pos'][[i],2]
         distance=((x**2+y**2+z**2)**0.5)
         starmass = h[BHhalos[i]].s['mass'].sum()
         print("Starmass: ",starmass)
         print("x =",x)
         print("y =",y)
         print("z =",z)
         print("i =",i)
         print("Distance: ",distance)
         #Data format below is wrong! With the indexing
         data[0,i] = BH['iord'][i]
         data[1,i] = BHhalos[i]
         data[2,i] = distance[0]
         data[3,i] = starmass

        #Name each successive column, must be same number as you put for in data!
    print("Data =",data)
    data=np.transpose(data)
    print("Data =",data)
    #Data should be transposed here because I have 4 columns, not 4 rows
    df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass'])
    df=df[df['Host Galaxy']!=0]
    df=str(df)
    print(df)
    f.write(df)
f.close()
