def isFibbonacci(num):
    a = 0
    b = 1
    while a < num:
        a, b = b, a + b
    return a == num

num = input("Enter a number: ")
num = float(num)
print(isFibbonacci(num))