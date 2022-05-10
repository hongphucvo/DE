import requests

size = 20


for i in range (1,size +1):

    url = 'https://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt.utf8'
    try:
        r = requests.get(url, allow_redirects=True)
    except:
        r = requests.get(url+'.gzip', allow_redirects=True)
    filename = './col/'+str(i)+'.txt'
    open(filename, 'wb').write(r.content)
