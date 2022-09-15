bracket = list(input())
stack =[]
answer = 0
for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
    elif bracket[i] == ")":
        if bracket[i-1] =="(":
            stack.pop()
            answer+=len(stack)
        elif bracket[i-1] == ")":
            stack.pop()
            answer+=1
print(answer)