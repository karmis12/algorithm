n=int(input())
room_num=1
cover_num=1
while n>room_num:
  room_num=room_num+6*cover_num
  cover_num+=1
print(cover_num)