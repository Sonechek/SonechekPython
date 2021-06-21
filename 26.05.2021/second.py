tab = list(map(int, str(input())))
final_number = 0
for i in range(int(len(tab))):
    maximum = max(tab)
    tab.remove(max(tab))
    final_number += int(maximum)
print(final_number)