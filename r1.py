#!/usr/bin/env python

import sys
current_doc = None
current_word = None
current_count = 0
word = None
doc = None

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # print(line)
    # splitting the data on the basis of tab we have provided in mapper.py

    word,doc = line.split('\t', 1)

# this IF-switch only works because Hadoop sorts map output
# by key (here: word) before it is passed to the reducer
    if current_doc == doc:
        if current_word == word:
            current_count+=1
        else:
            print('%s#%s\t%s' % (current_word, current_doc, current_count))
            current_word = word
            current_count=1
    else:
        # tf calculating
        if current_doc:
            print('%s#%s\t%s' % (current_word, current_doc, current_count))
        current_doc = doc
        current_word = word
        current_count = 1
# do not forget to output the last word if needed!
if current_doc == doc:
    print('%s#%s\t%s' % (current_word, current_doc, current_count))
        