import datetime
import json
import random
import datetime


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
    return score_list

def print_top_scores():
    print("Top scores:")
    score_list = get_score_list()
    score_list.sort()
    for score in score_list[:3]:
        attempts, date, user = score
        print("\tuser:", user, "attempts:", attempts, "date:", date)

def store_score(user, attempts):
    rec = [attempts, str(datetime.datetime.now()), user]
    score_list = get_score_list()
    score_list.append(rec)
    with open("score_list.txt", "w") as score_file:
        score_file.write(json.dumps(score_list, indent=4))

def play_game():
    user = input("What's your name? ").strip()
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            store_score(user, attempts)
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

def main():
    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection == "A":
            play_game()
        elif selection == "B":
            print_top_scores()
        else:
            break
class results():
    def __int__(self, score, player_name, date):


main()

score_file =
with open("score_list.txt", "w" ) as score_file:
    score_file.write(str(score_data.__dict__))