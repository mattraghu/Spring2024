def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            if i != n:
                return False
    return True

start = 0
end = 10

for i in range(start, end+1):
    if isPrime(i):
        print(i)

