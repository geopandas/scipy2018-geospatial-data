from pysal import esda as esda
np.random.seed(1)
moran = esda.moran.Moran(pres.swing_full, w)
print(moran.I)
