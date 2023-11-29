class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def add_point_to_point_winner(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_words_for_even_score(self):
        score_str = ""
        if self.player1_score == 0:
            score_str = "Love-All"
        elif self.player1_score == 1:
            score_str = "Fifteen-All"
        elif self.player1_score == 2:
            score_str = "Thirty-All"
        else:
            score_str = "Deuce"
        return score_str
    
    def get_words_for_win_or_advantage(self):
        score_difference = self.player1_score - self.player2_score
        score_str = ""
        if score_difference == 1:
            score_str = "Advantage player1"
        elif score_difference == -1:
            score_str = "Advantage player2"
        elif score_difference >= 2:
            score_str = "Win for player1"
        else:
            score_str = "Win for player2"
        return score_str
    
    def get_words_for_individual_score(self):
        score_str = ""
        current_players_score = 0
        player1_turn = 1
        player2_turn = 2
        for player_turn in range(player1_turn, player2_turn + 1):
            if player_turn == 1:
                current_players_score = self.player1_score
            else:
                score_str += "-"
                current_players_score = self.player2_score

            if current_players_score == 0:
                score_str += "Love"
            elif current_players_score == 1:
                score_str += "Fifteen"
            elif current_players_score == 2:
                score_str += "Thirty"
            elif current_players_score == 3:
                score_str += "Forty"
        return score_str

    def get_current_score(self):
        current_score_str = ""

        if self.player1_score == self.player2_score:
            current_score_str = self.get_words_for_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            current_score_str = self.get_words_for_win_or_advantage()
        else:
            current_score_str = self.get_words_for_individual_score()

        return current_score_str
