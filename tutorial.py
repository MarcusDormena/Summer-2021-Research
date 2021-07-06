import matplotlib.pyplot as plt
import pynbody
import pylab
s = pynbody.load('/mnt/data0/jillian/testdata/g15784.lr.01024.gz')
h = s.halos()
h1 = h[1]
print('ngas = &e, ndark = %e, nstar = %e\n'%(len(h1.gas),len(h1.dark),len(h1.star)))
pynbody.analysis.halo.center(h1, mode='hyb')
print(h[1]['pos'][0])
print(h[5]['pos'][0])
h5 = h[5]
h5_transform = pynbody.analysis.halo.center(h5, mode='hyb', move_all=False)
print(h[1]['pos'][0])
print(h[5]['pos'][0])
h5_transform.revert()
print(h[5]['pos'][0])
print(h[1]['pos'][0])
with pynbody.analysis.halo.center(h[5], mode ='hyb'): print(h[5]['pos'][0])
print(h[5]['pos'][0])
s = pynbody.load('/mnt/data0/jillian/testdata/g15784.lr.01024.gz'); h1 = s.halos()[1];
cen_hyb = pynbody.analysis.halo.center(h1, mode = 'hyb', retcen=True)
cen_pot = pynbody.analysis.halo.center(h1, mode = 'pot', retcen=True)
print(cen_hyb)
print(cen_pot)
s['pos'] -= cen_hyb
s.physical_units()
pynbody.plot.image(h1.g, width = 100, cmap='Blues')
plt.show()
