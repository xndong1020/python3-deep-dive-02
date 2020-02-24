numbers = [1, 50, 2, 88, 3, 100]

small = filter(lambda x: x < 4, numbers)
print(small)  # <filter object at 0x10868a350>
print(list(small))  # [1, 2, 3]


from itertools import filterfalse, compress, takewhile, dropwhile

big = filterfalse(lambda x: x < 4, numbers)
print(big)  # <itertools.filterfalse object at 0x1087b1590>
print(list(big))  # [50, 88, 100]


items = ["apple", "ginger", "banana", "orange", "mongo"]
selectors = [True, False, 1, 0]

selected = compress(items, selectors)
print(selected)  # <itertools.compress object at 0x1100cfc50>
print(list(selected))  # ['apple', 'banana']

takes1 = takewhile(lambda x: x < 60, numbers)
print(takes1)  # <itertools.takewhile object at 0x10732d0a0>
print(list(takes1))  # [1, 50, 2]

takes2 = dropwhile(lambda x: x < 60, numbers)
print(takes2)  # <itertools.dropwhile object at 0x10d072140>
print(list(takes2))  # [88, 3, 100]
