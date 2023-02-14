from termcolor import colored
import random

def get_score() -> int:
    score = 0

    drives = random.randint(10, 12)

    for x in range(drives):
        did_score = random.randint(0, 1)

        if did_score == 1:
            did_touchdown = random.randint(0, 1)
            if did_touchdown == 1:
                score += 6
                did_pat = random.randint(1, 100)
                if did_pat <= 94:
                    score += 1
            else:
                score += 3

    return score

home_score = colored(get_score(), "blue", attrs=["bold"])
away_score = colored(get_score(), "red", attrs=["bold"])

print("Final Score", home_score, "to", away_score)