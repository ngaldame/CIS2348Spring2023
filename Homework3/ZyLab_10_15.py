# Nathan Galdamez Gomez, 2141118
# This is ZyLab 10.15

# This is a class called Team
class Team:
    def __init__(self):
        self.teamname = 'None'
        self.team_wins = 0
        self.team_losses = 0

    # Define get_win_percentage function
    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


# This is the driver code
if __name__ == '__main__':
    # Create an object of the Team class
    team = Team()
    # Get inputs for team name, team wins, and team losses
    name = str(input())
    wins = int(input())
    losses = int(input())
    # Call get_win_percentage function and print win percentage
    team.teamname = name
    team.team_wins = wins
    team.team_losses = losses

    # Print win percentage
    if team.get_win_percentage() > 0.5:
        print(f'Congratulations, Team {name} has a winning average!')
    else:
        print(f'Team {name} has a losing average.')
