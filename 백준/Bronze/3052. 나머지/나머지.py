list = [int(input()) for i in range(10)]
remain_list=[]
for j in range(10):
    if list[j]%42 not in remain_list:
        remain_list.append(list[j]%42)
    else:
        pass
print(len(remain_list))