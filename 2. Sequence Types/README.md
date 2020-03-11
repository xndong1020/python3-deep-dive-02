## 2. Sequence Types

### 1. Built-In Sequence Types

-- Mutable:
---- lists, bytearrays
-- Immutable:
---- strings, tuples, range, bytes
-- Additional Standard Types:
---- collection package:
------ namedtuple, deque
---- array module:
------ array

- tuple is also a data structure

### 2. Homogeneous (same type) vs Heterogeneous

-- Homogeneous:
---- string,
-- Heterogeneous
---- list

Homogeneous is often more efficient

### 3. Iterable vs Sequence Type

As Sequence type must have positional index, so some data type like Set, it is iterable, but Set is not a sequence type (no ordering)

```py
s = { 1, 2, 3} // a set cannot use positional index like s[1]
```


### common methods for both mutable and immutable sequence types:

```py
x in s      # existence
x not in s  # existence
s1 + s2     # concatenation
s * n       # repetition

len(s)
min(s)
max(s)

# enumerate function
s = 'jeremy'

# if you want to loop through a  string, and find the index for each character

for idx, item in enumerate(s):
  print(idx, item)

result
"""
0 j
1 e
2 r
3 e
4 m
5 y
"""

s.index(x)        # index of first occurrence of x in s
s.index(x, i)     # index of first occurrence of x in s, at or after index i
s.index(x, i, j)  # index of first occurrence of x in s, at or after index i, and before index j

s[i]        # the element at index i
s[i: j]     # the slice from index i, to (but not including) j, eg. s[j] is not included in the slice
s[i: j :k] # the slice from index i, to (but not including) j, in steps of k

# reverse a string by using slicing negative steps
s1 = s[-1] # output 'y'. because if step of -1, means start from the end
s2 = s[3: 0 :-1]  # output 'ere', start from s[3], which is 'e', and end at s[0], which is 'j'. but upper bound 'j' not included
rev = s[::-1] # this means start from very end, stop at very beginning, with step of -1 (from back to start)

```

### 4. range object are more restrictive:

no concatenation/ repetition
min, max, in, not in are not as efficient

### 5. Review: beware of concatenation and repetition

```py
x = [1, 2]     a = x + x    a -> [1, 2, 1, 2]   # it is ok if containing value types
x = 'abc'      a = x + x    a -> 'abcabc'       # it is ok if containing immutable reference types

# but be care of if containing mutable reference types
x= [ [0, 0] ]    a = x + x   a -> [ [0, 0], [0, 0] ]

as x[0] and x[1] is sharing the same memory address

a[0][0] = 100  a -> [ [100, 0], [100, 0] ]  # both are changed because they are sharing the same memory address
```

#### Mutable Sequence Type
Mutating an object means changing the object's state without creating a new object

##### concatenation does NOT mutable sequence type
```py
names = ["Eric", "John"]
print(id(names))  # 4518273504

names = names + ["Mike"]
print(id(names))  #  4520652064
```


##### Mutating using []
```py
s[i] = x      # element at index i is replaced with x
s[i:j] = s2   # slice is replaced by the contents of iterable s2
del s[i]      # delete an element at index i
del s[i:j]    # delete entire slice

# we can even assign to extended slice
s[i:j:k] = s2


s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s2 = ["A", "B", "C"]

s[1:7:2] = s2
print(s)  # [1, 'A', 3, 'B', 5, 'C', 7, 8, 9]
```


##### Some methods supported by mutable sequence types such as lists
```py
s.clear()       # remove all items from s
s.append(x)     # appends single item x to the end of s
s.insert(i, x)  # insert x at index i
s.extend(iter)  # append contents from iterable iter to the end of s
s.pop(i)        # remove and returns element at index i
s.remove(x)     # removes the first occurrence of x in s. Python will find it for you. If not found, throws an error
s.reverse()     # does an in-place reversal of elements of s
s.copy()        # returns a shallow copy of s. So if copy is mutated, s is mutated as well
```




