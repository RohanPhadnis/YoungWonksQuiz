l = []
TAX_RATE = 0.3

with open('data.csv') as file:
    text = file.read().split('\n')

headers = text[0].split(',')

for data in text[1:]:
    temp = data.split(',')
    d = {}
    for n in range(len(temp)):
        d[headers[n]] = temp[n]
    l.append(d)

for n in range(len(l)):
    for k in headers:
        if k not in l[n].keys():
            if k == 'tax':
                l[n]['tax'] = str(int(TAX_RATE * int(l[n]['pay'])))
            elif k == 'total':
                l[n]['total'] = str(int((1 - TAX_RATE) * int(l[n]['pay'])))

write = ''

s = ','.join(headers) + '\n'
for d in l:
    s += ','.join(d.values()) + '\n'

with open('output.csv', 'w') as file:
    file.write(s)