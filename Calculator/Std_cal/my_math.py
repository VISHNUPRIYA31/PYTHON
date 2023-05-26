name = "python"
def add (a,b,c):
    return a+b+c
def mul(a,b):
    return a*b
def inc(y):
    return y+50
def fact(n):
    f = 1
    for i in range(n,0,-1):
        f = f * i
    return f
def digit_count(n):
    c = 0
    while n!=0:
        n = n//10
        c += 1
    return c
def num_rev(n):
    new_num = 0 
    while n!=0:
        l_d = n%10
        new_num = new_num *10 + l_d
        n //= 10
    return new_num
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
#fibonacci series generation using for loop 
def fibo_for(n):
    a = 0
    b = 1
    print(a,b,end = ",",sep=",")
    for i in range(2,n):
        c = a+b
        print(c,end=",")
        a = b
        b = c
#fibonacci series generation using for recursion
def fibo_rec(n):
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

def pow_rec(b,p):
    if p == 1:
        return b
    else:
        return b * pow_rec(b,p-1)
