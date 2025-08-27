class Game:
    def __init__(self):
        self.score = 0

    def roll(self, pins_hit: int) -> None:
        self.score += pins_hit