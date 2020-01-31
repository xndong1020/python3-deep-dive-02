# Section 4. Iterables and Iterators

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

### 4. separate iterable and iterator into different classes

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

for sequence type like list, you can use \_\_getitem\_\_() method rather than \_\_iter()\_\_ and iterator

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

Python will use \_\_iter\_\_() first, if \_\_iter\_\_() is not found, then will try to use \_\_getitem\_\_() method. if \_\_getitem\_\_() method is not found as well, then raise an error

### 5a. namedTuple basics

from collections import namedtuple

"""
downside of plain tuple is that

1. the data you store in them can only be pulled out by accessing it through integer indexes.
   You can’t give names to individual properties stored in a tuple. This can impact code readability

2. It’s hard to ensure that two tuples have the same number of fields and the same properties stored on them.
   This makes it easy to introduce “slip-of-the-mind” bugs by mixing up the field order.
   """

```py
tup = ("hello", object(), 42)
print(tup[2])  # what does index '2' mean?
```

Namedtuples aim to solve these two problems.

Each object stored in them can be accessed through a unique (human-readable) identifier.
This frees you from having to remember integer indexes.

```py
# Declaring namedtuple,  we defined a simple Student data type with 3 fields: "name", "age", "DOB".
Student = namedtuple("Student", ["name", "age", "DOB"])

# create "Student" object with values
S = Student("Jeremy", "19", "2541997")

# Access using index
print("The Student age using index is : ", end="")
print(S[0])

# Access using field
print("The Student age using filed is : ", end="")
print(S.name)
```

### 5a. Example of when to consume iterator manually

For example you have a csv file in below format, line 1 is columns, line 2 is data types, and rests are actual data:

```
Car;MPG;Cylinders;Displacement;Horsepower;Weight;Acceleration;Model;Origin
STRING;DOUBLE;INT;DOUBLE;DOUBLE;DOUBLE;DOUBLE;INT;CAT
Chevrolet Chevelle Malibu;18.0;8;307.0;130.0;3504.;12.0;70;US
Buick Skylark 320;15.0;8;350.0;165.0;3693.;11.5;70;US
Plymouth Satellite;18.0;8;318.0;150.0;3436.;11.0;70;US
AMC Rebel SST;16.0;8;304.0;150.0;3433.;12.0;70;US
...
```

and the very basic way of loop through it is:

```py

# simplest way to read file line by line
import os
from collections import namedtuple

# simplest way to read file line by line
cars_data = []
with open(f"{os.path.dirname(__file__)}/cars.csv") as file:
    row_index = 0
    for line in file:
        # for first line, which is the 'columns' header
        if row_index == 0:
            columns = line.strip("\n").split(";")
            Car = namedtuple("Car", columns) #  Declaring namedtuple
        # for second line, which is the 'data types' header
        elif row_index == 1:
            data_types = line.strip("\n").split(";")
        else:
            # initializing a "Car" namedtuple object, then add to "cars_data" list
            cars_data.append(Car(*line.strip("\n").split(";")))

        row_index += 1
```

Also add utils functions to type cast the data

```py
import os
from collections import namedtuple

# simplest way to read file line by line
def cast_data_type(data_type, value):
    if data_type == "DOUBLE":
        return float(value)
    elif data_type == "INT":
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    # return [cast_data_type(data_types[idx], data) for idx, data in enumerate(data_row)]
    # or another way of doing the same thing
    return [
        cast_data_type(data_type, data) for data_type, data in zip(data_types, data_row)
    ]


cars_data = []
with open(f"{os.path.dirname(__file__)}/cars.csv") as file:
    row_index = 0
    for line in file:
        # for first line, which is the 'columns' header
        if row_index == 0:
            columns = line.strip("\n").split(";")
            Car = namedtuple("Car", columns)  #  Declaring namedtuple
        # for second line, which is the 'data types' header
        elif row_index == 1:
            data_types = line.strip("\n").split(";")
        else:
            # initializing a "Car" namedtuple object, unpack data, then add to "cars_data" list
            cars_data.append(Car(*cast_row(data_types, line.strip("\n").split(";"))))

        row_index += 1
```

