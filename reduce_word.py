#!/usr/bin/env python

from operator import itemgetter
import sys

current_doc = None
current_doc_key = 0
current_word = None
# read the entire line from STDIN
curr = 0. #(0, 1)  # doc _ count
docs = None
total_tf1=0.
total_tf2=0.

# docfile = open(
# 'hdfs://localhost:9000/user/hongphucvo/dictionary_map_1/part-00000')


for line in sys.stdin:
	# print(line)
	# remove leading and trailing whitespace
	# line = line.strip()
	# splitting the data on the basis of tab we have provided in mapper.py
	# this IF-switch only works because Hadoop sorts map output
	docs, idf = line.split('\t', 1)
	# convert count (currently a string) to int
	
	try:
		idf = float(idf)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	# print(docs)
	# this IF-switch only works because Hadoop sorts map output
	# by key (here: word) before it is passed to the reducer
	# print(total_tf1)
	if current_doc == docs:
		curr += idf
	else:
		if current_doc:
			# if curr[0]/curr[1] < 0.2:

			doc1, doc2 = current_doc.split('#', 1)
			doc1, total_tf1 = doc1.split('@', 1)
			doc2, total_tf2 = doc2.split('@', 1)

			total_tf1 = float(total_tf1)
			total_tf2 = float(total_tf2)
			print('%s~%s\t%f' %
				  (doc1,doc2, curr/(total_tf1+total_tf2-curr)))
		current_doc = docs
		curr = idf

if current_doc == docs:
	doc1, doc2 = current_doc.split('#', 1)
	doc1, total_tf1 = doc1.split('@', 1)
	doc2, total_tf2 = doc2.split('@', 1)

	total_tf1 = float(total_tf1)
	total_tf2 = float(total_tf2)
	print('%s~%s\t%f' % (doc1,doc2, curr/(total_tf1+total_tf2-curr)))


#high is gud