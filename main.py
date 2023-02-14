import team
import pickle

load_team_ref = {}

teams = {}

running = True

def create_team() -> None:
    in_city = str(input("Enter a City: "))
    in_name = str(input("Enter a Team Name: "))
    in_abbr = str(input("Enter a Team Abbreviation: "))

    t = team.Team(in_city, in_name, in_abbr)

    teams[in_abbr] = t
    load_team_ref[in_abbr] = in_abbr

def view_teams() -> None:
    for team in teams:
        print(teams[team].city, teams[team].name, teams[team].abbr)

def save_teams() -> None:
    for team in teams:
        teams[team].save_team_data("data/teams/" + teams[team].abbr + ".ksf")

    with open("data/teams/load_ref.ksf", 'wb') as save_team_ref:
        pickle.dump(load_team_ref, save_team_ref)

def load_teams() -> None:
    global load_team_ref
    with open("data/teams/load_ref.ksf", "rb") as save_team_ref:
        load_team_ref = pickle.load(save_team_ref)

def menu() -> None:
    global running
    while running:
        in_user = int(input("""
        1. Create Team
        2. View Teams
        3. Exit
        """))

        if in_user == 1:
            create_team()
        elif in_user == 2:
            view_teams()
        elif in_user == 3:
            save_teams()
            running = False
        else:
            raise Exception("Input out of range")

if __name__ == '__main__':
    menu()