
numbers = {
   '########':0,
   '.###.#.#':1,
   '##.##.##':2,
   '##.#.###':3,
   '####.#.#':4,
   '###..###':5,
   '.##.####':6,
   '##.##.#.':7,
   '##..####':8,
   '####.##.':9
}

text = ''
for i in range(4):
    x = input()
    if x:
        text += x

lines = text.splitlines()
key = ''.join(map(str, lines))

print(numbers[key])