from random import randint

secret = randint(1, 10)
# print(secret)
isWin = False
i = 0

while i < 3 and not isWin:
    i += 1
    print(f"próba {i}: ", end="")
    attempt = int(input())
    if secret == attempt:
        isWin = True

if isWin:
    print("You win")
else:
    print("You lose")
