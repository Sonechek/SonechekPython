# from PIL import Image

def code(alph, key):
    with open(f'input.txt', mode='r', encoding='utf8') as o:
        tabs = o.read().split('\n')
    with open(f'output.txt', mode='w', encoding='utf8') as w:
        for i in range(len(tabs)):
            line = ''
            for j in range(len(tabs[i])):
                line += alph[(alph.index(tabs[i][j]) + key) % len(alph)]
            w.write(line + '\n')


rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ1234567890'
eng_alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
symb = ':; !?&-+=()*/.,'
alph = rus_alph + eng_alph + symb
key = 149995388

code(alph, key)
