def numerology(nothing):
    list_guests = open('input.txt', 'r',encoding='UTF-8')
    text = list_guests.read()
    lines = text.split('\n')
    for number_of_guest in range(1,len(lines)):
        count = 0
        for i in range(1,(number_of_guest)+2):
            if (number_of_guest % i) == 0:
                count += i
        if (count % 2) != 0:
            print((lines[number_of_guest-1].split(' '))[(1 if len(lines[number_of_guest-1].split(' ')) == 2 else 2)])
numerology(int(input()))
