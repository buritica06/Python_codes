etfs = sp500_px.loc[sp500_px.index > '2012-07-01',
 sp500_sym[sp500_sym['sector'] == 'etf']['symbol']]
sns.heatmap(etfs.corr(), vmin=-1, vmax=1,
 cmap=sns.diverging_palette(20, 220, as_cmap=True))