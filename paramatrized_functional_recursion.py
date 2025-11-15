"""Sum of 1 to N """

def sum_n(sum,i,n):
    if i > n:
        print(sum)
        return
    sum_n(sum + i,i+1,n)

# sum_n(0,1,4)

"""functional recursion"""

def fuctional_recursion(n):
    if n == 1:
        return 1
    return n + fuctional_recursion(n-1)

a = fuctional_recursion(4)
print(a)