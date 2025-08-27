class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins_hit: int) -> None:
        if len(self.rolls) < 20:
            self.rolls.append(pins_hit)

    @property
    def score(self) -> int:
        return sum(self.rolls)