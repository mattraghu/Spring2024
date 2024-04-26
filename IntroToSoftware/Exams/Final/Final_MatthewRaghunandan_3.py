import time

def function1(n):
    if n <= 1:
        return n
    else:
        return function1(n-1) + function1(n-2)
    
# n = int(input("Input num: "))
# print(function1(n))

def function2(n): # start at 1 
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c

        return b

# n = int(input("Input num: "))
# print(function2(n))


start = time.time()
print(function1(30))
end = time.time()
print(f"Time taken for function1: {end-start}")

start = time.time()
print(function2(30))
end = time.time()
print(f"Time taken for function2: {end-start}")