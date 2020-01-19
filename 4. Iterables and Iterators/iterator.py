class Cities:
  def __init__(self, cities):
    self.cities = cities

  def __len__(self):
    return len(self.cities)

  def __iter__(self):
    return CitiesIterator(self)

class CitiesIterator:
  def __init__(self, cities):
    self.cities = cities
    self.idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.idx >= len(self.cities):
      raise StopIteration
    else:
      city = cities[self.idx]
      self.idx += 1
      return city

cities = ['Sydney', 'Canberra', 'Perth']

for c in cities:
  print(c)