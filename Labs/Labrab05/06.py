def Sambala(day):  #Шамбалаааааа
    nday = ((day//2 * 2) + day)
    tab = []
    for i in range(nday):      
        '''
        Если строки в таблице одинаковые, то "tab[1][1] = 0" поменяет не одно значение в координате [1][1], а весь столбец,
        потому что вся таблица(при условии, что строки в ней идентичные или пустые, полностью не проверил) ссылается на одну строку
        и "tab[1][1] = 0" меняет всего одну строку, на которую будет ссылаться таблица поэтому каждую строку желательно заполнить 
        хотя бы одним символом
        '''
        line = str(i)+' ' * (nday - 1)
        line = line.split(' ')
        tab.append(line)
    for pos in range(nday):   #Внешний квадратик
        tab[0][pos] = 'X'
        tab[pos][0] = 'X'
        tab[nday-1][pos] = 'X'
        tab[pos][nday-1] = 'X'

    count_circles = day // 2 
    countX = nday - 2
    posiX = 2
    while count_circles != 0:
        for pos in range(posiX,countX):
            tab[posiX][pos] = 'X'
            tab[pos][posiX] = 'X'
            if count_circles == 1:
                break
            tab[-posiX-1][pos] = 'X'
            tab[pos][-posiX-1] = 'X'
        countX -= 2
        posiX += 2
        count_circles -= 1

    print(tab)
    # for i in range(len(tab)):
    #     print(tab[i])
        
    # for i in range(len(tab)):
    #     print(*tab[i])

    sstr = str()
    for pos in range(len(tab)):
        for i in range(len(tab)):
            sstr += tab[pos][i]
            if tab[pos][i] != 'X':
                sstr += '■'
            # sstr = sstr.join(tab[i])
        sstr += '\n'
    print(sstr)
Sambala(int(input()))
