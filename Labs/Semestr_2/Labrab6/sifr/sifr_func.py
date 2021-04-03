# from PIL import Image

def code(alph, key):
    with open(f'input.txt', mode='r', encoding='utf8') as o:
        tabs = o.read().split('\n')
    with open(f'output.txt', mode='w', encoding='utf8') as inp:
        for i in range(len(tabs)):
            line = ''
            for j in range(len(tabs[i])):
                line += alph[(alph.index(tabs[i][j]) + key) % len(alph)]
            inp.write(line + '\n')


rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890'
eng_alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb = ':; !?&-+=()*/.,'
alph = rus_alph + eng_alph + symb
key = 3

code(alph, key)
