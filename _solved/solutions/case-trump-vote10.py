np.random.seed(11)
lmos = esda.moran.Moran_Local(pres.swing_full, w, 
                              permutations=70000) #min for a bonf. bound
(lmos.p_sim <= (.05/len(pres))).sum()