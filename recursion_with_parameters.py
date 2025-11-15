"""Print a number n times using recursion"""

def fun(x,n):
    if n == 0:
        return
    print(x)
    fun(x,n-1)

# fun(15,4)

"""Print 1 to N using Head Recursion"""

def func(i,N):
    if i > N:
        return
    print(i)
    func(i+1,N)

# func(1,4)



"""Print N to 1 using Tail Resursion """

def funca(i,n):
    if i > n:
        return

    funca(i+1,n)
    print(i)

# funca(1, 4)

"""Print N to 1 using Head Resursion """

def funsa(i):
    if i == 0:
        return
    print(i)
    funsa(i-1)

# funsa(5)


"""Print 1 to N using Tail Resursion """

def fun12(i):
    if i == 0:
        return
    fun12(i-1)
    print(i)

fun12(4)