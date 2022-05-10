#!/usr/bin/env python

import sys

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	word, doc = line.split('#', 1)
	doc, freq = doc.split('\t', 1)
# convert count (currently a string) to int
	try:
		freq = float(freq)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	print('%s\t%s#%f' % (word,doc,freq))
