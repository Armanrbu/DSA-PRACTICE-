nums = [1,1,1,2,2,3,4,5,5,5,5,6,6,6,7,8,9]

# Brutteforce
# n = len(nums)
# freq = {}
# for i in range(0,n):
#     freq[nums[i]] = 0

# j = 0

# for k in freq:
#     nums[j] = k
#     j+=1

# print(nums)


# Optimal try
def check(nums):
    n = len(nums)
    i = 0
    j = i + 1
    if n == 1:
        return 1
    while(j < n):
        if nums[i] == nums[j]:
            j+=1
        if nums[i] != nums[j]:
            i+=1
            nums[i],nums[j] = nums[j],nums[i]
            j+=1
    return i + 1
    

a = check(nums)
print(a)