#### 3. Lists vs Tuples
Tuple is not just a immutable sequence type, it is a data structure,  and it is more efficient than list. So unless you need the mutability of the container, you really want to use tuple over list.

1. Because of constant folding, tuple compiling is much faster than list compiling
```py
from dis import dis

print(dis(compile('(1, 2, 3, 4, "a")', "string", "eval")))

"""
1           0 LOAD_CONST               0 ((1, 2, 3, 4, 'a'))
            2 RETURN_VALUE

Just 2 steps
1. load a const, which is the target tuple (1, 2, 3, 4, 'a')
2. return value
"""

print(dis(compile('[1, 2, 3, 4, "a"]', "string", "eval")))

"""
  1           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 ('a')
             10 BUILD_LIST               5
             12 RETURN_VALUE

Steps are depended on the length of the list, each element in the list will be loaded seperately, and 1 extra step to build the list, then return value
"""


print(dis(compile("(1, 2, 3, 4, [10, 20])", "string", "eval")))

"""
As long as there is a list in the tuple, the compiler has to do more steps
  1           0 LOAD_CONST               0 (1)
              2 LOAD_CONST               1 (2)
              4 LOAD_CONST               2 (3)
              6 LOAD_CONST               3 (4)
              8 LOAD_CONST               4 (10)
             10 LOAD_CONST               5 (20)
             12 BUILD_LIST               2
             14 BUILD_TUPLE              5
             16 RETURN_VALUE
"""
```

We can compare the time for Python to compile a tuple and a list
```py
from timeit import timeit

print(timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10_000_000))
# .10960877799999999

print(timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10_000_000))
# .1.230675957
```

2. And we can see Python did some optimization for tuple. For example, because tuple is immutable, so Python don't need to worry about creating a new instance for tuple
```py
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = list(l1)  # list() constructor will create a new list object

print(l1 is l2, id(l1), id(l2))  # False 4513944272 4514126816

l1[0] = 0  # if you change a element in l1, l2 is not affected
print(l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
t2 = tuple(t1)

print(t1 is t2, id(t1), id(t2))  # True 4408873936 4408873936
```

3. In terms of storage efficiency, tuple is better than list. For below code, you can see some storage over allocation from list
```py
# Storage efficiency
import sys

t = tuple()
prev = sys.getsizeof(t)

for i in range(10):
    # create a new tuple based on range(i+1), it will be (0,), (0,1,) ...
    c = tuple(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f"{i+1} items: {size_c} bytes, delta={delta}")

"""
1 items: 64 bytes, delta=8
2 items: 72 bytes, delta=8
3 items: 80 bytes, delta=8
4 items: 88 bytes, delta=8
5 items: 96 bytes, delta=8
6 items: 104 bytes, delta=8
7 items: 112 bytes, delta=8
8 items: 120 bytes, delta=8
9 items: 128 bytes, delta=8
10 items: 136 bytes, delta=8
"""

l = list()
prev = sys.getsizeof(l)

for i in range(10):
    # create a new list based on range(i+1), it will be [0,], [0,1,] ...
    c = list(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f"{i+1} items: {size_c} bytes, delta={delta}")

"""
1 items: 104 bytes, delta=32
2 items: 112 bytes, delta=8
3 items: 120 bytes, delta=8
4 items: 128 bytes, delta=8
5 items: 136 bytes, delta=8
6 items: 144 bytes, delta=8
7 items: 152 bytes, delta=8
8 items: 168 bytes, delta=16
9 items: 200 bytes, delta=32
10 items: 208 bytes, delta=8
"""
```

Instead creating new list, what if we append list?
```py
l = list()
prev = sys.getsizeof(l)

for i in range(10):
    # create a new list based on range(i+1), it will be [0,], [0,1,] ...
    l.append(i)
    size = sys.getsizeof(l)
    delta, prev = size - prev, size
    print(f"{i+1} items: {size} bytes, delta={delta}")

"""
0 items: 72 bytes
1 items: 104 bytes, delta=32
2 items: 104 bytes, delta=0
3 items: 104 bytes, delta=0
4 items: 104 bytes, delta=0
5 items: 136 bytes, delta=32
6 items: 136 bytes, delta=0
7 items: 136 bytes, delta=0
8 items: 136 bytes, delta=0
9 items: 200 bytes, delta=64
10 items: 200 bytes, delta=0
"""
```
Whenever a list is running out spaces, it will expend a few slots to pre allocate enough space for storing new elements, and the over allocation will become bigger and bigger as the size of list grow.


