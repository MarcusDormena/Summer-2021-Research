import numpy as np
import pynbody
import matplotlib.pyplot as plt
from pynbody import filt, array
import pandas as pd

#filenamelist = ['/mnt/data0/jillian/h2((simulation #!))/h2((simulation #)).cosmo50PLK.3072gst5HbwK1BH.((Time Before Merger))/h2((simulation #)).cosmo50PLK.3072gst5HbwK1BH.((Time Before Merger))','/mnt/data0/jillian/h2((simulation #!))/h2((simulation #)).cosmo50PLK.3072gst5HbwK1BH.((Time After Merger))/h2((simulation #)).cosmo50PLK.3072gst5HbwK1BH.((Time After Merger))']

nfilenames = len(filenamelist)  # this is the number of mergers times 2. because each merger has 2 BH's

BHiordlist = []

n=0
k=0
    print(pynbody.analysis.cosmology.age(s),"Gyrs old")
    print("Redshift:",s.properties['z'])
        #For data, the number before len is the number of columns you want
    data=np.zeros((4,len(BH)))
    print(data.shape)
              
    #This will skip all of the "0" galaxies because the zeros will mess the code up
    f = open("findingBH.txt", "a")
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
