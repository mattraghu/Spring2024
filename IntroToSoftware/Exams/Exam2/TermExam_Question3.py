def calculatePi(n,currentSum=0,i=0):
    
    if i == n:
        return currentSum*4
    elif i == 0:
        return calculatePi(n,1,1)
    else:
        currentSum = currentSum + ((-1)**i)*(3+2*(i-1))**-1
        return calculatePi(n,currentSum,i+1)
    
n = input("Enter the number of terms: ")
n = int(n)
print(calculatePi(n))