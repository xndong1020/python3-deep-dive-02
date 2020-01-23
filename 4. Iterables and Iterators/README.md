# 4. Iterables and Iterators

### 1. Creating a custom collection of items type with '\_\_next\_\_' method

```py
class Squares:
  def __init__(self):
    self.i = 0

  def __next__(self):
    result = self.i ** 2 # square
    self.i += 1
    return result


square = Squares()

print(next(square)) # 0
print(next(square)) # 1
print(next(square)) # 4
print(next(square)) # 9
print(next(square)) # 16

# same as
for _ in range(5):
  print(next(square))
```

We can keep going. However a few things are missing:

1. Now the next() is infinite, how can we make it stop when it reaches its end?
2. We cannot loop through 'square' object
3. How we can reset back to 0, without creating another 'square' object?

```py
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


square = Squares(3)

while True:
  try:
    for _ in range(5):
     print(next(square))
  except StopIteration:
     print(f"Iteration stopped at {square.i}")
     break

"""
output:
0
1
4
Iteration stopped at 3
"""
```

### 2. Use iterator to fix the remaining problems

**The iterator protocol** is a contract that contains 2 methods

1. \_\_iter\_\_ This method should just return the object (class instance) itself.

```py
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
    return self


square = Squares(3)

for i in square:
  print(i)

# sort
square_reverse = sorted(square, reverse=True)
```

2. \_\_next\_\_ This method is responsible for handing back the next element from the collection and rasing the StopIteration exception when all elements have been handed out

### 3. How to reset an exhausted collection of items

when you use built-in for loop to loop through a collection of items, the \_\_iter\_\_ will be called once, then followed by nth of \_\_next\_\_ until it is exhausted. Behind the scenes, python will firstly call the \_\_iter\_\_() method of a collection of items, then call the \_\_next\_\_() method of the instance

So we can check the pointer position, if current position of the point is at the end of the collection of items, then we can reset it

```py
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
  print(item) # 0, 1, 4
```

### 4. separate iterable and iterator

An iterable is a Python object that implements the iterable protocol, it requires 1 method: \_\_iter\_\_(), which **returns an iterator**

An iterator is an object that implements \_\_iter\_\_(), which returns itself (an iterator), and \_\_next\_\_(), which returns the next element

An iterable will never be exhausted, because they always return a new iterator that is used to iterate

An iterator is also a iterable, but it will be exhausted after iteration.

```py
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
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.cities):
            raise StopIteration
        else:
            city = cities[self._index]
            self._index += 1
            return city

# a iterable will never be exhausted, because it always returns a new iterator that is used to iterate
cities = ["Sydney", "Canberra", "Perth"]
for c in cities:
    print(c)
for c in cities:
    print(c)

# output:
Sydney
Canberra
Perth
Sydney
Canberra
Perth

# once iterator is exhausted, it doesn't return anything
cities_iterator = iter(cities)
for c in cities_iterator:
    print(c)
for c in cities_iterator:
    print(c)

# output:
Sydney
Canberra
Perth
```

for sequence type like list, you can use **getitem**() method rather than **iter()** and iterator

```py
class Cities:
    def __init__(self, cities):
        self.cities = cities

    def __len__(self):
        return len(self.cities)

    def __getitem(self, i):
        return self.cities[i]


# a iterable will not be exhausted, because it always returns a iterator
cities = ["Sydney", "Canberra", "Perth"]
for c in cities:
    print(c)
for c in cities:
    print(c)

# output:
Sydney
Canberra
Perth
Sydney
Canberra
Perth
```

Python will use \_\_iter**() first, if \_\_iter**() is not found, then will try to use \_\_getitem**() method. if \_\_getitem**() method is not found as well, then raise an error
