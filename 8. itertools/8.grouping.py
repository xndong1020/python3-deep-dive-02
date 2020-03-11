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


# if we change the order of data, result will be very different
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

# so possibly we need to sort it before groupby
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
