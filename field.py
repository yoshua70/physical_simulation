from point import Point

class InteractiveField:
  def __init__(self, F):
    self.points = []
    self.F = F

  def append(self, *args, **kwargs):
    self.points.append(Point(*args, **kwargs))

  def intensity(self, coord):
    proj = Vector(*[0 for i in range(coord.dim())])
    single_point = Point(Vector(), mass=1.0, q=1.0)
    for p in self.points:
      if coord % p.coords < 10 ** (-10):
        continue
      d = p.coords % coord
      fmod = self.F(single_point, p, d) * (-1)
      proj = proj + (coord - p.coords) / d * fmod
    return proj

  def step(self, dt):
    self.clean_acc()
    for p in self.points:
      p.accinc(self.intensity(p.coords) * p.q)
      p.accelerate(dt)
      p.move