#Recursive Procedure for implementing Fibonacci numbers

def fib(n):
    if n < 2: #base cases
        f = n
    else:
        f1 = fib(n-1)
        f2 = fib(n-2)
        f = f1 + f2
    return f

#testing

print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))


# HW Problem! Implement this problem only using while loop to see the relationship between recursion and while loops.

#also, for test, practice changing intList keysearch to recursion.

def wfib(n):
    ans = -1
    f1 = 0  #base cases
    f2 = 1

    if n == 1: #base case checks
        ans = 1
    elif n == 0:
        ans = 0

    while n > 1: #since we have base cases for fib0 and fib1
        f = f1+f2 #adding the 2 previous fibs to create the next
        f1 = f2  
        f2 = f  
        n -= 1
        ans = f

    return ans

#testing

print(wfib(1))
print(wfib(2))
print(wfib(3))
print(wfib(4))
print(wfib(5))
print(wfib(6))


