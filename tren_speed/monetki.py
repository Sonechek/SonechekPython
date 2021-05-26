n = int(input())
zeros = 0
ones = 0
for i in range(n):
    temp = input()
    if temp == '1':
        ones += 1
    else:
        zeros += 1
if ones >= zeros:
    print(zeros)
elif zeros > ones:
    print(ones)
