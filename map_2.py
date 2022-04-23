import string, os, json
from collections import defaultdict

def readDictionary():
    dictionary = {}
    dir_path = "./dictionary_reduce_1"
    
    numFiles = 0
    
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            numFiles += 1
        
    for path in os.listdir(dir_path):
        f = open(dir_path + "/" + path)
        json_object = json.load(f)
        
        dictionary[str(path.split(".")[0])] = json_object[str(path.split(".")[0])]
    
    return dictionary

def normalize(doc: string):
    quotes = ['.', ',', '-', '\'', '\"', '?']
    escape_seq = ['\n', '\t', '\r']
    
    for quote in quotes:
        doc = doc.replace(quote, "")
        
    for esq in escape_seq:
        doc = doc.replace(esq, " ")
    
    return doc

def split_doc(doc):
    result = set()
    split_array = doc.split(" ")
    
    for word in split_array:
        result.add(word)
    
    return result

def create_dictionary(docs):
    result = defaultdict(list)
    
    for i in range(0, len(docs)):
        for word in docs[i]:
            result["D" + str(i)].append(word)
    
    return result

def map_1(dataSet: list):
    dataRemovedQuote = list(map(lambda x: normalize(x), dataSet))
    
    dataSplit = list(map(lambda x: split_doc(x), dataRemovedQuote))
        
    dictionary = create_dictionary(dataSplit)
    
    return dictionary

def map_2(query: string):
    dict_query = map_1([query])
    dict_search = {"Dq": dict_query["D0"]}
    
    dictionary = readDictionary()
    result = {}
    
    for word in dictionary:
        if word in dict_search["Dq"]: 
            for doc in dictionary[word]:
                key = doc + "-" + "Dq@" + str(len(dict_search))
                if key in result:
                    result[key] += 1
                else: result[key] = 1
                
    return result
