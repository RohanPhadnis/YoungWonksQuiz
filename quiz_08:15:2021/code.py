# IMPORTING DEPENDENCIES
import json
import os

# READING DATA
with open('input.csv') as file:
    rows = file.read().strip().split('\n')

# VARIABLE DEFINITION
headers = rows[0].split(',')
data = []

# DATA PARSING
for row in rows[1:]:
    d = {}
    vals = row.split(',')
    for n in range(len(headers)):
        d[headers[n]] = vals[n]
    data.append(d)


print(data)

# DATA WRITING AND STORAGE
encoder = json.JSONEncoder()

if 'output.json' not in os.listdir():
    open('output.json', 'x')

with open('output.json', 'w') as file:
    file.write(encoder.encode(data))



