repeat = int(input())

for i in range(repeat):
    num, word = input().split()
    num = int(num)
    for j in word:
        print(num*j,end="")
    print("")