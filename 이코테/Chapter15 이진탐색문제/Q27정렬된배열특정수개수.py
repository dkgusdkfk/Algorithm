n, x = map(int, input().split())

data = list(map(int, input().split()))

def start(array, target, s, e):
    while s <= e:
        mid = (s+e)//2
        if array[mid] == target and array[mid-1] != target:
            return mid
        elif array[mid]<target:
            s = mid+1
        else:
            e = mid-1
    return -1

def end(array, target, s, e):
    while s <= e:
        mid = (s+e)//2
        if array[mid] == target and array[mid+1] != target:
            return mid
        elif array[mid]>target:
            e = mid-1
        else:
            s = mid+1
    return -1

s = start(data, x, 0, n-1)
if s==-1:
    print(s)
else:
    e = end(data, x, s, n-1)

    result = e-s+1
    print(result)