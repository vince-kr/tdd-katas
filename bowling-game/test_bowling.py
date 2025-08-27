import pytest

import bowling

@pytest.fixture
def game():
    return bowling.Game()

def test_after_two_normal_roles_score_is_sum_of_rolls(game):
    game.roll(3)
    game.roll(5)
    assert game.score() == 8

def test_after_ten_roles_game_is_finished(game):
    for _ in range(20):
        game.roll(4)
    # score is now 80
    game.roll(8)  # roll should be ignored: game is finished
    assert game.score() == 80

def test_after_a_strike_frame_should_end(game):
    game.roll(10)  # first roll is a strike
    for _ in range(18):
        game.roll(0)  # scoring 0 points avoids issues with bonus logic later
    game.roll(6)  # this should be ignored
    assert game.score() == 10

"""
def test_after_a_spare_count_next_roll_double(game):
    game.roll(6)
    game.roll(4)  # spare
    game.roll(3)  # counts double
    assert game.score() == 16
"""