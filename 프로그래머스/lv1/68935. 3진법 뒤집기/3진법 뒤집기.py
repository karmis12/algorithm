def solution(n):
    answer = ''
    while n>=1:
        n, re = divmod(n,3)
        answer+=str(re)
    answer= int(answer,3)
    return answer