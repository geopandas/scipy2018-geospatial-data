np.random.seed(21)
lmos16 = esda.moran.Moran_Local(pres.swing_2016, w, 
                              permutations=70000) #min for a bonf. bound
(lmos16.p_sim <= (.05/len(pres))).sum()
pres.assign(local_score = lmos16.Is, 
            pval = lmos16.p_sim,
            quad = lmos16.q)\
    .sort_values('local_score')\
    .query('pval < 1e-3 & local_score < 0')[['name','state_name','dem_2008','dem_2016',
                                             'local_score','pval', 'quad']]