import requests

link = 'https://pcoding.ru/csv/11.txt'

s = requests.get(link).content.decode('utf-8')

s = list(map(int, s.split(' ')))
s = sum(s)
print(s)