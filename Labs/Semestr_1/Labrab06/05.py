def lections_Noknown(nothing):
    true_names = []
    for _ in range(int(input())):
        true_names.append(input())
    Noknowh_names = []
    for _ in range(int(input())):
        Noknowh_names.append(input())

    for name in true_names:
        count = 0
        for second_name in Noknowh_names:
            
            if len(name) != len(second_name):
                continue
            for i in range(len(name)):
                name_check = list(name)
                second_name_check = list(second_name)
                name_check[i] = ''
                second_name_check[i] = ''
                if name_check == second_name_check:
                    count += 1
        print(count,end=' ')
lections_Noknown(int(input()))