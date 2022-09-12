hour, minute = map(int, input().split())
if minute-45>=0:
    print(hour, minute-45)
elif minute-45<0:
    if hour>0:
        print(hour-1, 60+(minute-45))
    else:
        hour=24
        print(hour-1, 60+(minute-45))
