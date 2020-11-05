import requests

link = 'https://pcoding.ru/csv/11.txt'
s = requests.get(link).content.decode('utf-8')
s = list(map(int, s.split()))
lst = []
for item in s:
    if item % 2 != 0:
        lst.append(item)
print(lst)