We can refactor our code by using manually consume iterator

```py
import os
from collections import namedtuple

# simplest way to read file line by line
def cast_data_type(data_type, value):
    if data_type == "DOUBLE":
        return float(value)
    elif data_type == "INT":
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    # return [cast_data_type(data_types[idx], data) for idx, data in enumerate(data_row)]
    # or another way of doing the same thing
    return [
        cast_data_type(data_type, data) for data_type, data in zip(data_types, data_row)
    ]


cars_data = []
with open(f"{os.path.dirname(__file__)}/cars.csv") as file:
    # retrieve the iterator from file iterable
    file_iterator = iter(file)
    # manually read first line from iterator
    columns = next(file_iterator).strip("\n").split(";")
    # manually read second line from iterator
    data_types = next(file_iterator).strip("\n").split(";")
    Car = namedtuple("Car", columns)  #  Declaring namedtuple

    # start to read the remaining lines
    cars_data = [
        Car(*cast_row(data_types, line.strip("\n").split(";")))
        for line in file_iterator
    ]
```

### 5b. Cyclic iterator example

Let's say you want to combine 2 lists into something like below:
"""
1 2 3 4 5 6 7 8 9 ...

N S W E

1N 2S 3W 4E 5N 6S 7W 8E 9N 10S ...
"""

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        """
        0 % 4 = 0， combined = self._iterable[0] -> N
        1 % 4 = 1， combined = self._iterable[1] -> S
        2 % 4 = 2， combined = self._iterable[2] -> W
        3 % 4 = 3， combined = self._iterable[3] -> E
        4 % 4 = 0， combined = self._iterable[0] -> N
        5 % 4 = 1， combined = self._iterable[1] -> S
        """
        current = self._iterable[self._index % len(self._iterable)]
        self._index += 1
        return current

cyclic_iter = CyclicIterator("NSWE")
"""cyclic_iter is infinite iterator, which returns something like
N
S
W
E
N
S
W
E
N
S
"""

combined = zip(range(1, 11), cyclic_iter)
""" zip returns list of tuple
(1, 'W')
(2, 'E')
(3, 'N')
(4, 'S')
(5, 'W')
(6, 'E')
(7, 'N')
(8, 'S')
(9, 'W')
(10, 'E')
"""

for num, direction in list(combined):
  print(f"{num}{direction}")

"""
1W
2E
3N
4S
5W
6E
7N
8S
9W
10E
"""
```

a bit simpler version is:

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self._iterable[self._index % len(self._iterable)]
        self._index += 1
        return current


cyclic_iter = CyclicIterator("NSWE")
[print(f"{num}{direction}") for num, direction in zip(range(1, 11), cyclic_iter)]
```

Or it can be more simpler:

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        current = self._iterable[self._index % len(self._iterable)]
        self._index += 1
        return current


cyclic_iter = CyclicIterator("NSWE")

items = [f"{i}{next(cyclic_iter)}" for i in range(1, 11)]
# ['1N', '2S', '3W', '4E', '5N', '6S', '7W', '8E', '9N', '10S']
```

However, above code only works for sequence type, because we need to use the self.\_index to track the current index

for other iterable, you may think the code can be something like below:

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        # delegate the iterator logic to the __iter__ of self._iterable
        delegated_iterator = iter(self._iterable)
        current = next(delegated_iterator)
        return current


cyclic_iter = CyclicIterator({"N", "S", "W", "E"})

for _ in range(10):
    print(next(cyclic_iter))


E
E
E
E
E
E
E
E
E
E
```

it does NOT work as expected, because when \_\_next\_\_() of CyclicIterator is called, it re-creates the delegated iterator

