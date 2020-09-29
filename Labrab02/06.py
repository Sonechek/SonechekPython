x = int(input())
for i in range(x):
    print('%s%s' % (' ' * (x-i-1), 'x' * (i*2+1)))