from functions import students_kunger, mans_Kungur, mans_rating_Kungur, names_not_from_Perm, select_all_sorted

names = students_kunger()
for name in names:
    print(name['nameStud'])

names = mans_Kungur()
for name in names:
    print(name['nameStud'])

names = mans_rating_Kungur()
for name in names:
    print(name['nameStud'], name['rating'])

names = names_not_from_Perm()
for name in names:
    print(name['nameStud'])

names = select_all_sorted()
for name in names:
    print(name['nameStud'])
