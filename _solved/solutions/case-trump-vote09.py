f = plt.figure(figsize=(6,6))
plt.scatter(pres.swing_full, lp.weights.lag_spatial(w, pres.swing_full))
plt.plot((-.3,.1),(-.3,.1), color='k')
plt.title('$I = {:.3f} \ \ (p < {:.3f})$'.format(moran.I,moran.p_sim))