nums = [1,2,3,4,5,9,10]
target = 90

n = len(nums)
index = 0
for i in range(0,n):
    if nums[i] == target:
        break
    index +=1
    
        
print(index)

