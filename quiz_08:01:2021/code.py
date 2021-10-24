d1 = {'a': 1, 'b': 2, 'c':3}
d2 = {'d': 4, 'e': 5, 'f': 6}
d3 = {'g': 7, 'h': 8, 'i':9}

l = [d1, d2, d3]
d = {key: val for dictionary in l for key, val in dictionary.items()}
print(d)
