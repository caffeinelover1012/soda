import random

number = random.randint(1, 100)
score = 0

while True:
    guess = int(input("Enter a number between 1-100: "))
    score+=1
    if guess>number:
        print("Too High!")
    elif guess<number:
        print("Too Low!")
    else:
        print(f"Congratulations! You guessed the number in {score} tries.")
        break
    

















