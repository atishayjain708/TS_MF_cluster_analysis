import matplotlib.pyplot as plt
import csv
import sys
import numpy as np
from saxpy.znorm import znorm

# Prepare the time-series data for plotting
series = np.genfromtxt('open_prices', delimiter='\n', missing_values='null', filling_values=0)
all_series = np.asfarray(np.split(series, 57), float)

P=15
w = 4 
a = 20
lsh_limit=6
linkage_method = 'average'
# linkage_method = sys.argv[1]
cur_index = 0
counter = 0 # Used to iterate through the multiple TS indices that need to be plotted, passed as arguments

index_to_plot = np.genfromtxt('to_plot_'+str(P)+'_'+linkage_method+'_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit), delimiter='\n', missing_values='', filling_values='-9999', dtype=int)

# Adjust indices in to_plot to become 0-indexed
for i in range(0,len(index_to_plot)):
	index_to_plot[i]-=1

# Prepare labels
with open('file_list_all','r') as f:
	labels = f.readlines()

# Set up for plotting
fig, ax = plt.subplots(5, 3)
plotcounter=1
to_plot=[]
to_label_legend=[]
fig = plt.figure(figsize=(25, 10))

for i in range(0,len(index_to_plot)):
	if index_to_plot[i] != -100: #-100 because after adjustment to make 0-indexed, -99 becomes -100
		to_plot.append(index_to_plot[i])
		# print(index_to_plot[i])
		to_label_legend.append(labels[index_to_plot[i]])
	else:
		fig.add_subplot(5,3,plotcounter)
		for series in all_series:
			if counter < len(to_plot) and cur_index == to_plot[counter]:
				# print(series)
				# print(znorm(series))
				plt.plot(znorm(series[:-1]))
				counter+=1
			cur_index+=1
		cur_index = 0
		plt.legend(to_label_legend, fontsize=5)
		# plt.title('Plot '+str(plotcounter))
		counter=0
		plotcounter+=1
		to_plot=[]
		to_label_legend=[]

plt.savefig('Plots/diff_znorm_comparison_nested_'+str(P)+'_'+linkage_method+'_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit))
plt.show()
