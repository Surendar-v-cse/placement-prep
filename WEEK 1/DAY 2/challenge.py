import random

def game():
    num = random.randint(1,20)
    attempt = 10

    while attempt > 0:
        n = int(input(f"\n{attempt} attempt left , Guess the number btw 1 to 20: "))
        
        if n == num: 
            print(f"Element Found!! Element is {num}")
            break
        elif n > num:
            print("Lower")
        elif n < num:
            print("Higher")

        attempt -= 1
    if attempt == 0:

        print(f"\nAttempt is over , the number is {num}")

game()