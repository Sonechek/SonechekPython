import requests

link = 'https://pcoding.ru/csv/11.txt'

s = requests.get(link).content.decode('utf-8')
lst = s.split(' ')
acc = 0
for item in lst:
    acc += int(item)
print(acc)