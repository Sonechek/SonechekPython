lst = [int(input()) for i in range(int(input()))] 

print(min(sum(lst), len(lst)- sum(lst)))