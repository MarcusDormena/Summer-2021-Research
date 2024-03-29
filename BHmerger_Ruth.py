import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist =  ['/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000384/h229.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000456/h229.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000480/h229.cosmo50PLK.3072gst5HbwK1BH.000480','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000576/h229.cosmo50PLK.3072gst5HbwK1BH.000576','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000864/h229.cosmo50PLK.3072gst5HbwK1BH.000864','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000960/h229.cosmo50PLK.3072gst5HbwK1BH.000960','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001056/h229.cosmo50PLK.3072gst5HbwK1BH.001056','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001106/h229.cosmo50PLK.3072gst5HbwK1BH.001106','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001824/h229.cosmo50PLK.3072gst5HbwK1BH.001824','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001920/h229.cosmo50PLK.3072gst5HbwK1BH.001920']

MassRatio_list = [0.191031,0.0216442,0.291805,0.728774,0.0210938,0.854044,0.449772,0.478513,0.00651045,0.679589,0.457031]

nfilenames = len(filenamelist)

BHiordlist = [60352791, 60353219, 60352780, 60353758, 60352791, 60354626, 60352912, 60353166, 60352780, 60353759, 60352780, 60353024, 60352780, 60352867, 60352986, 60354630, 60352780, 60353760, 60352791, 60354588, 60352780, 60352912]
#These are the BH Codenames
#2791 = Ryu
#3219 = Ken
#2780 = Akuma
#3758 = Blanka
#4626 = Chun-Li
#2912 = Guile
#3166 = Dhalsim
#3759 = E. Honda
#3024 = M. Bison
#2867 = Dan
#2986 = Gouken
#4630 = Cammy
#3760 = Juri
#4588 = Fang

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
    f = open("findBH_Ruth.txt", "w")
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
