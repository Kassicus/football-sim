from termcolor import colored
import random
import pickle

class Team():
    def __init__(self) -> None:
        self.city = ""
        self.name = ""
        self.abbr = ""

        self.min_drives = 0
        self.max_drives = 0

        self.score_percent = 0
        self.touchdown_percent = 0
        self.pat_percent = 0

    def save_team_data(self, file_loc) -> None:
        team_data = {
            'city': self.city,
            'name': self.name,
            'abbr': self.abbr,
            'min_drives': self.min_drives,
            'max_drives': self.max_drives,
            'score_percent': self.score_percent,
            'touchdown_percent': self.touchdown_percent,
            'pat_percent': self.pat_percent
        }

        with open(file_loc, 'wb') as save_file:
            pickle.dump(team_data, save_file)

    def load_team_data(self, file_loc) -> None:
        with open(file_loc, "rb") as save_file:
            team_data = pickle.load(save_file)

        self.city = team_data['city']
        self.name = team_data['name']
        self.abbr = team_data['abbr']
        self.min_drives = team_data['min_drives']
        self.max_drives = team_data['max_drives']
        self.score_percent = team_data['score_percent']
        self.touchdown_percent = team_data['touchdown_percent']
        self.pat_percent = team_data['pat_percent']

    def set_default_stats(self) -> None:
        self.min_drives = 10
        self.max_drives = 12

        self.score_percent = 50
        self.touchdown_percent = 50
        self.pat_percent = 94

    def display(self) -> None:
        print(self.city, self.name, self.abbr)

    def edit(self) -> None:
        editing = True

        print("1 - City: ", self.city)
        print("2 - Name: ", self.name)
        print("3 - Abbreviation: ", self.abbr)
        print("4 - Min Drives: ", self.min_drives)
        print("5 - Max Drives: ", self.max_drives)
        print("6 - Score Percent: ", self.score_percent)
        print("7 - Touchdown Percent: ", self.touchdown_percent)
        print("8 - PAT Percent: ", self.pat_percent)
        print("9 - End Editing Team")

        user_in = int(input("Which stat would you like to edit? "))

        match user_in:
            case 1:
                city = input("Enter new City: ")
                self.city = city
            case 2:
                name = input("Enter new Name: ")
                self.name = name
            case 3:
                abbr = input("Enter new Abbreviation: ")
                self.abbr = abbr
            case 4:
                min_drives = int(input("Enter new Min drives: "))
                self.min_drives = min_drives
            case 5:
                max_drives = int(input("Enter new Max drives: "))
                self.max_drives = max_drives
            case 6:
                score = int(input("Enter a new Score Percentage: "))
                self.score_percent = score
            case 7:
                touchdown = int(input("Enter a new Touchdown Percentage: "))
                self.touchdown_percent = touchdown
            case 8:
                pat = int(input("Enter a new PAT Percentage: "))
                self.pat_percent = pat
            case 9:
                editing = False

        if editing:
            self.edit()

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