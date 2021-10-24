# range object iteration
total = 0
for i in range(0, 100):
    print(i)
    total += i
print('total:', total)


# list object iteration
fruits = ['apple', 'banana', 'grapes', 'orange']
for f in fruits:
    print(f)


# double variable iteration
fruits = ['apple', 'banana', 'grapes', 'orange']
for index, fruit in enumerate(fruits):
    print('index: {}\tfruit: {}'.format(index, fruit))

prices = {
    'apple': 5,
    'banana': 1,
    'grapes': 3,
    'orange': 2
    }
for key, value in prices.items():
    print('fruit: {}\tprice: {}'.format(key, value))


# anonymous for loop
for _ in range(5):
    print('hello!')


# single-line
import random
nums = [random.randint(0, 10) for _ in range(10)]
print(nums)
unicode =  {num: chr(num) for num in range(128)}
print(unicode)
