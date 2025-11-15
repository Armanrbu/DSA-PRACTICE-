# brute force soln

num = [4,2,1,0]

n = len(num)

for i in range(0,n+1):
    if i not in num:
        print(i)
