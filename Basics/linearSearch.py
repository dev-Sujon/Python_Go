arr = [2,1,8,9,10,100,30,90,51,13,44,20,56,88] #array declaration & initialization
target = 2

def linearSearch(arr,x):
    print("Array :",arr)
    print("Target :",x)
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
res = linearSearch(arr,target)

if res == -1:
    print("Not found in the array")
else:
    print(target,"is found in the array of ",res)
