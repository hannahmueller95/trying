import json
import random
from datetime import datetime

user = input("What's your name? ").strip()
secret = random.randint(1, 30)
attempts = 0
wrong_guesses = dict()

with open("score_list.txt", "r") as score_file:
    s = score_file.read()
    score_list = json.loads(s)

with open("wrong_guesses.txt", "r") as f:
    s = f.read().strip()
    if s != '':
        wrong_guesses = json.loads(s)

score_list.sort()
mywrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    mywrong_guesses.append(guess)

now = str(datetime.now())
record = [attempts, now, user]
score_list.append(record)
with open("score_list.txt", "w") as score_file:
    score_file.write(json.dumps(score_list))

wrong_guesses[user] = mywrong_guesses
with open("wrong_guesses.txt", "w") as f:
    f.write(json.dumps(wrong_guesses))

with open("score_list.txt", "r") as score_file:
    json_str = score_file.read()
    score_list = json.loads(json_str)

score_list.sort()

for score in score_list[:3]:
    print(score)

