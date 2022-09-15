import sys
repeat = int(sys.stdin.readline())
deque = []
for i in range(repeat):
    message = sys.stdin.readline().split()
    if message[0] =="push_front":
        deque.insert(0, message[1])
    
    elif message[0] =="push_back":
        deque.append(message[1])
    
    elif message[0] =="pop_front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop(0))
    
    elif message[0] =="pop_back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque.pop())
    
    elif message[0] =="size":
        print(len(deque))

    elif message[0] =="empty":
        if len(deque)==0:
            print(1)
        else:
            print(0)
    elif message[0] =="front":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[0])
    elif message[0] =="back":
        if len(deque)==0:
            print(-1)
        else:
            print(deque[-1])