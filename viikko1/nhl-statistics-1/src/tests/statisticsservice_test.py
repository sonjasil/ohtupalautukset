import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_works(self):
        result = self.stats.search("Semenko")

        self.assertAlmostEqual(result.name, "Semenko")

    def test_team_search(self):
        result = []
        for player in self.stats.team("EDM"):
            result.append(player.name)

        self.assertAlmostEqual(result, ["Semenko", "Kurri", "Gretzky"])

    def test_top_search(self):
        result = self.stats.top(1)

        self.assertAlmostEqual(result[0].name, "Gretzky")
