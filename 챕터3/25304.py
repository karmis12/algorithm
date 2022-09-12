total=int(input())
n=int(input())
sum=0
for i in range(n):
    a,b=map(int, input().split())
    price=a*b
    sum+=price
if total==sum:
    print("Yes")
else:
    print("No")