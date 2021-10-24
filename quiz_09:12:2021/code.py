vowels = 'aeiou'
vowels += vowels.upper()

print(vowels)

for _ in range(5):
    string = input('Enter a string: ')
    for v in vowels:
        string = string.replace(v, '')
    print(string)
