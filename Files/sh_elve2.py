import shelve
db = shelve.open("file2.txt")
db['language'] = ['ru', 'rn', 'ua']
db['colors'] = ['red', 'blue', 'green']
db['language'], db['colors']
(['ru', 'rn', 'ua'], ['red', 'blue', 'green'])
db.close()