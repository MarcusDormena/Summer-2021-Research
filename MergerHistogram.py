from os import name 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df = pd.read_csv("./Desktop/NoFIrstColumn.csv")
print(df)

#import matplotlib.pyplot as plt
tickvalues = range(0,12)
plt.hist(df, bins = 20, color='b')

plt.xlabel("Merger")
y=np.arange(0,40)
plt.ylabel("Distance (kpc)")

plt.title("Distance from Galaxy Centers")
plt.xticks(range(1,11))
plt.show()
