import math

class Vector(list):
  def __init__(self, *args):
    for arg in args:
      self.append(arg)

  def __add__(self, other):
    """ Return the vector addition od self and other """
    if type(other) is Vector:
      assert len(self) == len(other), "Error 0"
      added = tuple(a + b for a,b in zip(self, other))
      return Vector(*added)

  def __sub__(self, other):
    """ Return the vector substraction of self and other vector """
    if type(other) is Vector:
      assert len(self) == len(other), "Error 0"
      substracted = tuple(a - b for a,b in zip(self, other))
      return Vector(*substracted)

  def inner(self, other):
    """ Return the inner product of self and other vector """
    assert len(self) == len(other), "Error 0"
    return sum(a * b for a, b in zip(self, other))

  def __mul__(self, other):
    """ Return the dot product of self and other vector if multiplied by another vector. If multiplied by an int or float, multiplies each component by other"""
    if type(other) == type(self):
      assert len(self) == len(other), "Error 0"
      return self.inner(other)
    elif type(other) == type(1) or type(other) == type(1.0):
      product = tuple(a * other for a in self)
      return Vector(*product)

  def __mod__(self):
    """ Return the norm of self vector """
    return math.sqrt(sum(a ** 2 for a in self))

