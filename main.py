import team

teams = {}

running = True

def create_team() -> None:
    in_city = str(input("Enter a City: "))
    in_name = str(input("Enter a Team Name: "))
    in_abbr = str(input("Enter a Team Abbreviation: "))

    t = team.Team(in_city, in_name, in_abbr)

    teams[in_abbr] = t

def view_teams() -> None:
    for team in teams:
        print(teams[team].city, teams[team].name, teams[team].abbr)

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
            running = False
        else:
            raise Exception("Input out of range")

if __name__ == '__main__':
    menu()