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

To solve this problem, we can either to use our own islice\_() function

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

#### 4. Infinite Iterators

##### itertools.count()

`count(start, [step=1])` returns an infinite iterator
It has some similarity to range -> both have start, step
difference with range -> no stop, infinite

start and step can be any numeric type: integer, float, complex, bool(eg 1, 0)

```py
from itertools import count

count1 = count(10)  # start from 10, step default to 1
print(count1)  # lazy, infinite iterator

###
10
11
12
13
14
15
16
17
18
19
###

for _ in range(100):
    print(next(count1))

count2 = count(1, 2)

for _ in range(10):
    print(next(count2))

###
1
3
5
7
9
11
13
15
17
19
###


count3 = count(10.6, 0.1)

for _ in range(10):
    print(next(count3))

###
10.6
10.7
10.799999999999999
10.899999999999999
10.999999999999998
11.099999999999998
11.199999999999998
11.299999999999997
11.399999999999997
11.499999999999996
###

```

##### itertools.cycle()

`cycle(finite_iterable)` function loop over a finite iterable indefinitely

Note:

1. If the argument of cycle() is an iterator, and this iterator becomes exhausted, cycle() method **will still** produce an infinite sequence.
2. cycle() will NOT repeat iterable itself for n times, instead it will repeat the elements from the iterable, for n times.

```py
from itertools import cycle

cycled = cycle(["a", "b", "c"])
print(cycled)  # <itertools.cycle object at 0x00000196D3EDF3C0>

for _ in range(5):
    print(next(cycled))

# a b c a b
```

##### itertools.repeat()

The `repeat(elem [,n])` function simply yields the same value indefinitely.
repeat(10, 3) --> 10 10 10

**Caveat**: The item yielded by `repeat()` are the **same object**, they each reference the **same object in memory**

```py
from itertools import repeat

# infinite iterator
infinite_spam = repeat("spam")  # Lazy iterator

for _ in range(10):
    print(next(infinite_spam))

# spam spam spam spam spam spam spam spam spam spam

# Optionally, you can specify a count to make the iterator finite
finite_spam = repeat("spam", 3)

print(list(finite_spam))  # ['spam', 'spam', 'spam']
```

| **Iterator** | **Arguments** | **Results**                                    | **Example**                           |
| ------------ | ------------- | ---------------------------------------------- | ------------------------------------- |
| count()      | start, [step] | start, start+step, start+2\*step, …            | count(10) --> 10 11 12 13 14 ...      |
| cycle()      | p             | p0, p1, … plast, p0, p1, …                     | cycle('ABCD') --> A B C D A B C D ... |
| repeat()     | elem [,n]     | elem, elem, elem, … endlessly or up to n times | repeat(10, 3) --> 10 10 10            |

#### 5a. Chaining

`itertools.chain(*args)` takes variable number of positional arguments, and each argument themselves should be **iterables**, and it will return a **lazy iterator**

Make an iterator that returns elements from the first iterable until it is exhausted, then proceeds to the next iterable, until all of the iterables are exhausted. Used for treating consecutive sequences as a single sequence.

This is analogous to sequence concatenation (eg. [1,2] + [3, 4] + [5], which gives us [1, 2, 3, 4, 5]), but not the same!!

1. chaining dealing with iterables(including iterators)
2. chaining is itself a lazy iterator

```py
from itertools import repeat

iter1 = [1, 2, 3]  # sequence
iter2 = repeat("spam", 3)  # lazy iterator
iter3 = (5, 6)  # tuple

# manually chain iterables
def chain_(*args):
    for itor in args:
        yield from itor


itor = chain_(iter1, iter2, iter3)

print(itor)  # <generator object chain_ at 0x0000023DA6085660>
print(list(itor))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]
```

Or, we can use itertools.chain(), or itertools.chain.from_iterable()

```py
# use chain as follows:
iter1 = [1, 2, 3]  # sequence
iter2 = repeat("spam", 3)  # lazy iterator
iter3 = (5, 6)  # tuple

...

from itertools import chain

iter2 = repeat("spam", 3)  # iter2 was exhausted in previous code
lazy_itor = chain(iter1, iter2, iter3)

iter2 = repeat("spam", 3)  # iter2 was exhausted in previous code
lazy_itor02 = chain.from_iterable([iter1, iter2, iter3])

print(list(lazy_itor))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]
print(list(lazy_itor02))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]
```

`chain.from_iterable()` takes exactly 1 argument, which is an iterable of iterables.
Why use chain.from_iterable([iter1, iter2, iter3]) ??

Caveat: if l = [iter1, iter2, iter3], then we cannot use chain() directly, as chain() method is expecting variable number of iterables.
We could do chain(\*l), and this will work. However, **unpacking is eager, not lazy!**. This could be a problem if we really wanted the entire chaining process to be lazy.

We can manually create \_from_iterable()

```py
# manually create from_iterable
iter1 = [1, 2, 3]  # sequence
iter2 = repeat("spam", 3)  # lazy iterator
iter3 = (5, 6)  # tuple

def _from_iterable(it):
    for sub_it in it:
        yield from sub_it


lazy_iter03 = _from_iterable([iter1, iter2, iter3])

print(list(lazy_iter03))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]
```

`chain.from_iterable(it)` iterates lazily over it, then in turn, iterates lazily over each iterable in it.

#### 5b. teeing

`teeing(iterable, n)` returns **independent** iterables in a tuple
eg.
tee(iterable, 10) -> (iter1, iter2, ..., iter10)

iter1, iter2, ..., iter10 are **all different objects**

The elements of the returned tuple are lazy iterators, even if the original argument (eg. [1, 2, 3]) was not a lazy iterator.

l = [1, 2, 3]
tee(l, 3) -> (iter1, iter2, iter3), all iter1, iter2, iter3 are lazy iterators, not lists!!
