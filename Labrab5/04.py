def Tumba_04_Desifr(de): #Дешифратор 
    nums = []
    for _ in range(len(str(de))):
        nums.insert(0,de%10)
        de //= 10
    result_desifr = []
    firstnum = {1:'одна',2:'две',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять',10:'десять',}
    secondnum_for_two_to_five = {1:'единицы',2:'двойки',3:'тройки',4:'четвёрки',5:'пятёрки',6:'шестёрки',7:'семёрки',8:'восьмёрки',9:'девятки',10:'десятки',}
    secondnum_for_one = {1:'единица',2:'двойка',3:'тройка',4:'четвёрка',5:'пятёрка',6:'шестёрка',7:'семёрка',8:'восьмёрка',9:'девятка',10:'десятка',}
    secondnum_for_five_to_ten = {1:'единиц',2:'двоек',3:'троек',4:'четвёрок',5:'пятёрок',6:'шестёрок',7:'семёрок',8:'восьмёрок',9:'девяток',10:'десяток',}
    for i in range(0,len(nums),2):
        result_desifr.append(firstnum[nums[i]])
        if nums[i] == 1:
            result_desifr.append(secondnum_for_one[nums[i+1]])
            result_desifr.append(',')
            continue
        if 2 <= nums[i] <= 4:
            result_desifr.append(secondnum_for_two_to_five[nums[i+1]])
            result_desifr.append(',')
            continue
        if 5 <= nums[i] <= 10:
            result_desifr.append(secondnum_for_five_to_ten[nums[i+1]])
            result_desifr.append(',')
            continue
    print(*result_desifr)

def Tumba_04_Sifr(si): #шифратор
    nums = []
    for _ in range(len(str(si))):
        nums.insert(0,si%10)
        si //= 10
    result_sifr = []
    for i in range(9):
        if i in nums:
            result_sifr.append(Tumba_Count(i,nums))
            result_sifr.append(i)
    print(*result_sifr,sep='')

def Tumba_Count(n,nums):#считаем количество животных одного типа
    return(nums.count(n))
Tumba_04_Desifr(int(input()))