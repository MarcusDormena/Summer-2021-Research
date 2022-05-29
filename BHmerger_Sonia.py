import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

filenamelist_ruth =  ['/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000107/h229.cosmo50PLK.3072gst5HbwK1BH.000107','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000139/h229.cosmo50PLK.3072gst5HbwK1BH.000139','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000188/h229.cosmo50PLK.3072gst5HbwK1BH.000188','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000192/h229.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000225/h229.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000384/h229.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000456/h229.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000480/h229.cosmo50PLK.3072gst5HbwK1BH.000480','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000576/h229.cosmo50PLK.3072gst5HbwK1BH.000576','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000864/h229.cosmo50PLK.3072gst5HbwK1BH.000864','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.000960/h229.cosmo50PLK.3072gst5HbwK1BH.000960','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001056/h229.cosmo50PLK.3072gst5HbwK1BH.001056','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001106/h229.cosmo50PLK.3072gst5HbwK1BH.001106','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001824/h229.cosmo50PLK.3072gst5HbwK1BH.001824','/mnt/data0/jillian/h229/h229.cosmo50PLK.3072gst5HbwK1BH.001920/h229.cosmo50PLK.3072gst5HbwK1BH.001920']

filenamelist = ['/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000192/h242.cosmo50PLK.3072gst5HbwK1BH.000192','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000225/h242.cosmo50PLK.3072gst5HbwK1BH.000225','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000288/h242.cosmo50PLK.3072gst5HbwK1BH.000288','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000347/h242.cosmo50PLK.3072gst5HbwK1BH.000347','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000384/h242.cosmo50PLK.3072gst5HbwK1BH.000384','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000456/h242.cosmo50PLK.3072gst5HbwK1BH.000456','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000637/h242.cosmo50PLK.3072gst5HbwK1BH.000637','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.000672/h242.cosmo50PLK.3072gst5HbwK1BH.000672','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001269/h242.cosmo50PLK.3072gst5HbwK1BH.001269','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001344/h242.cosmo50PLK.3072gst5HbwK1BH.001344','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001536/h242.cosmo50PLK.3072gst5HbwK1BH.001536','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.001632/h242.cosmo50PLK.3072gst5HbwK1BH.001632','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002400/h242.cosmo50PLK.3072gst5HbwK1BH.002400','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002496/h242.cosmo50PLK.3072gst5HbwK1BH.002496','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002592/h242.cosmo50PLK.3072gst5HbwK1BH.002592','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.002688/h242.cosmo50PLK.3072gst5HbwK1BH.002688','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003840/h242.cosmo50PLK.3072gst5HbwK1BH.003840','/mnt/data0/jillian/h242/h242.cosmo50PLK.3072gst5HbwK1BH.003936/h242.cosmo50PLK.3072gst5HbwK1BH.003936']

nfilenames = len(filenamelist)  # this will be 24 when all the files are entered.
nfilenames_ruth = len(filenamelist_ruth) # should be 22  # delete this line later

BHiordlist = [75288848,75289477,75289317,75289686,75288553,75288848,75288614,75288740,75288565,75288831,75288505,75289109,75288553,75288953,75288553,75289347,75288614,75288843,75288505,75288553,75288505,75288614,75288505,75289317]

BHiordlist_ruth = [60352791, 60353219, 60352780, 60353758, 60352791, 60354626, 60352912, 60353166, 60352780, 60353759, 60352780, 60353024, 60352780, 60352867, 60352986, 60354630, 60352780, 60353760, 60352791, 60354588, 60352780, 60352912]

#name these ones after street fighter characters? Ryu, blanka, e. honda, ken, dhalsym, m. bison, guile, chun-li, 

n=0
k=0

#Function to find which halo (galaxy) the BH is in:     
#def findBHhalos(s):
#    BHhalos = BH['amiga.grp']
#    return BHhalos

#as long as j is between 0 and 23, print it
#for j in range(nfilenames):
#    if j%2==0 and j!=0:
#        k=k+2
#
#    print(" ")
#    print("Round ",n+1)    
#    print ("j = ",j)
#    print ("k = ",k)
#    n=n+1
#    s = pynbody.load(filenamelist[j])
#    h=s.halos()
#    s.physical_units()
#    print("BH #1 =", BHiordlist[k])
#    print("BH #2 =", BHiordlist[k+1])
#    BHfilter = np.where((s.stars['iord']==BHiordlist[k])|(s.stars['iord']==BHiordlist[k+1]))
#    BH =  s.stars[BHfilter]
#
#    BHhalos = findBHhalos(s)
#    
    #This is printing info about the j'th BH
#    print(pynbody.analysis.cosmology.age(s),"Gyrs old")
#    print("Redshift:",s.properties['z'])

    #For data, the number before len is the number of columns you want
#    data=np.zeros((4,len(BH)))
#    print(data.shape)

#######RUTH BABAYYYYY#####
def findBHhalos(s_ruth):
    BHhalos_ruth = BH_ruth['amiga.grp']
    return BHhalos_ruth

for j in range(nfilenames_ruth):
    if j%2==0 and j!=0:
        k=k+2

    print(" ")
    print("Round ",n+1)    
    print ("j = ",j)
    print ("k = ",k)
    n=n+1
    s_ruth = pynbody.load(filenamelist_ruth[j])
    h_ruth=s_ruth.halos()
    s_ruth.physical_units()
    print("BH #1 =", BHiordlist_ruth[k])
    print("BH #2 =", BHiordlist_ruth[k+1])
    BHfilter_ruth = np.where((s_ruth.stars['iord']==BHiordlist_ruth[k])|(s_ruth.stars['iord']==BHiordlist_ruth[k+1]))
    BH_ruth =  s_ruth.stars[BHfilter_ruth]

    BHhalos_ruth = findBHhalos(s_ruth)
    
    #This is printing info about the j'th BH
    print(pynbody.analysis.cosmology.age(s_ruth),"Gyrs old")
    print("Redshift:",s_ruth.properties['z'])

    #For data, the number before len is the number of columns you want
    data=np.zeros((4,len(BH_ruth)))
    print(data.shape)

    #This will skip all of the "0" galaxies because the zeros will mess the code up
    f = open("findingBH_NEW.txt", "a")
    print("len(BH_ruth) =",len(BH_ruth))
    for i in range(len(BH_ruth)):
         if BHhalos_ruth[i] ==0:
             continue
         print("Data:",data)
         pynbody.analysis.halo.center(h_ruth[BHhalos_ruth[i]], mode='hyb')
         x=BH_ruth['pos'][[i],0]
         y=BH_ruth['pos'][[i],1]
         z=BH_ruth['pos'][[i],2]
         distance=((x**2+y**2+z**2)**0.5)
         starmass_ruth = h_ruth[BHhalos_ruth[i]].s_ruth['mass'].sum()
         print("Starmass: ",starmass_ruth)
         print("x =",x)
         print("y =",y)
         print("z =",z)
         print("i =",i)
         print("Distance: ",distance)
         #Data format below is wrong! With the indexing
         data[0,i] = BH_ruth['iord'][i]
         data[1,i] = BHhalos_ruth[i]
         data[2,i] = distance[0]
         data[3,i] = starmass_ruth
     

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
