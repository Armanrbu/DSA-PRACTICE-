"""Print 1 t0 N using Head recursion"""

def func(i,n):
    if i > n:
        return
    print(i)
    func(i+1,n)

func(0,10)


"""Print a specific no n times"""

def funa(n,times):
    if times == 0:
        return
    print(n)
    funa(n,times-1)

funa(2,3)

"""Print N to 1 using head recursion"""

def funnb(n):
    if n == 0:
        return
    print(n)
    funnb(n-1)

funnb(12)

"""Print 1 to N Using tail recursion"""

def func(n):
    if n == 0:
        return
    func(n-1)
    print(n)

func(3)

"""Print N to 1 using Tail recursion"""

def funs(i,n):
    if i > n:
        return
    funs(i+1,n)
    print(i)

funs(2)