class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.points = int(self.goals) + int(self.assists)
    
    def __str__(self):
        return f"{self.name:20} team {self.team:5} {self.goals} + {self.assists} = {self.points}"
