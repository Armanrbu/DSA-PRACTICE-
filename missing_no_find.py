# brute force soln

num = [4,2,1,0]

# n = len(num)

# for i in range(0,n+1):
#     if i not in num:
#         print(i)


#better soln using dic

# n = len(num)
# freq ={}

# for i in range(0,n+1):
#     freq[i] = 0

# for na in num:
#     freq[na] = 1

# for k,v in freq.items():
#     if v == 0:
#         print(k)



# Optimal solution

# using loop to calculate sum

n = len(num)
sum = 0

#U can use any loop given below to find the sum

for i in num:           #with for in 
    sum = i + sum

# for i in range(0,n+1):
#     sum = sum + i                  #with for range loop
# print(sum)

# print(n*(n+1)//2 - sum)



# Optimal solution on-line

#using in-built sum()

print(n*(n+1)//2 - sum(num))