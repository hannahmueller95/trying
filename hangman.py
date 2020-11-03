word = secret
guesses = None
turns = 10
while turns > 0:
    failed = None
guess = input("guess a character:")

for char in word:
    if char in guesses:
        print(char)
    else:
        print("Sorry")




guesses += guess

if guess not in word:
    turns =- 1
    print("You have", + turns, 'more guesses')

if turns == 0
    print("you Lose")
    break
