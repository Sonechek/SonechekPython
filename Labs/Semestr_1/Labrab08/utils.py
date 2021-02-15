import re
# #def code_pifii(st):
#     '''
#         chr() - возвращает символ от его номера
#         мы должны каждые два символа возвращать в десятичный формат и затем функцией chr() возвращать сам\
#         около 32 длина 
#         68 74 74 70 73 3A 2F 2F 70 63 6F 64 69 6E 67 2E 72 75 2F 74 78 74 2F 77 6F 72 64 73 2E 74 78 74
        
#     ''' 
#     st = re.findall(r'\w\w', st)

#     tab = []
#     for i in range(len(st)):
#         tab.append(int(st[i], 16))

#     acc = []
#     for i in range(len(tab)):
#         acc.append(chr(tab[i]))
#     site = ''.join(acc)
#     print(site)


def binary_search(value):
    f1 = open('words-utf8.txt', 'r')
    text = []
    text = f1.read()
    first = 0
    last = len(text) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if text[mid] == value:
            index = mid
        else:
            if value < text[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index
    f1.close()


print(binary_search(input()))