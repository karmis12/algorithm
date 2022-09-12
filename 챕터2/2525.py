 hour, minute = map(int, input().split())
time=int(input())
if minute+time>=60:
    plus_time = int((minute+time)/60)
    minute = (minute+time)%60
    hour+=plus_time
    if hour>=24:
        hour-=24
    print(hour,minute)
elif minute+time<60:
    print(hour,minute+time)