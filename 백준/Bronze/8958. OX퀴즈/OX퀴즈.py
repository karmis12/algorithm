n = int(input())
for i in range(n):
    OX=input()
    score = 0
    box =0
    for j in OX:
        if j=="O":
            box += 1
            score+=box
        elif j=="X":
            box=0
    print(score)