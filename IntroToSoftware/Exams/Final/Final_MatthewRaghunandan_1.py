import random 

n = random.randint(1,20)

guessed = False
for i in range(5):
    entry = int(input("Enter a numbers: "))

    if entry == n:
        guessed = True
        break
    elif entry > n:
        print("The number is too high.")
    else: 
        print("The number is too low.")


if guessed: 
    print("Congratulations! You guessed the number!")
else:
    print(f"Sorry, you've run out of attempts. The number was {n}. Better luck next time!")



