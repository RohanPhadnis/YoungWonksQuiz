import pprint

with open('data.csv') as file:
    text = file.read().split('\n')

keys = text[0].split(',')
print(keys)
l = []

for val in text[1:]:
    
    if len(val) > 0:
        d = {}
        data = val.split(',')
        print(data)
        for k in range(len(keys)):
            try:
                d[keys[k]] = float(data[k])
            except:
                d[keys[k]] = data[k]
        l.append(d)

pprint.pprint(l)
