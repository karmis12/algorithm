n = int(input())
num = input()
nums =list(map(int, num))  
# map을 쓰는 이유는 str문자를 하나하나의 문자로 바꿔주고 각각int값으로 바꾸기 위해
sum_nums = sum(nums)
print(sum_nums)