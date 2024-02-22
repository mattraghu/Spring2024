def expo(n, e):
    result = 1
    for i in range(e):
        result *= n
    return result

print(expo(7, 3))

def expo(n, e):
    if e == 0:
        return 1
    else:
        return n * expo(n, e - 1)
    
print(expo(7, 3))