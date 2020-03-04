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


#### 6. Mapping and Reducing
##### Mapping and Accumulation

Mapping  ---->  applying a callback to each element of an iterable
`map(fn, iterable)`


Accumulation -----> reducing an iterable to a single value
`sum(iterable)` calculate the sum of every element in an iterable
`min(iterable)` returns the minimal element of the iterable
`max(iterable)` returns the maximal element of the iterable

`reduce(fn, iterable, [initializer])`  is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

```py
l = [1, 2, 3, 4]
# x is accumulator, y is current element
reduce(lambda x, y: x + y, l)

step 1: 
current is 1, accumulator is 0 ----> accumulator = 1 + 0 = 1
step 2: 
current is 2, accumulator is 1 ----> accumulator = 1 + 2 = 3
step 3: 
current is 3, accumulator is 3 ----> accumulator = 3 + 3 = 6
step 4: 
current is 4, accumulator is 6 ----> accumulator = 4 + 6 = 10



# if reduce has a initial value
# x is accumulator, y is current element
reduce(lambda x, y: x + y, l, 100)

step 1: 
current is 1, accumulator is 100 ----> accumulator = 1 + 100 = 101
step 2: 
current is 2, accumulator is 101 ----> accumulator = 2 + 101 = 103
step 3: 
current is 3, accumulator is 103 ----> accumulator = 3 + 103 = 106
step 4: 
current is 4, accumulator is 106 ----> accumulator = 4 + 106 = 110

```

##### complex reduce example
```py
from functools import reduce

users = [
    {"name": "Jeremy", "department": "IT"},
    {"name": "Nicole", "department": "IT"},
    {"name": "Allen", "department": "Accounting"},
    {"name": "Sarah", "department": "Accounting"},
    {"name": "Josh", "department": "Finance"},
]


def group_user(accumulator, user):
    if user["department"] in accumulator:
        accumulator[user["department"]]["users"].append(user["name"])
    else:
        accumulator[user["department"]] = {}
        accumulator[user["department"]].update({"users": [user["name"]]})
    return accumulator


results = reduce(group_user, users, {})
print("results", results)

# {'IT': {'users': ['Jeremy', 'Nicole']}, 'Accounting': {'users': ['Allen', 'Sarah']}, 'Finance': {'users': ['Josh']}}
```

##### itertools.starmap
`starmap(fn, iterable)` is very similar to `map(fn, iterable)`
1. it unpacks every sub element of the iterable argument, and passes that to the map function
2. useful for mapping a multiple-argument function on an iterable of iterables

```py
# using map
l = [[1, 2], [3, 4]]
result = map(lambda item: item[0] * item[1], l)
print(list(result))  # [2, 12]

# using starmap
from itertools import starmap
from operator import mul  # mul expected 2 arguments

l = [[1, 2], [3, 4]]
result1 = starmap(mul, l)
print(list(result1))  # [2, 12]

# using generator expression
result2 = (mul(*item) for item in l)
print(list(result2))  # [2, 12]
```

of course starmap can deal sub-element that has more than 2 elements
```py
# more than 2 arguments
l = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
result3 = starmap(lambda x, y, z: x + y + z, l)
print(list(result3))  # [6, 60, 600]
```

##### itertools.accumulate(iterable, fn)  -> lazy iterator
The `accumulate(iterable, fn)` is very similar to the `reduce(fn, iterable, [initialValue])` function

But the differences are:
1. accumulate returns a lazy iterator producing all the intermediate results. Reduce only returns the final results
2. accumulate does not accept initial value
3. note that the argument order is NOT the same!

```py
# using accumulate function
from itertools import accumulate
from operator import add

l = [1, 2, 3, 4, 5, 6]
results4 = accumulate(l, add)  

print(results4)  # <itertools.accumulate object at 0x1057121e0>
for num in results4:
    print(num)  # 1 3 6 10 15 21, all the intermediate results
```


