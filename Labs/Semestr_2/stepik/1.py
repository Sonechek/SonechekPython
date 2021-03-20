
numbers = {
   0: ('##', '##', '##', '##'),
   1: ('.#', '##', '.#', '.#'),
   2: ('##', '.#', '#.', '##'),
   3: ('##', '.#', '.#', '##'),
   4: ('##', '##', '.#', '.#'),
   5: ('##', '#.', '.#', '##'),
   6: ('.#', '#.', '##', '##'),
   7: ('##', '.#', '#.', '#.'),
   8: ('##', '..', '##', '##'),
   9: ('##', '##', '.#', '#.')
}



n = str(input())
for i in range(4):
    res = ''
    for j in range(len(n)):
        res += numbers[int(n[j])][i]

    print(res)
# tab = []
# n = str(input())
# for i in range(4):
#     for j in range(len(n)):
#     # print(numbers[int(item)])
#         tab.append(numbers[i][int(n)])
# for i in range(len(tab)):
#     tab.append('\n')

# # print(n)
# # print(numbers[n])
# res = ''.join(tab)

# print(res)