3. retrieving element from tuple and list using index
```py
tt = tuple(range(100_000))
ll = list(tt)

print(timeit("tt[99_999]", globals=globals(), number=10_000_000))
# 0.5591784460000002
print(timeit("ll[99_999]", globals=globals(), number=10_000_000))
# 0.5623680189999998
```
There is no big difference, however reading element from tuple is still slightly faster, because tuple is using `direct access`, while for list, it has to access an array of pointers, then retrieve element(s) from list

Conclusion:
1. If you have a immutable sequence type, which only contains immutable objects, then compiler can efficiently do all in step, and tread everything as a constant
2. If you don't need the mutability of sequence type, better of using tuples instead of lists
3. For storage efficiency, tuple will do constant pre allocation, while list will do variable pre allocation
4. Speed of retrieving element from tuple and list are similar, tuple is still a bit faster because of tuple using `direct access`


#### 4. Index Base and Slice Bounds - Rationale
1. Why does sequence indexing start at 0, and not 1?
2. Why does a sequence slices s[i:j] include s[i], but exclude s[j]?

For example a list s = [1, 2, 3, 4, 5]
If we do lower_boundary <= index < upper_boundary, i.e. 0 <= index < len(s), in our case it is 0 <= index < 5, that is most efficient. We can easily get some useful information:
1. number of elements: upper_boundary - lower_boundary -> 5 - 0 = 5
2. how many elements before an index, for example '2', easily we know there are 2 elements before '2', which are '0', and '1'



#### 5. Copying Sequences
There are many ways to do `shallow copy`:
```py
s = [1, 2, 3]

# 1. simple loop
cp1 = []
for item in s:
    cp1.append(item)
print(cp1)
print(cp1 is s)  # False
print(cp1[0] is s[0])  # True. Shallow Copy


# 2. list comprehension
cp2 = [item for item in s]
print(cp2 is s)  # False
print(cp2[0] is s[0])  # True. Shallow Copy

# 3. The copy method. which only implemented for mutable type
cp3 = s.copy()
print(cp3 is s)  # False
print(cp3[0] is s[0])  # True. Shallow Copy

# 4. The copy method. which only implemented for mutable type
cp4 = s[:]
print(cp4 is s)  # False
print(cp4[0] is s[0])  # True. Shallow Copy

# 5. list() constructor
cp5 = list(s)
print(cp5 is s)  # False
print(cp5[0] is s[0])  # True. Shallow Copy
```


##### Shallow copy is likely to cause problem for mutable types
```py
s1 = [[1, 2], [3, 4]]

cp6 = s1.copy()
cp6[0][1] = 100

print(cp6)  # [[1, 100], [3, 4]]
print(s1)   # [[1, 100], [3, 4]]
```
Reason: `Shallow copy` create a new list, however for the elements inside of it, `Shallow copy` only copy the address of the elements. It is ok for immutable types like integer, but for mutable type like **list**, it may cause some problem.



##### Use copy, deepcopy from 'copy' module
Easiest way to do deepcopy is use `deepcopy` method from copy module
```py
# use copy, deepcopy from 'copy' module
from copy import copy, deepcopy

s2 = [[1, 2], [3, 4]]
cp7 = copy(s2)

cp7[0][1] = 100

print(cp7)  # [[1, 100], [3, 4]]
print(s2)   # [[1, 100], [3, 4]]


s3 = [[1, 2], [3, 4]]
cp8 = deepcopy(s3)

cp8[0][1] = 100

print(cp8)  # [[1, 100], [3, 4]]
print(s3)   # [[1, 2], [3, 4]]
```
