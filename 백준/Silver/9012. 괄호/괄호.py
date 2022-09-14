repeat = int(input())
for i in range(repeat):
    count=0
    check=True
    ps = input()
    for j in range(len(ps)):
        if ps[j] =="(":
            count+=1
        elif ps[j] == ")":
            count-=1
        if count <0:
            print("NO")
            check=False
            break
    if check==True:
        if count == 0:
            print("YES")
        elif count!=0:
            print("NO")