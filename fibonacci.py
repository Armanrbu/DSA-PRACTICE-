" 0, 1, 1, 2, 3, 5, 8, 13, 36, 49"

def fibo(i,j,a,n):
    if i >= n:
        return a
    a = a + j
    return fibo(i+1,j+1,a,n)

a = fibo(0,1,0,2)
print(a)