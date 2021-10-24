def find_substring(string1, string2):
    if len(string1) < len(string2):
        smaller, bigger = string1, string2
    else:
        smaller, bigger = string2, string1
    same = False
    for x in range(len(bigger) - len(smaller)):
        if bigger[x] == smaller[0]:
            same = True
            for y in range(0, len(smaller)):
                if smaller[y] != bigger[x + y]:
                    same = False
        if same:
            return True
    return False


for _ in range(5):
    s1 = input('Enter string: ')
    s2 = input('Enter string: ')
    print(find_substring(s1, s2))
