import matplotlib.pyplot as plt
import csv
import sys
import numpy as np
from saxpy.znorm import znorm

np.set_printoptions(threshold=100000, suppress=True)
print(sys.argv[1].strip().split(','))
flag = ''
if sys.argv[1] != '' and sys.argv[1] != 'a':
	index_to_plot = np.array(sys.argv[1].strip().split(','))
	index_to_plot = index_to_plot.astype(int)
else:
	flag = 'a'
series = np.genfromtxt('open_prices', delimiter='\n', missing_values='null', filling_values=0)
all_series = np.asfarray(np.split(series, 57), float)
all_series = all_series[:,:-1] # removing the last element 'null' from all series (n=255-1=254)
for i in range(0,57):
	all_series[i] = znorm(all_series[i])
print(all_series)
with open('open_prices', 'r') as f:
	cur_index = 0
	# print(index_to_plot)
	counter = 0 # Used to iterate through the multiple TS indices that need to be plotted, passed as arguments
	# print(all_series)
	print(all_series.shape)
	if flag == 'a':
		for series in all_series:
			plt.plot(series, label=str(cur_index))
	else:
		for series in all_series:
			if counter < len(index_to_plot) and cur_index == index_to_plot[counter]:
				print(znorm(series))
				plt.plot(znorm(series))

				counter+=1
			cur_index+=1
# plt.legend()
plt.show()
