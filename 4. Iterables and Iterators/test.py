# class Squares:
#   def __init__(self, size):
#     self.size = size
#     self.i = 0

#   def __len__(self):
#     return self.size

#   def __next__(self):
#     if self.i >= self.size:
#       raise StopIteration
#     else:
#       result = self.i ** 2 # square
#       self.i += 1
#       return result

#   def __iter__(self):
#     return self


# square = Squares(3)

# for item in square:
#   print(item) #  0, 1, 4

# for item in square:
#   print(item) # nothing, because 'square' instance is exhausted

class Squares:
  def __init__(self, size):
    self.size = size
    self.i = 0

  def __len__(self):
    return self.size

  def __next__(self):
    if self.i >= self.size:
      raise StopIteration
    else:
      result = self.i ** 2 # square
      self.i += 1
      return result

  def __iter__(self):
    # reset pointer
    if self.i == self.size:
      self.i = 0

    return self


square = Squares(3)

for item in square:
  print(item) #  0, 1, 4

for item in square:
  print(item) # nothing, because 'square' instance is exhausted