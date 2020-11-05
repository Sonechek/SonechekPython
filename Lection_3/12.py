import requests

link = 'https://pcoding.ru/csv/12.txt'
s = requests.get(link).content.decode('utf-8')
tab = [list(map(int, line.split())) for line in s.split('\n')]
for item in tab:
    print(*item)
n = len(tab)
for y in range(n):
    for x in range(n):
        if x > y:
            tab[y][x], tab[x][y] = tab[x][y], tab[y][x]
for item in tab:
    print(*item)