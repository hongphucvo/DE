#!/usr/bin/env python

import sys

current_docs = None
# read the entire line from STDIN
curr = 0. 
docs = None
total_tf1=0.

# docfile = open(
# 'hdfs://localhost:9000/user/hongphucvo/dictionary_map_1/part-00000')


for line in sys.stdin:
	docs, idf = line.split('\t', 1)
	try:
		idf = float(idf)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	if current_docs == docs:
		curr += idf
	else:
		if current_docs:
			# if curr[0]/curr[1] < 0.2: TODO
			# if curr>0.:

			doc, total_tf1 = current_docs.split('@', 1)
			total_tf1 = float(total_tf1)
			print('%s\t%f' %
				(doc, curr/total_tf1*100))
		current_docs = docs
		curr = idf

if current_docs == docs:
	# if curr>0.:
	doc, total_tf1 = current_docs.split('@', 1)
	total_tf1 = float(total_tf1)
	print('%s\t%f' %
				(doc, curr/total_tf1*100))
#high is gud