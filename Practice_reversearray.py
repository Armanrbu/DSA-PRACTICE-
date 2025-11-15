# if we want to reverse full array

def func(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    func(arr,left+1,right-1)

def recursivearr(arr):
    func(arr,0,len(arr)-1)
    return arr

a = recursivearr(arr= [1,2,3,4,7,9,0])

print(a)

# if we want to reverse from specific index

def funa(arr,left,right):
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    funa(arr,left+1,right-1)

def reversarray(arr,left,right):
    funa(arr,left,right)
    return arr

aa = reversarray([1,2,3,4,5,6,7,8,9,0],0,3)

print(aa)