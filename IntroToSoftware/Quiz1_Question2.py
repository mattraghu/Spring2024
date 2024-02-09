def find_factorial():
    num = int(input("Enter a number: "))

    factorial = 1

    if num < 0:
        print("ERROR: Factorial does not exist for negative numbers")
        return


    for i in range(1, num+1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

find_factorial()