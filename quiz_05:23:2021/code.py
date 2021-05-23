import pprint

with open('data.csv') as file:
    text = file.read().split('\n')

keys = text[0].split(',')
l = []

for val in text[1:]:
    if len(val) > 0:
        d = {}
        data = val.split(',')
        for k in range(len(keys)):
            d[keys[k]] = data[k]
        l.append(d)

pprint.pprint(l)
