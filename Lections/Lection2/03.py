# цикл с постусловием
pos_begin = 48; pos_end = 57
pos = pos_begin
b = True
while True:
    print(pos, chr(pos))
    pos += 1 
    if pos> pos_end:
        break
        