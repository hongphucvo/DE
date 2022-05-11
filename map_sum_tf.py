#!/usr/bin/env python

import sys


# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	word, doc = line.split('#', 1)
	doc, tf = doc.split('\t', 1)
# convert count (currently a string) to int
	try:
		tf = float(tf)
	except ValueError:
		continue
	print('%s\t%s#%f' % (doc,word,tf))
