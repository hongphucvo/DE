from collections import defaultdict
import string, json, os

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

def writeFile(dictionary):
    dir = "./dictionary_map_1"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
        
    for i in range(0, len(dictionary)):
        file = open("./dictionary_map_1/" + str(i) + ".json", 'w+')
        
        data = {
            "D" + str(i): dictionary["D" + str(i)]
        }
        
        json_object = json.dumps(data, indent = 4)
        
        file.write(json_object)
        file.close()

    