#### 7. zipping
the `zip` function returns a lazy iterator
It takes a variable number of positional arguments - each of which are iterables

It returns an iterator that produces tuples containing the elements of the iterables, iterable on at a time

It stops immediately once one the iterables has been exhausted, zip based on the shortest iterable

```py
result1 = zip([1, 2, 3], [10, 20], ['a', 'b', 'c', 'd'])
print(result1)  # <zip object at 0x10a727fa0>
print(list(result1))  # [(1, 10, 'a'), (2, 20, 'b')]
# based on shortest iterable, which is [10, 20]
```

###### itertools.zip_longest
Sometimes we want to zip, but based on the longest iterable
we can optional provide a default value for the "hole"  ---> fillvalue

```py
from itertools import zip_longest

# without fillvalue
result2 = zip_longest([1, 2, 3], [10, 20], ["a", "b", "c", "d"])
print(result2)  # <itertools.zip_longest object at 0x10d0b99b0>
print(list(result2))
# [(1, 10, 'a'), (2, 20, 'b'), (3, None, 'c'), (None, None, 'd')]

# with fillvalue
result3 = zip_longest([1, 2, 3], [10, 20], ["a", "b", "c", "d"], fillvalue=-1)
print(result3)  # <itertools.zip_longest object at 0x10d0b99b0>
print(list(result3))
# [(1, 10, 'a'), (2, 20, 'b'), (3, -1, 'c'), (-1, -1, 'd')]
```

#### 8. Grouping
Something we want to loop over an iterable of elements, but we want to `group` those elements as we iterate through them

`itertools.groupby(data, [keyfunc])` keyfunc is used to calculate the `key` we want to use for `grouping`, and it returns a lazy iterator

```py
data = [
    (1, 10, 100),
    (1, 11, 101),
    (1, 12, 102),
    (2, 20, 200),
    (2, 21, 201),
    (3, 30, 300),
    (3, 31, 301),
    (3, 32, 302),
]

from itertools import groupby

groups = groupby(data, lambda x: x[0])
print(groups)  # <itertools.groupby object at 0x10f14e9b0>

for key, grouper in groups:
    print(key)  # 1 2 3
    print(list(grouper))
    # [(1, 10, 100), (1, 11, 101), (1, 12, 102)]
    # [(2, 20, 200), (2, 21, 201)]
    # [(3, 30, 300), (3, 31, 301), (3, 32, 302)]
```

if we change the order of data, result will be very different
```py
data1 = [
    (2, 21, 201),
    (3, 30, 300),
    (3, 31, 301),
    (3, 32, 302),
    (1, 10, 100),
    (1, 11, 101),
    (1, 12, 102),
    (2, 20, 200),
]

from itertools import groupby

for key, grouper in groupby(data1, lambda x: x[0]):
    print(key)  
    print(list(grouper))
    # [(1, 10, 100), (1, 11, 101), (1, 12, 102)]
    # [(2, 20, 200), (2, 21, 201)]
    # [(3, 30, 300), (3, 31, 301), (3, 32, 302)]


"""
2
[(2, 21, 201)]
3
[(3, 30, 300), (3, 31, 301), (3, 32, 302)]
1
[(1, 10, 100), (1, 11, 101), (1, 12, 102)]
2
[(2, 20, 200)]
"""
```

so possibly we need to sort it before groupby
```py
data1 = [
    (2, 21, 201),
    (3, 30, 300),
    (3, 31, 301),
    (3, 32, 302),
    (1, 10, 100),
    (1, 11, 101),
    (1, 12, 102),
    (2, 20, 200),
]

sorted_data = sorted(data1, key=lambda x: x[0])
for key, grouper in groupby(sorted_data, lambda x: x[0]):
    print(key)  
    print(list(grouper))
    
"""
1
[(1, 10, 100), (1, 11, 101), (1, 12, 102)]
2
[(2, 21, 201), (2, 20, 200)]
3
[(3, 30, 300), (3, 31, 301), (3, 32, 302)]
"""
```