if we move the iterator to other place, still not work as expected. because the iterator is exhausted after first consumption

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._iterator = iter(self._iterable)

    def __iter__(self):
        return self

    def __next__(self):
        current = next(self._iterator)
        return current


cyclic_iter = CyclicIterator({"N", "S", "W", "E"})

for _ in range(10):
    print(next(cyclic_iter))

S
E
N
W
Traceback (most recent call last):
  File "4. Iterables and Iterators/4.cyclic_iterator.py", line 124, in <module>
    print(next(cyclic_iter))
  File "4. Iterables and Iterators/4.cyclic_iterator.py", line 117, in __next__
    current = next(self._iterator)
StopIteration
```

To fix this problem, we need to manually reset the self.\_iterator

```py
class CyclicIterator:
    def __init__(self, iterable):
        self._iterable = iterable
        self._iterator = iter(self._iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = next(self._iterator)
        except StopIteration:
            # re-create iterator if it is exhausted
            self._iterator = iter(self._iterable)
            # if don't have this line, current will be None
            current = next(self._iterator)
        finally:
            return current


cyclic_iter = CyclicIterator({"N", "S", "W", "E"})

for _ in range(10):
    print(next(cyclic_iter))
```

### 6. Lazy iterator

1. Lazy Evaluation
   This is ofter used in class property. Properties of classes may not always be populated when the object is created. Value of property only becomes available when the property is requested - deferred

An example of not using lazy evaluation

```py
import math


class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        print("calculating area ...", r)
        self._radius = r
        # no lazy evaluation, whenever r is changed, self.area is re-calculated
        self.area = math.pi * (r ** 2)


circle = Circle(10)
print(circle.radius)  # 10
print(circle.area)  #  314.1592653589793
```

if we change radius a lot, but we don't need area, this will cause waste

we can move area into a separate property, so it will not re-calculate when radius change. But still every time when you access area property, even when the radius is not change, it will re-calculate. If the calculation is expensive, then still a waste.

```py
class Circle:
    def __init__(self, r):
        self.radius = r

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r

    @property
    def area(self):
        print("calculating area ...")
        # still no lazy evaluation, but not re-calculate when radius change
        return math.pi * (self.radius ** 2)


circle = Circle(10)
print(circle.radius)
print(circle.area)
print(circle.area)
print(circle.area)
```

To fix the problem, we need a flag to return a cached area property, or re-calculate it

```py
class Circle:
    def __init__(self, r):
        self._radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if self._radius != r:
            self._radius = r
            # when radius changed, reset the area property to None.
            self._area = None

    @property
    def area(self):
        if self._area is None:
            print("calculating area ...")
            # lazy evaluation, only re-calculate when self._area is none
            self._area = math.pi * (self.radius ** 2)
            return self._area

        # returns cached value
        return self._area


circle = Circle(10)
circle = Circle(10)
print(circle.radius)
print(circle.area)
print(circle.area)
print(circle.area)
circle.radius = 11
print(circle.area)

10
calculating area ...
314.1592653589793
314.1592653589793
314.1592653589793
calculating area ...
380.132711084365
```

An example of lazy iterable is:

```py
"""

Factorials (阶乘). for example,  6! is 1×2×3×4×5×6 = 720
"""


class Factorials:
    def __iter__(self):
        return self.FactorialsIterator()

    class FactorialsIterator:
        def __init__(self):
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.current)
            self.current += 1
            return result


factorials = Factorials()
factorials_iter = iter(factorials)
facts = [next(factorials_iter) for _ in range(7)]

print(facts)  # [1, 1, 2, 6, 24, 120, 720]
```

The Factorials class is lazy, it delegates the iteration logic to an iterator, which is FactorialsIterator inner class, to do the heavy lifting for it. and FactorialsIterator class is not evaluated, unless instance of Factorials class is being iterated.

### 7. Python built-in functions that return iterables and iterators

From previous lectures, iterables implements \_\_iter\_\_(), whereas iterators implements both \_\_iter\_\_() and \_\_next\_\_()
Below functions return iterables:

```py
range() - lazy,

