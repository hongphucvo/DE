#!/usr/bin/env python

import sys

current_word = None
word = None
doc = None
cur = [(doc, 1.)]
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    word, doc = line.split('\t', 1)
    doc, tf = doc.split('#', 1)
# convert count (currently a string) to int
    try:
        tf = float(tf)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

# this IF-switch only works because Hadoop sorts map output
# by key (here: word) before it is passed to the reducer
    if current_word == word:
        cur += [(doc, tf)]
    else:
        # tf calculating
        if current_word:
            cur = sorted(cur)
            print('%s\t%s' % (current_word, cur))
        current_word = word
        cur = [(doc, tf)]
# do not forget to output the last word if needed!
if current_word == word:
    cur = sorted(cur)
    print('%s\t%s' % (current_word, cur))