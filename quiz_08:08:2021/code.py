dictionary = {}
keys = ['a', 'b', 'c']
print(dictionary)

for n in range(10):
    print(n)
    for key in keys:
        print(key)
        try:
            print('trying')
            dictionary[key] += 1
        except KeyError as error:
            print('received KeyError:', error)
            dictionary[key] = 0
        else:
            print('no error')
    print()
    print()

print(dictionary)
