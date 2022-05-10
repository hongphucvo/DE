#!/usr/bin/env python

import sys

# read the entire line from STDIN

for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    word, doc = line.split('#', 1)
    doc, count = doc.split('\t', 1)
    # try:
    #     count = int(count)
    # except ValueError:
    #     continue
    # print(line)
    print('%s\t%s=%s' % (doc, word, count))