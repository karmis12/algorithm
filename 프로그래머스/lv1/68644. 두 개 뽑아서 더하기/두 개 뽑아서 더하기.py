def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            j=j+1+i
            num=numbers[i]+numbers[j]
            answer.append(num)
    answer=sorted(set(answer))
    return answer