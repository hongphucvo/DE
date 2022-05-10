#!/usr/bin/env python

import sys

current_doc = None
# read the entire line from STDIN
curr = 0. 
doc = None
total_tf1=0.

# docfile = open(
# 'hdfs://localhost:9000/user/hongphucvo/dictionary_map_1/part-00000')


for line in sys.stdin:
	doc, idf = line.split('\t', 1)
	doc, total_tf1 = doc.split('@', 1)
	
	try:
		idf = float(idf)
		total_tf1 = float(total_tf1)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	if current_doc == doc:
		curr += idf
	else:
		if current_doc:
			# if curr[0]/curr[1] < 0.2: TODO
			# if curr>0.:
			print('%s\t%f' %
				(current_doc, curr))
		current_doc = doc
		curr = idf

if current_doc == doc:
	# if curr>0.:
	print('%s\t%f' %
		(current_doc, curr))
#high is gud