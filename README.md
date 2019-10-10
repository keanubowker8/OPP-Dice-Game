# Assignment 1. Rolling multi-sided dice
## Description of the task
A normal die (the singular of dice) is a cube, and each face shows a number from one to six. Some games employ nonstandard dice that may have fewer (e.g. four) or more (e.g. thirteen) sides. Let’s design a general class MultiSidedDie to model multi-sided dice. We could use such an object in any number of simulation or game programs. Each MultiSidedDie object will know two things:

1) How many sides it has
2) Its current value
When a new MultiSidedDie is created, specify how many sides it will have (e.g number_of_sides). The die can be operated on through three provided methods: roll, to set the die to a random value between 1 an number_of_sides, exclusively; set_value, to set the die to a specific value (i.e cheat); and get_value to see what current value is.

## Steps
Copy the following code into a script called multi_sided_die.py:

```#class definition for an n-sided die

#import packages

class MultiSidedDie:

  #constructor here

  #define method 'roll' to roll the MultiSidedDie

  #define method 'get_value' to return the current value of the MultiSidedDie

  #define method 'set_value' to set the die to a particular value
  ```
  

Create class MultiSidedDie with attributes number of sides and value.
Create class methods for rolling the die, getting the value of the die and setting the value of the die.


# Assignment 3: Dice Poker
## RULES OF THE GAME
The player starts with \$100.
Each round costs \$10 to play. This amount is subtracted from the player’s money at the start of the round.
The player initially rolls a completely random hand (i.e. all the five dice are rolled).
The player gets two chances to enhance the hand by re-rolling some or all of the dice.
At the end of the hand, the player’s money is updated according to the following payout schedule:
Hand	Pay
Two Pairs	5
Three of a Kind	8
Full House	12
Four of a Kind	15
Straight	20
Five of a Kind	30

## Explanation of the scoring
Two pairs is two sets of pairs, for example two threes and two eights in the same hand. A Full House is a pair and a Three of a Kind in the same hand. Four of a kind is four of the same card, such as four eights. A straight is five numbers in order. So this can be 12345 or 23456. Five of a kind are five of the same number (all sixes for example).

## Instructions
Build a Dice Poker game according to the game rules above. Ultimately, we want this program to present a nice graphical interface. Our interaction will be through mouse clicks. The interface should have the following characteristics:

The current score (amount of money) is constantly displayed.
The program automatically terminates if the player goes broke.
The display may choose to quit at appropriate points during play.
The interface will present visual cues to indicate what is going on at any given moment and what the valid user responses are.
This class has to implement these operations:

Constructor (__init__) - Create the initial collection.
roll - Assign a random value to some subset of the dice while maintaining the current value of others.
value - return the current values of the five dice.
score - return the score for the dice.
