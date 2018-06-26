f = plt.figure(figsize=(10,4))
ax = plt.gca()
ax.set_aspect('equal')
is_weird = lmos.p_sim <= (.05/len(pres))
pres.plot(color='lightgrey', ax=ax)
pres.assign(quads=lmos.q)[is_weird].plot('quads', 
                                         legend=True, 
                                         k=4, categorical=True,
                                         cmap='bwr_r', ax=ax)