#!/usr/bin/env python

from math import log
from operator import itemgetter
import sys
import os

current_doc = None
current_word = None
word = None
doc = None
cur = [(doc, 1.)]


# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# print(line)
	doc, word = line.split('\t', 1)
	word, count = word.split('=', 1)
# convert count (currently a string) to int
	try:
		count = float(count)
	except ValueError:
		continue

	if current_doc == doc:
		cur += [(word, count)]
	else:
		# tf calculating
		if current_doc:
			sizeN = sum(wordcount[1] for wordcount in cur)
			# print(sizeN)
			for w, c in cur:
				print('%s#%s\t%f' % (w, current_doc,float(c/sizeN)))
		current_doc = doc
		current_word = word
		cur = [(word, count )]
if current_doc == doc:
	sizeN = sum(wordcount[1] for wordcount in cur)#len(cur)
	for w, c in cur:
		print('%s#%s\t%f' % (w, current_doc,float(c/sizeN)))
