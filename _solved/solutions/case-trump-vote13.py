pres.assign(local_score = lmos.Is, 
            pval = lmos.p_sim,
            quad = lmos.q)\
    .sort_values('local_score')\
    .query('pval < 1e-3 & local_score < 0')[['name','state_name','dem_2008','dem_2016',
                                             'local_score','pval', 'quad']]