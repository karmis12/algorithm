a=(input())
b=(input())
res=0
for i in range(len(b)):
    c=int(a)*int(b[-(i+1)])
    print(c)
    res+=c*(10**i)
print(res)