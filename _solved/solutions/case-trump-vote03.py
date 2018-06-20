import seaborn as sns
facets = sns.pairplot(data=pres.filter(like='dem_'))
facets.map_offdiag(lambda *arg, **kw: plt.plot((0,1),(0,1), color='k'))