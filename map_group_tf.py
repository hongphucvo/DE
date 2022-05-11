#!/usr/bin/env python

import sys


# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	doc, word = line.split('#', 1)
	word, tf = word.split('\t', 1)
# convert count (currently a string) to int
	try:
		tf = float(tf)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue
	print('%s\t%s#%f' % (word,doc,tf))
