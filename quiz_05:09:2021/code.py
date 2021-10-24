string = input('enter string: ')
print(string * len(string))

for _ in range(len(string)):
    print(string, end='')
