import json

class GameStats:
    """ Track statistics for Alien Invasion """

    def __init__(self, ai_game):
        """ Initialize statistics """
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score_file = "high_score.json"
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """ Initialize statistics that can change during the game """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self):
        """ Reads the high score from the json file """
        high_score = 0
        with open(self.high_score_file) as json_file:
            data = json.load(json_file)
            high_score = data["high_score"]
        return high_score

    def save_high_score(self):
        with open(self.high_score_file, 'w') as outfile:
            json.dump({"high_score": self.high_score}, outfile)
