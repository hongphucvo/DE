#!/usr/bin/env python

import sys

current_doc = None
doc = None
word = None
cur = [(word, 0.)]
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    doc, word = line.split('\t', 1)
    word, tf = word.split('#', 1)
    try:
        tf = float(tf)
    except ValueError:
        continue

    if current_doc == doc:
        cur += [(word, tf)]
    else:
        # tf calculating
        if current_doc:
            val = sum(w[1]for w in cur)
            for word_tf in cur:
                print ('%s@%f#%s\t%f' % (current_doc,val, word_tf[0],word_tf[1]))
            # print('%s\t%s' % (current_doc, cur))
        current_doc = doc
        cur = [(word, tf)]
# do not forget to output the last doc if needed!
if current_doc == doc:
    val = sum(w[1]for w in cur)
    for word_tf in cur:
        print ('%s@%f#%s\t%f' % (current_doc,val, word_tf[0],word_tf[1]))