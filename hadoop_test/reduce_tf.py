#!/usr/bin/env python

from math import log
import sys

current_word = None
word = None
doc = None
cur = []
size = 20  # TODO config




# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    word, doc = line.split('\t', 1)
    doc, freq = doc.split('#', 1)
    try:
        freq = float(freq)
    except ValueError:
        # ignore/discard this line
        continue

# this IF-switch only works because Hadoop sorts map output
# by key (here: word) before it is passed to the reducer
    if current_word == word:
        docs=map(lambda x: x[0],cur)
        if doc not in docs:
            cur += [(doc, freq)]
    else:
        # tf calculating
        if current_word:
            val = log(float(size)/(len(cur)))
            cur = sorted(map(lambda doctf: (
                doctf[0], doctf[1]*val), cur))
            for doctf in cur:
                print ('%s\t%s#%f' % (current_word, doctf[0],doctf[1]))
        current_word = word
        cur = [(doc, freq)]
# do not forget to output the last word if needed!
if current_word == word:
    val = log(float(size)/len(cur))
    cur = sorted(map(lambda doctf: (
        doctf[0], doctf[1]*val), cur))
    for doctf in cur:
        print ('%s\t%s#%f' % (current_word,doctf[0], doctf[1]))