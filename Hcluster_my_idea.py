from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
import numpy as np
import sys

w = 4    
a = 20
lsh_limit = 6 # The number of indices to use for LSH
X = []
labels = []
with open('CM_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit), 'r') as f:
	data = f.read()
# Change this to sys.argv[1] in case you need to experiment with diferrent linkage methods
linkage_method='average'
X = np.fromstring(data, sep=' ')
X = np.subtract(X.max(), X)
# X = np.diff(X)
print(X.shape)
# np.set_printoptions(threshold=50000, suppress=True)
# print(X.shape)
# X = znorm(X)
with open('file_list_all','r') as f:
	labels = f.readlines()
# print(labels)
Z = linkage(X, linkage_method, optimal_ordering=True)

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Time-series index')
plt.ylabel('Collision frequency')
P = 15
clusters = fcluster(Z, P, criterion='maxclust')
new_labels=[]
for i in range(0,P):
	new_labels.append('')
# print(len(new_labels))
for i in range(0,57):
    index = clusters[i]-1
    new_labels[index] = new_labels[index]+labels[i]
with open ('Clusters/diff_nested_clusters_'+str(P)+'_'+linkage_method+'_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit), 'w') as f:
    for i in new_labels:
        f.write(i+'\n')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
    labels=labels,
    show_leaf_counts=True,	
    truncate_mode='lastp',
    p=P,
    show_contracted=True,
    # leaf_label_func=llf,
)
# a,b = plt.yticks()
# with open ('Clusters/clusters_'+linkage_method, 'w') as f:
# 	for i in b:
# 		f.write(str(i))
# 		f.write(' \n')
# k = 15

plt.savefig('Plots/dendrogram_last_'+str(P)+'_'+linkage_method+'_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit))
plt.show()