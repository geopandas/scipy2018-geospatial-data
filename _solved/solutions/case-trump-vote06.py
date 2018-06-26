f,ax = plt.subplots(3,1,
                    subplot_kw=dict(aspect='equal', 
                                    frameon=False),
                    figsize=(60,15))
pres.plot('dem_2008', ax=ax[0], cmap='RdYlBu')
pres.plot('swing_full', ax=ax[1], cmap='bwr_r')
pres.plot('dem_2016', ax=ax[2], cmap='RdYlBu')
for i,ax_ in enumerate(ax):
    ax_.set_xticks([])
    ax_.set_yticks([])