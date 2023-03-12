import copy
import random
# Consider using the modules imported above.

# First, create a Hat class in prob_calculator.py. The class should take a variable number of arguments that specify the number of balls of each color that are in the hat. For example, a class object could be created in any of these ways:

# hat1 = Hat(yellow=3, blue=2, green=6)
# hat2 = Hat(red=5, orange=4)
# hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

# A hat will always be created with at least one ball. 
# The arguments passed into the hat object upon creation should be converted to a contents instance variable. 
# contents should be a list of strings containing one item for each ball in the hat. Each item in the list should be a color name representing a single ball of that color.
# For example, if your hat is {"red": 2, "blue": 1}, contents should be ["red", "red", "blue"].


class Hat:
    def __init__(self, **balls):
        self.contents = [key for key, value in balls.items() for i in range(value)]

    


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
