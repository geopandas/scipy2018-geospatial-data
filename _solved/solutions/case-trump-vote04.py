import seaborn as sns
facets = sns.pairplot(x_vars=pres.filter(like='dem_').columns,
                      y_vars=['gini_2015'], data=pres)