import matplotlib.pyplot as plt
import csv
import sys
import os
import numpy as np
from saxpy.znorm import znorm
import pandas as pd

# Assume a comma separated list of names are enterd as sys.argv[1]
files_to_plot = sys.argv[1].strip().split(',')
# print(files_to_plot)
counter=0
for i in files_to_plot:
	i=i.strip()
	os.system('cp ./DATA/'+i+'.NS.csv ./work_dir')
	data = pd.read_csv('./work_dir/'+i+'.NS.csv',  usecols=[1], header=None, dtype=float, skiprows=2, squeeze=True)
	data = data[:-1].copy()
	data = znorm(data)
	plt.plot(data, label=files_to_plot[counter])
	counter+=1
plt.legend()
plt.savefig('./Plots/Individual/znorm'+sys.argv[1])
plt.show()
