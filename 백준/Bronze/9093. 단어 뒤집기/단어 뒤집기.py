repeat = int(input())
for i in range(repeat):
    sentence = input().split()
    for j in sentence:
        print(j[::-1],end=" ")