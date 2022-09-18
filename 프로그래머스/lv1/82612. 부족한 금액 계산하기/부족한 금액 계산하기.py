def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer+=price*(i+1)
    if money - answer>=0:
        answer=0
    else:
        answer= answer-money
    return answer