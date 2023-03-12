import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
          for i in range(value):
            self.contents.append(key)

    def draw(self, n):
        drawn = []
        if n > len(self.contents):
            return self.contents
        for i in range(n):
            choice = random.randrange(len(self.contents))
            drawn.append(self.contents.pop(choice))
        return drawn 
            
            
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    expected_num_balls = []
    for key in expected_balls:
        expected_num_balls.append(expected_balls[key])

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        num_balls = []
        for key in expected_balls:
            num_balls.append(balls_drawn.count(key))

        if num_balls >= expected_num_balls:
            successes +=1  

    return successes / num_experiments