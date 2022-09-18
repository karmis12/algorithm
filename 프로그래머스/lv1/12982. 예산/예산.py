def solution(d, budget):
    d.sort()
    answer=len(d)
    sum=0
    for i in range(len(d)):
        sum += d[i]
        if sum>budget:
            answer=i
            break
        elif sum ==budget:
            answer=i+1
            break
    return answer