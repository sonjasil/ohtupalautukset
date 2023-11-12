import requests
import operator
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    print("Players from FIN:\n")    

    players = []

    for player_dict in response:
        if player_dict['nationality'] == "FIN":
            player = Player(player_dict)
            players.append(player)

    #print("Oliot:")
    
    players.sort(key=operator.attrgetter('points'), reverse=True)

    for player in players:
        print(player)


if __name__ == "__main__":
    main()
