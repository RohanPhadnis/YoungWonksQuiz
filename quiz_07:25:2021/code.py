day1 = {'Steven': 60, 'Vishal': 1000, 'Richard': 100, 'Julian': 40, 'Larry': 50}
day2 = {'Steven': 70, 'Vishal': 1000, 'Richard': 200, 'Julian': 50, 'Larry': 60}
day3 = {'Steven': 80, 'Vishal': 1000, 'Richard': 300, 'Julian': 60, 'Larry': 70}
pay_days = [day1, day2, day3]
'''data = {key: 0 for key in pay_days[0].keys()}
data = {key: data[key] + day[key] for day in pay_days for key in day}
print(data)'''

data = {k1: sum([day[k2] for day in pay_days for k2 in day.keys() if k1 == k2]) for day in pay_days for k1 in day.keys()}
print(data)
