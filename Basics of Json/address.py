book = {}
book['tom'] = {
    'name' : 'tom',
    'address' : '1 red street, NY',
    'phone' : 98833
    }

book['bob'] = {
    'name' : 'bob',
    'address' : '1 green street, NY',
    'phone' : 232452
    }
import json
s = json.dumps(book)
with open("/Users/valdermaut/Desktop/book.txt","w") as f:
     f.write(s)
