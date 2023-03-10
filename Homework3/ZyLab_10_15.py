# Nathan Galdamez Gomez, 2141118

# This is a class called Team
class Team:
    def __init__(self):
        self.teamname = 'none'
        self.team_wins = 0
        self.team_losses = 0
        
    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return team_wins / (team_wins + team_losses)
            
# This is the driver code
if __name__ == '__main__':
    # Create an object of the Team class
    team = Team()
    # Get inputs for team name, wins, and losses
    name = str(input())
    wins = float(input())
    losses = float(input())
    # TODO: Call get_win_percentage function and print win percentage
    
