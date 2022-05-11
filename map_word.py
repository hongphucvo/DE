#!/usr/bin/env python

from operator import itemgetter
import sys

# read the entire line from STDIN


def str_tup(str):
    # print(str)
    str = str[1:] if str[len(str)-1] != ')' else str[1:-1]
    ele = str.split(', ')
    # print(ele[0][1:-1])
    return (ele[0][1:-1], float(ele[1]))


def str_tup_list(str):
    str = str[1:-1]
    tup_list = str.split('), ')
    # print(tup_list)
    return map(lambda tup: str_tup(tup), tup_list)


for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # splitting the data on the basis of tab we have provided in mapper.py
    word, docs = line.split('\t', 1)
    # print(line)
    docs = str_tup_list(docs)
    # print(word, docs)
    for doc, idx in enumerate(docs):
        for idx2 in range (doc+1, len(docs)):
            if len(docs) > idx2:
                m=min(idx[1],docs[idx2][1])
                # if m>0.:#&&(idx[0][0:4]=='0.txt'||docs[idx2][0][0:4]=='0.txt')
                print('%s#%s\t%f' % (idx[0], docs[idx2][0], m))


