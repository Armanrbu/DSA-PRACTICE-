# brute force soln

# num = [4,2,1,0]

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