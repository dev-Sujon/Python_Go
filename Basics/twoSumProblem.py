
def twoSum(n,t):
    for i in range(len(n)):
        for j in range(i+1,range(n)):
            if (n[i]+n[j]) == t:
                return [i,j]


nums =[2, 7, 11, 15]
target = 9
res = twoSum(nums,target)
print(res)
