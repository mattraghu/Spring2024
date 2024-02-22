a = 0
b = 1

n = int(input("Enter the number of terms: "))
print(a)

for i in range(1, n):
    print(b)
    a, b = b, a + b