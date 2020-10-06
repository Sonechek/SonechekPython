k = input()
if 'A'in k or 'C' in k or 'E' in k or 'G' in k:
    if int(k[-1]) % 2 == 0:
        print('WHITE')
    else:
        print('BLACK')
else:
    if int(k[-1]) % 2 ==0:
        print ('BLACK')
    else:
        print('WHITE')