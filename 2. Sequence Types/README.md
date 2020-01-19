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
