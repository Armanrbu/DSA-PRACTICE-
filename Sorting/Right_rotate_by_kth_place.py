#My own code not optimal

nums = [1,2,3,4,5,6,7,8,9]

# k = 11
# n = len(nums)
# rotation = k % n
# j = 0
# while(j < rotation):
#     temp = nums[n-1]
#     for i in range(n-2,-1,-1):
#         nums[i+1] = nums[i]
#     nums[0] = temp
#     j+=1

# print(nums)

# # Brute force

# for _ in range(0,k):
#     e = nums.pop()
#     nums.insert(0,e)


# # little optimal Solution

# rotation = k % n

# for _ in range(0,rotation):
#     e = nums.pop()
#     nums.insert(0,e)


#Better 

n = len(nums)
k = 100
k = k % n

print(id(nums)) # just testing is there ids same or not when ":" is used
nums[:] = nums[n-k:] + nums[:n-k]

print(id(nums))

#Without Slicing

