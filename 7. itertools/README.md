### 1. Falsy value in Python

1. None
2. False
3. 0 in any numeric type, like Integer, Float, Complex (eg. 0, 0.0, 0+0j, ...)
4. empty sequence types (eg. list,tuple, string, ...)
5. empty mapping types (eg. dictionary, set, ...)
6. custom class that implements \_\_bool\_\_ or \_\_len\_\_, and returns False or 0

```py
empty_list = []
print(bool(empty_list))  # False

empty_tuple = ()
print(bool(empty_tuple))  # False

empty_str = ""
print(bool(empty_tuple))  # False


# Empty ranges range(0)
empty_range = range(0)
print(bool(empty_range))  # False

empty_dict = {}
print(bool(empty_str))  # False

class Account:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        print("__bool__ called")
        return self.balance > 0


account1 = Account(500)
print(bool(account1))  # True
account2 = Account(0)
print(bool(account2))  # False


class Inventory:
    def __init__(self, inventories):
        self.inventories = inventories

    def __len__(self):
        return len(self.inventories)


stocks1 = Inventory(["banana", "apple"])
print(bool(stocks1))  # True

stocks2 = Inventory([])
print(bool(stocks2))  # False
```


### 2. Aggregators

Functions that iterate through an iterable, and return a single value that usually takes into account every element of the iterable

#### Math
1. min(iterable)
2. max(iterable)
3. sum(iterable)

#### Array
To check if any, or all elements in the array satisfy a certain condition
4. any(iterable)
5. all(iterable)

```py
numbers = [1, 10, 20, 100]
pred = lambda x: x < 100

result = any([pred(num) for num in numbers])
print(result) # True


result = all((pred(num) for num in numbers))
print(result) # False
```

6. map(fn, iterable)
equals to: comprehension (fn(item) for item in iterable)

```py
numbers = [1, 10, 20, 100]

doubled = map(lambda x: x * 2, numbers)
print(doubled)  # [2, 20, 40, 200]
```

#### 3. slicing
[start:stop:step] and slice(start, stop, step) and be used on sequence types

```py
# for sequence types we use index
numbers = [1, 2, 3, 4, 5]

bits1 = numbers[0:3]
print(bits1)  # [1, 2, 3]

bits2 = numbers[0:3:2]  # with step of 2
print(bits2)  # [1, 3]

# for sequence types we use slice
slice1 = slice(0, 3)
print(type(slice1)) # <type 'slice'>

bits3 = numbers[slice1]
print(bits3)  # [1, 2, 3]

slice2 = slice(0, 3, 2)
bits4 = numbers[slice2]
print(bits4)  # [1, 3]

```

but for non sequence type iterables, you cannot use [start:stop] or slice
```py
def factorial_finite(n):
    for i in range(n):
        yield factorial(i)


# generator object
facts = factorial_finite(10)
print(facts[0:3]) 
# TypeError: 'generator' object has no attribute '__getitem__'
```
This error means facts as a generator object, is not **subscriptable**, or it is not **indexable**.

To solve this problem, we can either to use our own islice_() function
```py
def factorials_infinite():
    index = 0
    while True:
        yield factorial(index)
        index += 1

# our own islice_ function:
def islice_(iterable, start, stop):
    # skip any item from 0 to start position
    for _ in range(0, start):
        next(iterable)
    
    for _ in range(start, stop):
        yield next(iterable)



bits5 = islice_(factorials_infinite(), 3, 10)
print(list(bits5)) # [6, 24, 120, 720, 5040, 40320, 362880]
```

Or, we can use itertools.islice() function
```py
def factorials_infinite():
    index = 0
    while True:
        yield factorial(index)
        index += 1

from itertools import islice
bits6 = islice(factorials_infinite(), 0, 10)
print(bits6)  # <itertools.islice object at 0x102954470>

print(list(bits6))
```
From above code, islice() returns a **lazy iterator**.


#### 3. Filtering
##### filter()
`filter(predicate, iterable)` returns all the elements in the iterable where predicate(item) is True

filter() function returns a **lazy iterator**

filter() function can be achieved by using generator expression
`(item for item in iterable if predicate(item))`

```py
numbers = [1, 50, 2, 88, 3, 100]

small = filter(lambda x: x < 4, numbers)

print(small) # [1, 2, 3]
```

##### itertools.filterfalse()
`itertools.filterfalse(predicate, iterable)` returns all the elements in the iterable where predicate(item) is False

```py
from itertools import filterfalse

big = filterfalse(lambda x: x < 4, numbers)
print(big)  # <itertools.filterfalse object at 0x1087b1590>
print(list(big))  # [50, 88, 100]
```

##### itertools.compress()
`itertools.compress(data, selectors)` is a way of filtering one iterable(data), by using the truthness of items in another iterable(selectors) 

```py
items = ['apple', 'ginger', 'banana', 'orange', 'mongo']
selectors = [True, False, 1, 0]

selected = compress(items, selectors)
print(selected)  # <itertools.compress object at 0x1100cfc50>
print(list(selected)) # ['apple', 'banana']
```
In above example, 'items' have 5 elements, and 'selectors' have 4 elements, so the fifth selector will be None, which has falsy value

| Apple         | Ginger        | Banana     | Orange    | Mongo        |
| ------------- | ------------- | ---------- | --------- | ------------ |
| True (Truthy) | False (Falsy) | 1 (Truthy) | 0 (Falsy) | None (Falsy) |

So 'Apple' and 'Banana' are kept.

##### takewhile(), dropwhile()
`takewhile(predicate, iterable)` yield items in iterable, until predicate(item) returns falsy

`dropwhile(predicate, iterable)` drop items in iterable, until predicate(item) returns falsy, then returns remaining items

```py
numbers = [1, 50, 2, 88, 3, 100]

takes1 = takewhile(lambda x: x< 60, numbers)
print(takes1)  # <itertools.takewhile object at 0x10732d0a0>
print(list(takes1)) # [1, 50, 2]

takes2 = dropwhile(lambda x: x< 60, numbers)
print(takes2)  # <itertools.dropwhile object at 0x10d072140>
print(list(takes2)) # [88, 3, 100]
```


