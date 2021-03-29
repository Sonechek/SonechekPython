def code(alph, line, key):
    result = ''
    result = ''.join([chr(ord(smb)+ chr(ord((aplh)))*key) for smb in line])


    return result



rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
nums = '1234567890'
smbs = ':; !&-+=()*/.,'
alph = rus + rus.upper() + nums + smbs

line = ''
line = input()
key = 9412

line_code = code(alph, line, key)
print(line_code)