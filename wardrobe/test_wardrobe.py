import pytest

from wardrobe import wardrobe

# Tuple of arguments to the function under test followed by the expected
# output
arguments_and_results = [
    (
        ({50}, 50),
        [(50, )]
    ),
    (
        ({25}, 50),
        [(25, 25)]
    ),
    (
        ({50}, 25),
        []
    ),
    (
        ({10, 25}, 35),
        [(10, 25)]
    ),
    (
        ({10, 15, 50}, 60),
        [
            (10, 10, 10, 10, 10, 10),
            (10, 10, 10, 15, 15),
            (10, 50),
            (15, 15, 15, 15),
        ]
    ),
    (
        ({50, 75, 100, 120}, 250),
        [
            (50, 50, 50, 50, 50),
            (50, 50, 50, 100),
            (50, 50, 75, 75),
            (50, 100, 100),
            (75, 75, 100),
        ]
    ),
]

@pytest.mark.parametrize(
    "arguments, expected",
    arguments_and_results
)
def test_compute_configurations(arguments, expected):
    elements, wall_length = arguments
    actual = wardrobe.compute_configurations(elements, wall_length)
    assert actual == expected