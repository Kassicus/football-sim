from termcolor import colored
import pickle
import os
import pygame

import team
import lib

pygame.init()

class Window():
    def __init__(self) -> None:
        self.screen = lib.display_surface
        pygame.display.set_caption("Football Simulator")

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self):
        lib.events = pygame.event.get()

        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill(lib.color.BLACK)

    def update(self):
        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.fps_limit) / 1000

class Prog():
    def __init__(self) -> None:
        self.running = True

        self.load_team_list = {}
        
        try:
            with open("data/teams/load_ref.ksf", "rb") as save_team_list:
                self.load_team_list = pickle.load(save_team_list)
        except:
            pass
        
        self.team_list = {}

        self.menu_prompt = colored(">> ", "green", attrs=["bold"])

        self.commands = {
            "create": self.create_team,
            "view": self.view_teams,
            "exit": self.terminate,
            "reset": self.reset_teams,
            "help": self.help,
            "clear": self.clear_screen,
            "play": self.play_game,
            "edit": self.edit_team
        }

    def help(self) -> None:
        print("""
        create: create a new team
        view: view all existing teams
        reset: remove all existing teams
        clear: clear the screen
        play: play a game
        edit: edit a team

        exit: terminate the program (saves automatically)
        help: display this prompt
        """)

    def clear_screen(self) -> None:
        for x in range(150):
            print("\n")

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

    def play_game(self) -> None:
        home_team = input("Home Team: ")

        if home_team in self.team_list:
            home_score = self.team_list[home_team].play_game()
            home_display = colored(home_score, "blue", attrs=["bold"])

        away_team = input("Away Team: ")

        if away_team in self.team_list:
            away_score = self.team_list[away_team].play_game()
            away_display = colored(away_score, "red", attrs=["bold"])

        if home_score > away_score:
            self.team_list[home_team].all_time_wins += 1
            self.team_list[away_team].all_time_losses += 1
        elif home_score == away_score:
            self.team_list[home_team].all_time_ties += 1
            self.team_list[away_team].all_time_ties += 1
        else:
            self.team_list[home_team].all_time_losses += 1
            self.team_list[away_team].all_time_wins += 1

        print("Final Score", home_display, home_team, "to", away_display, away_team)

    def edit_team(self) -> None:
        self.view_teams()
        user_in = input("Enter a team code: ")

        if user_in in self.team_list:
            self.team_list[user_in].edit()

    def run(self) -> None:
        while self.running:
            self.menu()

    def terminate(self) -> None:
        self.save_teams()
        self.running = False

    def menu(self) -> None:
        user_in = input(self.menu_prompt)
        if user_in in self.commands:
            self.commands[user_in]()
        else:
            print("Invalid Command...\n")

if __name__ == '__main__':
    win = Window()
    win.run()
    pygame.quit()