# for dict
d = { 'a': 1, 'b': 2 }
keys = d.keys() # returns iterables
values = d.values() # returns iterables
items = d.items() # returns iterables
```

some returns iterators:

```py
zip()  - lazy,  enumerate() - lazy
open()

# below code will load everything into memory, then find the matching
origins = set()
with open('cars.csv') as f:
  rows = f.readlines() # read everything into memory

for row in rows[2:]:
  origin = row.strip('\n').split(';')[-1]
  origins.add(origin)

# below code will load line by line
origins = set()
with open('cars.csv') as f:
  next(f) # manually skip 1 line
  next(f) # manually skip 1 line
  for row in f:  # read line by line
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)
```

### 8. `iter()` function

When you iterate over an iterable, the first thing Python will do, is always call the iter() function on the object that we want to iterate

When `iter(obj)` is called, Python fist looks for an `__iter__` method, which will return an iterator.

On the other hand, iter() function doesn't always call the \_\_iter\_\_ method. if the object that only implements \_\_getitem\_\_ method, then the \_\_getitem\_\_ method is called

- if `__getitem__` is found, create an iterator object and return it
- if not found, raise a TypeError exception (not iterable)

```py
"""
For sequence type, __iter__ method may not be implemented.
In stead, __getitem__ method is used to create iterator
"""

class Squares:
    def __init__(self, length):
        self._length = length

    def __len__(self):
        return self._length

    def __getitem__(self, idx):
        if idx >= self._length:
            raise IndexError

        return idx ** 2


square = Squares(5)
square_iter = iter(square)

print(square_iter)  # <iterator object at 0x000002DDFED00DC0>
print(list(square_iter))  # [0, 1, 4, 9, 16]

next(square_iter)  # StopIteration
```

When `__getitem__` method is called, Python created an iterator object for us, same as `__iter__`

we can write an Iterator class to iterate any sequence type:

```py
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._sequence):
            raise StopIteration
        else:
            elem = self._sequence[self._idx]
            self._idx += 1
            return elem


square = [1, 2, 3, 4, 5]
square_iter = iter(SequenceIterator(square))

print(square_iter)  # <__main__.SequenceIterator object at 0x000001D3D11809A0>

print(list(square_iter))  # [1, 2, 3, 4, 5]
```

### 8a. Check if an object is iterable:

Need to check if the class has implemented either **getitem** or **iter** contract. For example `print('__iter__' in dir(SimpleIterable))`.

If a class has implemented **iter**, but don't return an iterator, you will get `TypeError: 'type' object is not iterable`

```py
class SimpleIterable:
    def __iter__(self):
        return 'Nope'

print('__iter__' in dir(SimpleIterable)) # True

for i in SimpleIterable: # TypeError: 'type' object is not iterable
    print(i)

# use try-catch to avoid error when necessary
try:
    for i in SimpleIterable: # TypeError: 'type' object is not iterable
        print(i)
except TypeError:
    print('not iterable')
```

### 9. Creating an iterator using callable

This is the second way of creating an iterator, that is using the second form of iter function, which requires a callable, and a stop value (sentinel value)

Source code of `__iter__` method:

```py
@overload
def iter(__iterable: Iterable[_T]) -> Iterator[_T]: ...
@overload
def iter(__function: Callable[[], _T], __sentinel: _T) -> Iterator[_T]: ...
```

we can create an iterator by use this way:

```py
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self._counter_callable = counter_callable
        self._sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        result = self._counter_callable()
        if result == self._sentinel:
            raise StopIteration
        else:
            return result


