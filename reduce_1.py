



# import os, json,sys
# from collections import defaultdict
#!/usr/bin/python
# import sys
# def readDictionary():
#     dictionary = {}
#     dir_path = "./dictionary_map_1"
    
#     numFiles = 0
    
#     for path in os.listdir(dir_path):
#         # check if current path is a file
#         if os.path.isfile(os.path.join(dir_path, path)):
#             numFiles += 1
    
#     print(numFiles)
    
#     for i in range(0, numFiles):
#         file = open("./dictionary_map_1/" + str(i) + ".json")
#         dict = json.load(file)
#         dictionary["D" + str(i)] = dict["D" + str(i)]
    
#     return dictionary
        
# def reduce_1():
#     dictionary = readDictionary()
#     result = defaultdict(list)
    
#     for name in dictionary:
#         dict = dictionary[name]
#         for key in dict:
#             result[key].append(str(name) + "@" + str(len(dict)))
    
#     return result

# def writeFile(result):
#     dir = "./dictionary_reduce_1"
#     for f in os.listdir(dir):
#         os.remove(os.path.join(dir, f))
    
#     for name in result:
#         file = open("./dictionary_reduce_1/" + name + ".json", 'w+')
        
#         data = {
#             str(name): result[name]
#         }
        
#         json_object = json.dumps(data, indent = 4)
        
#         file.write(json_object)
#         file.close()
# for line in sys.stdin:
#     # remove leading and trailing whitespace
#     line = line.strip()
#     print(line) 
# 
# 

# for line in sys.stdin:
#     print(line)      






#!/usr/bin/python
  
from operator import itemgetter
import sys
  
current_word = None
current_count = 0
word = None
  
# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
  
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # write result to STDOUT
            print('%s\t%s' % (current_word, current_count))
        current_count = count
        current_word = word
  
# do not forget to output the last word if needed!
if current_word == word:
    print('%s\t%s' % (current_word, current_count))
