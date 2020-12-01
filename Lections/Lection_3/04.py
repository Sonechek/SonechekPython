import requests

link = 'https://pcoding.ru/csv/12.txt'
s = requests.get(link).content.decode('utf-8')

lines = s.split('\n')
summa = sum(map(int, lines[0].split()))
print(summa)
