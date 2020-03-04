result1 = zip([1, 2, 3], [10, 20], ["a", "b", "c", "d"])
print(result1)  # <zip object at 0x10a727fa0>
print(list(result1))  # [(1, 10, 'a'), (2, 20, 'b')]

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
