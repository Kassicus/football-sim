import pickle
import os

import team

class Prog():
    def __init__(self) -> None:
        self.running = True

        self.load_team_list = {}
        
        with open("data/teams/load_ref.ksf", "rb") as save_team_list:
            self.load_team_list = pickle.load(save_team_list)
        
        self.team_list = {}

        self.commands = {
            "create": self.create_team,
            "view": self.view_teams,
            "exit": self.terminate,
            "reset": self.reset_teams
        }

    def load_team(self) -> None:
        for abbr in self.load_team_list:
            t = team.Team()
            t.load_team_data("data/teams/" + abbr + ".ksf")
            self.team_list[abbr] = t

    def save_teams(self) -> None:
        for team in self.team_list:
            self.team_list[team].save_team_data("data/teams/" + team + ".ksf")

        with open("data/teams/load_ref.ksf", "wb") as save_team_list:
            pickle.dump(self.load_team_list, save_team_list)

    def create_team(self) -> None:
        city = input("Enter a City: ")
        name = input("Enter a Name: ")
        abbr = input("Enter an Abbreviation: ")

        t = team.Team()

        t.city = city
        t.name = name
        t.abbr = abbr
        t.set_default_stats()

        self.team_list[abbr] = t
        self.load_team_list[abbr] = abbr

    def view_teams(self) -> None:
        for team in self.team_list:
            self.team_list[team].display()

    def reset_teams(self) -> None:
        for abbr in self.load_team_list:
            if os.path.exists("data/teams/" + abbr + ".ksf"):
                os.remove("data/teams/" + abbr + ".ksf")

        self.load_team_list = {}
        self.team_list = {}

    def run(self) -> None:
        while self.running:
            self.menu()

    def terminate(self) -> None:
        self.save_teams()
        self.running = False

    def menu(self) -> None:
        user_in = input(">> ")
        if user_in in self.commands:
            self.commands[user_in]()
        else:
            print("Invalid Command...\n")

if __name__ == '__main__':
    prog = Prog()
    prog.load_team()
    prog.run()