import pytest

import bowling

@pytest.fixture
def game():
    return bowling.Game()

def test_after_two_normal_roles_score_is_sum_of_rolls(game):
    game.roll(3)
    game.roll(5)
    assert game.score == 8

def test_after_ten_roles_game_is_finished(game):
    for _ in range(20):
        game.roll(4)
    # score is now 80
    game.roll(8)  # roll should be ignored: game is finished
    assert game.score == 80

"""
def test_after_a_spare_count_next_roll_double(game):
    game.roll(6)
    game.roll(4)  # spare
    game.roll(3)  # counts double
    assert game.score == 16
"""