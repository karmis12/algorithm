def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1, len(nums)):
                num=nums[i]+nums[j]+nums[k]
                list=[]
                for z in range(1,num+1):
                    if num%z==0:
                        list.append(z)
                if len(list)==2:
                    answer+=1
    return answer
