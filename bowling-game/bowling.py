class Game:
    def __init__(self):
        self.frames = []

    def roll(self, pins_hit: int) -> None:
        if self._game_finished:
            return  # silently ignore rolls after a game finishes

        if self._first_roll or not self._frame_in_progress:
            self.frames.append([pins_hit])  # create a new frame
        else:
            self.frames[-1].append(pins_hit)  # append to existing frame

    def score(self) -> int:
        return sum(sum(frame) for frame in self.frames)

    @property
    def _game_finished(self) -> bool:
        if self._first_roll:  # avoid IndexError in case of no frames
            return False
        last_frame = self.frames[-1]  # this IndexError
        return len(self.frames) == 10 and (
                len(last_frame) == 2 or
                sum(last_frame) == 10
        )

    @property
    def _first_roll(self) -> bool:
        return not self.frames

    @property
    def _frame_in_progress(self) -> bool:
        last_frame = self.frames[-1]
        return len(last_frame) == 1 and sum(last_frame) != 10