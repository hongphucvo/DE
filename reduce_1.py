import os, json
from collections import defaultdict

def readDictionary():
    dictionary = {}
    dir_path = "./dictionary_map_1"
    
    numFiles = 0
    
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            numFiles += 1
    
    print(numFiles)
    
    for i in range(0, numFiles):
        file = open("./dictionary_map_1/" + str(i) + ".json")
        dict = json.load(file)
        dictionary["D" + str(i)] = dict["D" + str(i)]
    
    return dictionary
        
def reduce_1():
    dictionary = readDictionary()
    result = defaultdict(list)
    
    for name in dictionary:
        dict = dictionary[name]
        for key in dict:
            result[key].append(str(name) + "@" + str(len(dict)))
    
    return result

def writeFile(result):
    dir = "./dictionary_reduce_1"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    
    for name in result:
        file = open("./dictionary_reduce_1/" + name + ".json", 'w+')
        
        data = {
            str(name): result[name]
        }
        
        json_object = json.dumps(data, indent = 4)
        
        file.write(json_object)
        file.close()
            