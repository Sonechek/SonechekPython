n = int(input())
lst = [int(input()) for i in range(n)]
for i in range(n):
    if lst[i] % 2 == 0:
        lst_4 = [lst[i]]
    else:
        lst_3 = [lst[i]]
print(lst_3)
print(lst_4)
if len(lst_4) > len(lst_3):
    print('Yes')
else:
    print('No')