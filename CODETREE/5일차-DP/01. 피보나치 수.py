n = int(input())
check = [0 for i in range(n+1)]

def fib(n):
    if check[n-1] != 0:
        return check[n-1]
    if n == 1:
        return 1
    elif n ==2:
        return 1
    check[n-1] =  fib(n - 1) + fib(n - 2)
    return check[n-1]
print(fib(n))