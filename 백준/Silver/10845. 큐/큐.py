import sys
repeat = int(sys.stdin.readline())
que=[]
for i in range(repeat):
    message = sys.stdin.readline().split()

    if message[0] == "push":
        que.append(message[1])

    elif message[0] == "pop":
        if len(que)==0:
            print(-1)
        else:
            print(que.pop(0))

    elif message[0] == "size":
        print(len(que))

    elif message[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0) 

    elif message[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])

    elif message[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])