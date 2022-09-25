word = input().upper()
max=0
ans=True
for i in set(word):
    if word.count(i) > max:
        max = word.count(i)
        ans = i
    
    elif word.count(i) == max:
        ans = False
if ans == False:
    print("?")
else:
    print(ans)