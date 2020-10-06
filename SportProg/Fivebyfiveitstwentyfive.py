a = int(input())
per_ch = 0
vt_ch = 0
if a == 5:
    print(a**2)
else:
    per_ch = a // 10
    vt_ch = a % 10
    s1 = str((per_ch + 1) * per_ch)
    s2 = str(vt_ch ** 2)
    print(s1+s2)

