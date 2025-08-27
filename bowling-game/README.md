# Bowling game kata

## Context and requirements

The game consists of 10 frames. In each frame the player has two rolls to 
knock down 10 pins. The score for the frame is the total number of pins 
knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two rolls. The bonus for 
that frame is the number of pins knocked down by the next roll.

A strike is when the player knocks down all 10 pins on his first roll. The 
frame is then completed with a single roll. The bonus for that frame is the 
value of the next two rolls.

In the tenth frame a player who rolls a spare or strike is allowed to roll the 
extra balls to complete the frame. However no more than three balls can be 
rolled in tenth frame.

### Classes & methods

Write a class `Game` that has two methods:

- `roll(pins_hit: int) -> None` is called each time the player rolls a ball. 
The argument is the number of pins knocked down.
- `score() -> int` returns the total score for that game.

## Test list

- [ ] A player's score is the sum of all normal rolls (no spares/strikes)
- [ ] A player cannot roll after a game finishes
- [ ] After a spare, the player's next roll should count double
- [ ] After a strike, the frame should end and the player's next two rolls should count double