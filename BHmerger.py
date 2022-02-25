import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist = ['/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000384/h242.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000456/h242.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000637/h242.cosmo50PLK.3072gst5HbwK1BH.000637','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000672/h242.cosmo50PLK.3072gst5HbwK1BH.000672','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001269/h242.cosmo50PLK.3072gst5HbwK1BH.001269','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001344/h242.cosmo50PLK.3072gst5HbwK1BH.001344','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001536/h242.cosmo50PLK.3072gst5HbwK1BH.001536','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001632/h242.cosmo50PLK.3072gst5HbwK1BH.001632','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002400/h242.cosmo50PLK.3072gst5HbwK1BH.002400','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002496/h242.cosmo50PLK.3072gst5HbwK1BH.002496','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003840/h242.cosmo50PLK.3072gst5HbwK1BH.003840','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003936/h242.cosmo50PLK.3072gst5HbwK1BH.003936']

nfilenames = len(filenamelist)  # this will be 24 when all the files are entered.
#nfilenames = 24  # delete this line later

BHiordlist = [75288848,75289477,75289317,75289686,75288553,75288848,75288614,75288740,75288565,75288831,75288505,75289109,75288553,75288953,75288553,75289347,75288614,75288843,75288505,75288553,75288505,75288614,75288505,75289317]

#For mergers, adjust snapshot times twice, after you see bwK1BH."blah". That's where you adjust the times

#Mergers 1 and 2
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225')

#Mergers 3 and 4
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347')

#Merger 5
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000384/h242.cosmo50PLK.3072gst5HbwK1BH.000384')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000456/h242.cosmo50PLK.3072gst5HbwK1BH.000456')

#Merger 6
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000637/h242.cosmo50PLK.3072gst5HbwK1BH.000637')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000672/h242.cosmo50PLK.3072gst5HbwK1BH.000672')

#Merger 7
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001269/h242.cosmo50PLK.3072gst5HbwK1BH.001269')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001344/h242.cosmo50PLK.3072gst5HbwK1BH.001344')

#Merger 8
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001536/h242.cosmo50PLK.3072gst5HbwK1BH.001536')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001632/h242.cosmo50PLK.3072gst5HbwK1BH.001632')

#Merger 9
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002400/h242.cosmo50PLK.3072gst5HbwK1BH.002400')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002496/h242.cosmo50PLK.3072gst5HbwK1BH.002496')

#Merger 10
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688')

#Merger 11
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688')

#Merger 12
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003840/h242.cosmo50PLK.3072gst5HbwK1BH.003840')
#s=pynbody.load('/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003936/h242.cosmo50PLK.3072gst5HbwK1BH.003936')

#h=s.halos()
#s.physical_units()
#print(pynbody.analysis.cosmology.age(s),"Gyrs old")
#print("Redshift:",s.properties['z'])

#function to find black holes:
#def findBH(s):
    #BHfilter = pynbody.filt.LowPass('tform', 0.0)

###############################################################################    
#############j is just the counter, k is the more massive BH ID################
###############################################################################

n=0
k=0

#Function to find which halo (galaxy) the BH is in:     
def findBHhalos(s):
     BHhalos = BH['amiga.grp']
     return BHhalos
     BHhalos = findBHhalos(s)
 
#as long as j is between 0 and 23, print it
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

#This is printing info about the j'th BH
    print(pynbody.analysis.cosmology.age(s),"Gyrs old")
    print("Redshift:",s.properties['z'])

#[iord]== "blah" is where you add the BH ID #, put more massive BH first    

     BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
     BH =  s.stars[BHfilter]

#int i = 0
#for (i<13):
#    i = i+1
#    print BH[i]

#    return BH
#BH = findBH(s)
#print("The number of Black Holes is",len(BH))
#print("These are the galaxies:", BHhalos)

#distance=np.zeros(len(BH))
#BHhalos_array=np.zeros(len(BH))
#BH_iord=np.zeros(len(BH))

#print(len(BH))

#For data, the number before len is the number of columns you want
     data=np.zeros((4,len(BH)))
#print(data.shape)
              
#This will skip all of the "0" galaxies because the zeros will mess the code up
     f = open("findingBH.txt", "a")
     for i in range(len(BH)):
         if BHhalos[i] ==0:
             continue
         pynbody.analysis.halo.center(h[BHhalos[i]], mode='hyb')
         x=BH['pos'][[i],0]
         y=BH['pos'][[i],1]
         z=BH['pos'][[i],2]
         starmass = h[BHhalos[i]].s['mass'].sum()
         data[0][i] = BH['iord'][i]
         data[1][i] = BHhalos[i]
         data[2][i] = ((x**2+y**2+z**2)**0.5)[0]
         data[3][i] = starmass
     data=np.transpose(data)

#Name each successive column, must be same number as you put for in data!
     df = pd.DataFrame(data=data, columns=['Black Hole ID#','Host Galaxy','Distance (kpc)', 'Total Stellar Mass'])
     df=df[df['Host Galaxy']!=0]
     df=str(df)
     print(df)
     f.write(df)
f.close()
