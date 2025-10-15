arr=[]
n = int(input("Enter number of element:"))
for i in range(0,n):
    ele= int(input())
    arr.append(ele)
print(arr)
target=int(input("Enter seach number:"))
##linear search
def linearSearch(a,x):
    for i in range(n):
        if a[i]==x:
            return i
    return -1
res = linearSearch(arr,target)
print(res)

