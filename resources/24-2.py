# find the first missing positive entry


def fmpe(arr):
    n = len(arr)
    for i in range(len(arr)):
        k = arr[i]
        while (1 <= k <= n) and (arr[k-1] != arr[i]):
            k = arr[i]
            arr[k-1], arr[i] = k, arr[k-1]
    for i in range(len(arr)):
        if arr[i] != (i+1):
            return i+1
    return n+1


print(fmpe([3,5,4,-1,5,1,-1])) # 2
print(fmpe([1,2,3,4,5])) # 6
print(fmpe([-3,-2,-1])) # 1
print(fmpe([0])) # 1
print(fmpe([1,3,3,4])) # 2