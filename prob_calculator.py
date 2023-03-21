import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **color_balls):
    self.contents = list()
    for color, number in color_balls.items():
      for value in range(number):
        self.contents.append(color)

  def draw(self, number):
    drawn = []
    if number > len(self.contents):
      drawn = self.contents.copy()
      self.contents = self.contents.clear()
      return drawn

    for balls in range(number):
      choosen = random.choice(self.contents)
      drawn.append(choosen)
      self.contents.remove(choosen)
    return drawn 
      
      

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  
  expected = []
  for color, number in expected_balls.items():
    for value in range(number):
      expected.append(color)

  for i in range(num_experiments):
    newHat = copy.deepcopy(hat)
    drawn = newHat.draw(num_balls_drawn)

    count = 0
    for j in range(len(expected)):
      if expected[j-1] in drawn:
        count += 1
        drawn.remove(expected[j-1])
        if count == len(expected):
          m += 1
          
  probability = m / num_experiments
  print(probability, "=", m, "/", num_experiments)
  return probability
