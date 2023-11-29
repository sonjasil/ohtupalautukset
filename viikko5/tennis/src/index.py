from tennis_game import TennisGame


def main():
    game = TennisGame("player1", "player2")

    print(game.get_current_score())

    game.add_point_to_point_winner("player1")
    print(game.get_current_score())

    game.add_point_to_point_winner("player1")
    print(game.get_current_score())

    game.add_point_to_point_winner("player2")
    print(game.get_current_score())

    game.add_point_to_point_winner("player1")
    print(game.get_current_score())

    game.add_point_to_point_winner("player1")
    print(game.get_current_score())


if __name__ == "__main__":
    main()
