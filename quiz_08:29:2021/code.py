import os
import json

unicode = {n: chr(n) for n in range(128)}
file_name = 'data.json'
encoder = json.JSONEncoder()
decoder = json.JSONDecoder()

print(unicode)

if file_name not in os.listdir():
    open(file_name, 'x')


with open(file_name, 'w') as file:
    file.write(encoder.encode(unicode))


with open(file_name) as file:
    data = decoder.decode(file.read())


print()
print(data)
