import requests

size = 10


for i in range (1,size +1):

    url = 'https://www.gutenberg.org/cache/epub/'+str(i)+'/pg'+str(i)+'.txt.utf8'
    r = requests.get(url, allow_redirects=True)
    filename = './collection/'+str(i)+'.txt'
    open(filename, 'wb').write(r.content)