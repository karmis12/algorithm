def solution(s):
    nums= {}
    nums["zero"]=0
    nums["one"]=1
    nums["two"]=2
    nums["three"]=3
    nums["four"]=4
    nums["five"]=5
    nums["six"]=6
    nums["seven"]=7
    nums["eight"]=8
    nums["nine"]=9
    
    answer=s
    for key, value in nums.items():
        answer= answer.replace(key,str(value))
                                
    return int(answer)