import team

team_one = team.Team("Test", "Team A", "AAA")
team_two = team.Team("Test", "Team B", "BBB")

home_score = team_one.play_game("home")
away_score = team_two.play_game("away")

print("Final Score", team_one.abbr, home_score, "to", team_two.abbr, away_score)