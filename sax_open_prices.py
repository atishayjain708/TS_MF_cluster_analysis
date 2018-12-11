# n = 251
# Using no. of alphabets = 20 and w = 4
import sys
import csv
import numpy as np
import saxpy.discord as discord
from saxpy.znorm import znorm
from saxpy.paa import paa
from saxpy.sax import ts_to_string
from saxpy.alphabet import cuts_for_asize

from itertools import permutations
from collections import defaultdict

sax_words = []
w = 4
a = 20
with open(sys.argv[1], 'r') as h:
	lines = h.readlines()
	DATA = []
	time_series = []
	for line in lines:
		line = line.strip()
		if line != 'null' and line != '\n':
			time_series.append(float(line))
		else : 
			DATA.append(time_series)
			time_series = []
	for data in DATA:
		data = np.asfarray(data, float)
		data = np.diff(data)
		data_znorm = znorm(data)
		data_paa = paa (data_znorm, w)
		sax_words.append(ts_to_string(data_paa, cuts_for_asize(a)))


# sax_words_ri = []
# i = 0
# for word in sax_words:
# 	perms = set([''.join(p) for p in permutations(word)])
# 	sax_words_ri.append(perms)
# 	i+=1

#Write all SAX words to file only once instead of generating again and again
with open('sax_words_ri_norot_w='+str(w)+'_a='+str(a), 'w+') as sax_words_file:
		for l in sax_words: 
			sax_words_file.write(l+'\n')
		# sax_words_file.write('\n')