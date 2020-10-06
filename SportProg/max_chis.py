s = input()

lst = list(s)

#print(sorted(lst, reverse=True))
s = ''.join(sorted(lst)[::-1])
print(s)