class Game:
    def __init__(self):
        self.frames: list[Frame] = []

    def roll(self, pins_hit: int) -> None:
        if self._game_finished:
            return  # silently ignore rolls after a game finishes

        if self._is_new_game:
            self.frames.append(Frame(pins_hit))
        elif self._last_frame.is_complete:
            self.frames.append(Frame(pins_hit))
            self._apply_spare_bonus(pins_hit)
        else:
            self._last_frame.add_roll(pins_hit)
            self._apply_strike_bonus(pins_hit)

    def score(self) -> int:
        return sum(frame.score for frame in self.frames)

    @property
    def _game_finished(self) -> bool:
        if not self.frames:  # No frames yet
            return False
        return len(self.frames) == 10 and self.frames[-1].is_complete

    @property
    def _is_new_game(self) -> bool:
        return not self.frames

    @property
    def _last_frame(self):
        if not self.frames:
            return None
        return self.frames[-1]

    def _apply_spare_bonus(self, pins_hit: int) -> None:
        second_to_last = self.frames[-2]
        if second_to_last.score == 10:
            second_to_last.add_roll(pins_hit)

    def _apply_strike_bonus(self, pins_hit: int) -> None:
        if len(self.frames) < 2:
            return
        second_to_last = self.frames[-2]
        if second_to_last.is_strike:
            second_to_last.add_roll(pins_hit)


class Frame:
    def __init__(self, first_roll):
        self.rolls = [first_roll]

    def add_roll(self, pins):
        self.rolls.append(pins)

    @property
    def is_complete(self):
        return len(self.rolls) >= 2 or self.is_strike

    @property
    def is_strike(self):
        return self.rolls[0] == 10

    @property
    def score(self):
        return sum(self.rolls)