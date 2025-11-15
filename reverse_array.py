"""array reverse"""

def func(arr,left,right):
    # n = [1,2,3]
    # l = 0
    # r = len(n)-1
    if left >= right:
        return
    arr[left],arr[right] = arr[right],arr[left]
    func(arr,left+1,right-1)


def reversearr(arr,left,right):
    func(arr,left,right)
    return arr

# def reversearrallelement(arr):
#     # func(arr,0,len(arr)-1)          // for all elements
#     return arr

n = [1,3,5,7,9,0,2]

a = reversearr(n,1,3)
print(a)