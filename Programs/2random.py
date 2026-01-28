import random

secret = random.randint(1, 100)
count = 0
max_attempts = 10

while count < max_attempts:
    i = int(input("Enter a number: "))

    if i == secret:
        print("🎉 You won!")
        print(f"Your score is {max_attempts - count}")
        break
    elif i > secret:
        print("Too big")
    else:
        print("Too small")

    count += 1

if count == max_attempts:
    print("❌ You lost!")
    print(f"The number was {secret}")
