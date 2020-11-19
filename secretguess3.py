import json
import random
import datetime

# for future use
class Results():

    def __init__(self, score, player_name, date=None):
        self.score = score
        self.player_name = player_name
        if date == None:
            date = datetime.datetime.now()
        self.date = date

class ScoreList:

    def __init__(self):
        self.score_list = []

    def load(self):
        with open("score_list.txt", "r") as score_file:
            self.score_list = json.loads(score_file.read())
    
    def add_score(self, user, attempts):
        rec = [attempts, str(datetime.datetime.now()), user]
        self.score_list.append(rec)

    def get_top_scores(self):
        l = self.score_list.copy()
        l.sort()
        return l[:5]

    def store(self):
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(self.score_list, indent=4))


def play_game2(scores):
    user = input("What's your name? ").strip()
    secret = random.randint(1, 30)
    attempts = 0

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            scores.add_score(user, attempts)
            scores.store()
            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

def print_top_scores2(scores):
    print("Top scores:")
    top = scores.get_top_scores()
    for score in top:
        attempts, date, user = score
        print("\tuser:", user, "attempts:", attempts, "date:", date)

def main():
    scores = ScoreList()
    scores.load()

    while True:
        selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit? ")

        if selection == "A":
            play_game2(scores)
        elif selection == "B":
            print_top_scores2(scores)
        else:
            break

main()


