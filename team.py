from termcolor import colored
import random

class Team():
    def __init__(self, city: str, name: str, abbr: str) -> None:
        self.city = city
        self.name = name
        self.abbr = abbr

        self.min_drives = 10
        self.max_drives = 12

        self.score_percent = 50
        self.touchdown_percent = 50
        self.pat_percent = 94

    def play_game(self, loc) -> colored:
        score = 0

        drives = random.randint(self.min_drives, self.max_drives)

        for x in range(drives):
            did_score = random.randint(1, 100)
            if did_score <= self.score_percent:
                did_touchdown = random.randint(1, 100)
                if did_touchdown <= self.touchdown_percent:
                    score += 6
                    did_pat = random.randint(1, 100)
                    if did_pat <= self.pat_percent:
                        score += 1
                else:
                    score += 3
        
        if loc == "home":
            return colored(score, "blue", attrs=["bold"])
        elif loc == "away":
            return colored(score, "red", attrs=["bold"])
        else:
            raise Exception("unexpected token for value: loc")