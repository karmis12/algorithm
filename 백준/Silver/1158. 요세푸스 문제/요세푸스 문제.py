N,K = map(int, input().split())
list = [i for i in range(1,N+1)]

num = 0
answer = []

for j in range(N):
    num += K-1
    if num >=len(list):
        num = num%len(list)
    
    answer.append(list.pop(num))
answer = ", ".join(map(str,answer)) # list를 join 할때 list안의 요소가 int값이면 join못함 따라서 str값으로 변경해야됨
print(f"<{answer}>")