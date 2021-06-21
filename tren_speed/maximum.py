tab = list(map(int, str(input())))
final_number = ''
for i in range(int(len(tab))):
    maximum = max(tab)
    tab.remove(max(tab))
    final_number += str(maximum)
print(final_number)
