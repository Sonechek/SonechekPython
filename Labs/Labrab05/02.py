f1 = open('c:/Users/user/Desktop/input.txt', 'r')
text = f1.read()
count = 0
for i in range(len(text)):
    if text[i] == '1':
        count += 1
count //= 2
print(count)
f1.close()