response = 'Hello, {}! You are {} years old.'
name = input('name: ')
age = int(input('age: '))
formatted = response.format(name, age)
print(formatted)


print(f'Hello, {name}! You are {age} years old.')
