n=int(input())
list = list(map(int, input().split()))

max_score = max(list)
new_list = [i/max_score*100 for i in list]
total_score = 0

for i in new_list:
    total_score += i
ans = total_score/n
print(ans)