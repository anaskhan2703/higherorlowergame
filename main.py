import random

userguess = 0
roundnumber = 1

print("Welcome to high or low number guessing game.")
minimum = int(input("What is the minimum number?: "))
maximum = int(input("What is the maximum number?: "))
randomnumber = random.randint(minimum, maximum)

while roundnumber < 10:
    print(f"Current try: {roundnumber}")
    userguess = int(input("Guess the number: "))
    if userguess == randomnumber:
        print(f"Congratulations! You won in {roundnumber} tries!\n The number was {randomnumber}")
        break
    elif userguess != randomnumber:
        roundnumber += 1
        if userguess > randomnumber:
            print("Guess was too high, try again ")
        elif userguess < randomnumber:
            print("Guess was too low, try again ")
print(f"You lost! You went through {roundnumber} tries without getting the correct guess.\nThe number was {randomnumber}")
