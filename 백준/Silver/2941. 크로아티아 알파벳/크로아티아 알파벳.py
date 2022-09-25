word = input()
len= len(word)
num2 = 0
num3 = 0

alp2 = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
alp3 = ["dz="]

for i in alp2:
    alp, num = i ,word.count(i)
    # print(alp+":", num)
    num2+= num

for i in alp3:
    alp, num = i ,word.count(i)
    # print(alp+":", num)
    num= num+1-1

    num2 += num
    #원래 dz=의 경우에는 3글자가 1글자이므로 글자수 -2해야되는데 alp2에서 중복으로 빠지므로 1번만 빼면된다
len-=num2

print(len)