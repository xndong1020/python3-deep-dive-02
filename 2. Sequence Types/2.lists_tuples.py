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


from timeit import timeit

print(timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10_000_000))
# .10960877799999999

print(timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10_000_000))
# .1.230675957


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = list(l1)  # list() constructor will create a new list object

print(l1 is l2, id(l1), id(l2))  # False 4513944272 4514126816

l1[0] = 0  # if you change a element in l1, l2 is not affected
print(l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
t2 = tuple(t1)

print(t1 is t2, id(t1), id(t2))  # True 4408873936 4408873936


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

l = list()
prev = sys.getsizeof(l)
print(f"{0} items: {prev} bytes")
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

tt = tuple(range(100_000))
ll = list(tt)

print(timeit("tt[99_999]", globals=globals(), number=10_000_000))
# 0.5591784460000002
print(timeit("ll[99_999]", globals=globals(), number=10_000_000))
# 0.5623680189999998
