import pprint

sentences = []

with open('data.txt') as file:
    for line in file.read().strip().split('\n'):
        sentences.append(line.split(' '))

pprint.pprint(sentences)

for x in range(len(sentences)):
    indices =  []
    for y in range(len(sentences[x])):
        if sentences[x][y] == 'I' or sentences[x][y] == 'you':
            indices.append(y)
        elif 'I' in sentences[x][y] or 'you' in sentences[x][y]:
            sentences[x][y] = sentences[x][y].replace('I', '')
            sentences[x][y] = sentences[x][y].replace('you', '')
    for loop, i in enumerate(indices):
        sentences[x].pop(i-loop)

print()
pprint.pprint(sentences)
