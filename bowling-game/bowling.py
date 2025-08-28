class Game:
    def __init__(self):
        self.frames: list[Frame] = []

    def roll(self, pins_hit: int) -> None:
        if self._game_finished:
            return  # silently ignore rolls after a game finishes

        if not self.frames:
            # First roll of the game
            self.frames.append(Frame(pins_hit))
        elif self.frames[-1].is_complete:
            # Start a new frame
            self.frames.append(Frame(pins_hit))

            # Add bonus for spare in previous frame
            if len(self.frames) > 1 and self.frames[-2].is_spare:
                # Use the actual pins_hit value directly as a bonus
                self.frames[-2].rolls.append(pins_hit)
        else:
            # Add roll to current frame
            self.frames[-1].add_roll(pins_hit)

    def score(self) -> int:
        return sum(frame.score for frame in self.frames)

    @property
    def _game_finished(self) -> bool:
        if not self.frames:  # No frames yet
            return False
        return len(self.frames) == 10 and self.frames[-1].is_complete

    @property
    def _last_frame(self):
        if not self.frames:
            return None
        return self.frames[-1]


class Frame:
    def __init__(self, first_roll=0):
        self.rolls = [first_roll]

    def add_roll(self, pins):
        self.rolls.append(pins)

    @property
    def is_complete(self):
        return len(self.rolls) >= 2 or self.is_strike

    @property
    def is_strike(self):
        return len(self.rolls) == 1 and self.rolls[0] == 10

    @property
    def is_spare(self):
        return len(self.rolls) == 2 and self.score == 10

    @property
    def score(self):
        return sum(self.rolls)