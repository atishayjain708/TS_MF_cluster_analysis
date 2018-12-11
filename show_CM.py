# n = 255
# Using no. of alphabets = 20 and w = 8
# For w = 8, k = 2 and 20 alphabet, min index (aa) = 194
# and maximum index (tt) = 232. Therefore we create a matrix 
# where aa maps to (0,0); i.e. hash function subtracts 194 
# from sum of chars to get hashing index
# Max possible buckets (with 20 alpahbets) = 400
# No rotation invariance in case of stocks
import csv
import sys
import math
import numpy as np
import saxpy.discord as discord
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize
from itertools import permutations
np.set_printoptions(threshold=50000, suppress=True)
# m is the number of shapes in dataset
n = 255		  # Lengtth of time-series	
m = 57		  # The number of time series		
lsh_limit = 6 # The number of indices to use for LSH
w = 4
a = 20
max_possible_buckets = lsh_limit*a
sax_words = []
visited = set() 	# Set to store what all buckets have been used; saves time;
sax_words_ri = []	# Read from sax_words_ri_all_Lshifts into sax_words_ri

with open('sax_words_ri_norot_w='+str(w)+'_a='+str(a), 'r') as sax_words_file:
	data = sax_words_file.read().split()
	for i in data:
		sax_words_ri.append(i.strip())
# print(sax_words_ri)

# Assumes a 2 letter string only; Hard-coded;
# Also updates the visited array every time it's called
def get_hash(word, num_indices):
	n=0
	for i in range(num_indices): 
		n=n+ord(word[i])
	h = n-num_indices*97
	visited.add(h)
	return h

CM = np.zeros((m,m), dtype=int)
# instead of while true, run for 30 times
lsh_counter = 100
while lsh_counter > 0:
	bucket_list = []
	for i in range(max_possible_buckets):
		bucket_list.append([0] * 1)
	lsh_indices = np.random.random_integers(0,w-1,lsh_limit)
	time_series_num = -1
	for word in sax_words_ri:
		time_series_num+=1
		word_to_hash = '' # word_to_hash is the word formed after taking letters at lsh_indices from a sax word
		for i in range(0,lsh_limit):
			word_to_hash = word_to_hash+word[lsh_indices[i]]
		bucket_list[get_hash(word_to_hash, lsh_limit)].append(time_series_num)
	# print(bucket_list)
	# All words have been put into buckets. Now checking if there are collisions and updating CM.
	# print(len(visited))
	# print(visited)
	for idx in visited:
		for i in bucket_list[idx]:
			for j in bucket_list[idx]:
				if i != j:
					CM[i][j]+=1;
	lsh_counter-=1

with open('CM_w='+str(w)+'_a='+str(a)+'_lsh_limit='+str(lsh_limit),'w') as f:
	for i in range(0,m):
		for j in range(0,m):
			if j < i:
				f.write(str(CM[i][j])+' ')
		f.write('\n')