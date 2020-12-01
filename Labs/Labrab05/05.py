n = input()
bukv = ['A','B','C','D','E','F','G','H']
num = ['1','2','3','4','5','6','7','8']
a = n[:2]
b = n[3:]
pos_b = 0
pos_a = 0
item_b1 = 0
item_a1 = 0
pos_a2 = 0
pos_b2 = 0
item_a2 = 0
item_b2 = 0
while a[:1] != bukv[item_b1]:
    item_b1 += 1
else:
    pos_b = item_b1
while a[1:2] != num[item_a1]:
    item_a1 += 1
else:
    pos_a = item_a1
while b[:1] != bukv[item_b2]:
    item_b2 += 1
else:
    pos_b2 = item_b2
while b[1:] != num[item_a2]:
    item_a2 += 1
else:
    pos_a2 = item_a2
if (abs(pos_a2 - pos_a) == 1 and abs(pos_b2 - pos_b) == 2) or (abs(pos_a2 - pos_a) == 2 and abs(pos_b2 - pos_b) == 1):
    print("Yes")
else:
    print("No")