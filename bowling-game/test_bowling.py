import pytest

import bowling

def test_after_two_normal_roles_score_is_sum_of_rolls():
    game = bowling.Game()
    game.roll(3)
    game.roll(5)
    assert game.score == 8