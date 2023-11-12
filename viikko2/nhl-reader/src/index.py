import requests
import operator
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url).json()

    def create_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nat):
        players_by_nat = []
        for player in self.reader:
            if player.nationality == nat:
                players_by_nat.append(player)
        players_by_nat.sort(key=operator.attrgetter('points'), reverse=True)
        return players_by_nat

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url).create_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")
    for player in players:
        print(player)



if __name__ == "__main__":
    main()
