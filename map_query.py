#!/usr/bin/python
  
import sys
import os
filename = os.path.basename(os.getenv('map_input_file'))
folder=os.getenv('map_input_file')
def normalize(doc):
	quotes = ['.', ',', '-', '\'', '\"', '?','#','@']
	escape_seq = ['\n', '\t', '\r']

	for quote in quotes:
		doc = doc.replace(quote, " ")

	for esq in escape_seq:
		doc  = doc.replace(esq, " ")

	return doc

for line in sys.stdin:
	# to remove leading and trailing whitespace
	if filename=='query.txt' :
		line = normalize (line.strip())
	
	# split the line into words
		words = line.split()
		for word in words:
			print('%s\t%s' % (word,'0'))
	else:
		if line[0].isalpha():
			print(line)