counter = counter()  # returns inc() function, with 'i' as its closure
print(counter)  # <function counter.<locals>.inc at 0x0000023109FEDB80>
counter_iter = CounterIterator(counter, 5)
print(counter_iter)  # <__main__.CounterIterator object at 0x0000026EBD5C8DF0>

[print(i) for i in counter_iter]

"""
1
2
3
4
"""
```

But be `careful` if you use callable to create an iterator. See below example:

- counter_iter will not consumed, just skip sentinel value
- if you call counter() before creating `counter_iter`, the closure of counter() is changed

```py
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self._counter_callable = counter_callable
        self._sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        result = self._counter_callable()
        if result == self._sentinel:
            raise StopIteration
        else:
            return result


counter = counter()  # returns inc() function, with 'i' as its closure
print(counter)  # <function counter.<locals>.inc at 0x0000023109FEDB80>

counter()  # closure i changed to 1
counter()  # closure i changed to 2

# # now the counter function closure is 3
counter_iter = CounterIterator(counter, 5)
print(counter_iter)  # <__main__.CounterIterator object at 0x0000026EBD5C8DF0>

for i in counter_iter:
    print(i)

print(next(counter_iter))  # 6

"""
3
4
6
"""

```

To fix problem 1: counter_iter will not consumed, just skip sentinel value

```py
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self._counter_callable = counter_callable
        self._sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration

        result = self._counter_callable()
        if result == self._sentinel:
            self.is_consumed = True
            raise StopIteration
        else:
            return result


counter = counter()  # returns inc() function, with 'i' as its closure
# # now the counter function closure is 3
counter_iter = CounterIterator(counter, 5)

for i in counter_iter:
    print(i)

print(next(counter_iter))  # StopIteration

"""
1
2
3
4

StopIteration
"""
```

We can use the built-in `iter()` method overloaded version 2, to achieve the same result:
**Note**:

- When we use the first way of creating iterable, the return object type of iter(iterable) will be `iterator`
- When we use the second way of creating iterable, the return object type of iter(callable, sentinel) will be `callable_iterator`

```py
def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


counter = counter()  # returns inc() function, with 'i' as its closure

# now the counter function closure is 4
counter_iter = iter(counter, 5)
print(counter_iter)  # <callable_iterator object at 0x0000029AB3B28DF0>

[print(i) for i in counter_iter]
"""
1
2
3
4
"""
print(next(counter_iter))  # StopIteration
```

Below are 2 examples:

1. Generate a random number, which value cannot be equal to 8:

```py
import random

random_iter = iter(lambda: random.randint(0, 10), 8)  # random number cannot equal to 8

for num in random_iter:
    print(num)

```

2. a countdown from 5 until reach 0

```py
def countdown():
    start = 6

    def dec():
        nonlocal start
        start -= 1
        return start

    return dec


countdown_iter = iter(countdown(), 0)

for i in countdown_iter:
    print(i)

"""
5
4
3
2
1
"""
```

### 9b. Delegating iterators (without writing our own iterator)

The built-in iter(iterable) method will return an iterator, we can delegate the iteration logic to that iterator

```py
from collections import namedtuple

# create an template for 'Person' namedtuple, with 2 attributes, "first", "last"
Person = namedtuple("Person", ["first", "last"])


class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [
                f"{person.first.capitalize()} {person.last.capitalize()}"
                for person in persons
            ]
        except (
            TypeError,
            AttributeError,
        ):  # TypeError when persons is not iterable, AttributeError when person doesn't have proper attributes
            print("Error")

    def __iter__(self):
        # the built-in iter(iterable) method will return an iterator, we can delegate the iteration logic to that iterator
        return iter(self._persons)


persons = [Person("niCoLE", "dong"), Person("jeREMY", "gU"), Person("hArPER", "gU")]

person_iter = iter(PersonNames(persons))

[print(person) for person in person_iter]


"""
Nicole Dong
Jeremy Gu
Harper Gu
"""

```
