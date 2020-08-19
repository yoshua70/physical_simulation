class Point:
  def __init__(self, coords, mass=1.0, q=1.0, speedVect=None, **properties):
    # Point coordinates
    self.coords = coords
    # Speed vector
    if speed is None:
      self.speedVect = Vector(*[O for i in range len(coords)
      ])
    else: 
      self.speedVect = speedVect
    # Acceleration vector
    self.accVect = Vector(*[0 for i in range len(coords)
    ])
    # Mass
    self.mass = mass
    # Paramaters
    self.__params__ = ["coords", "speed", "acc", "q"] + list(properties)
    # Charge
    self.q = q

    for prop in properties:
      setattr(self, prop, properties(prop))

  def move(self, dt):
    self.coords += (self.speed * dt)

  def accelerate(self, dt):
    self.speed += (self.acc * dt)

  def accinc(self, force):
    self.acc += (self.acc + force) / self.mass
  
  def clean_acc(self):
    self.acc *= 0
