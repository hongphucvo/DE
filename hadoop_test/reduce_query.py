#!/usr/bin/env python

import sys

current_doc=None
current_word=None
isIn=False
word=None
# read the entire line from STDIN
for line in sys.stdin:
    line = line.strip()
    # if len(line.split('\t'))>1:#   len(line.split('\t'))>1:
    try:    
        word,docs = line.split('\t')
    # print(word)
        if current_word == word:
            if docs=='0':
                isIn=True
            else:
                current_doc=docs
        else:
            # tf calculating
            # print(word)
            # print(current_doc,'+',isIn)
            if current_doc!=None and isIn == True:
                print('%s\t%s' %(current_word,current_doc))
            if docs=='0':
                isIn=True
                current_doc=None
            else:
                current_doc=docs
                isIn=False
            current_word=word
    except:
        pass
# do not forget to output the last word if needed!
if current_word == word:
    if current_doc!=None and isIn == True:
        print('%s\t%s' %(word,current_doc))
            