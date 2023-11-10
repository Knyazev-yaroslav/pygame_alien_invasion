class GameStats:


    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = self._get_high_score()


    def _get_high_score(self):
        with open('high_score.txt', 'r') as hs:
            high_score = hs.read()
        if high_score:
            return int(high_score)
        else:
            return 0


    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
