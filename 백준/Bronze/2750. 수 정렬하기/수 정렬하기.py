repeat = int(input())
list=[]
for i in range(repeat):
    num = int(input())
    if num not in list:
        list.append(num)
list = sorted(list)
for i in list:
    print(i)