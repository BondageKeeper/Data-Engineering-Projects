figure , axis = plt.subplots(figsize=(10,6))
line_a = np.random.normal(200,5,200)
line_b = np.random.normal(200,15,200)
inaccuracy = np.array([100,110,290,300,270])
line_b_outcome = np.concatenate((line_b,inaccuracy)) #tuple
axis.grid(axis='x')
axis.boxplot([line_a,line_b_outcome],labels = ['Stable Production','Unstable Production'],patch_artist=True,showmeans=True,vert=True,boxprops=dict(color='violet'),flierprops=dict(markerfacecolor='red',markersize=5))
plt.tight_layout()
plt.show()
