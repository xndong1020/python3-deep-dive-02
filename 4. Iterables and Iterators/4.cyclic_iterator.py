"""
1 2 3 4 5 6 7 8 9 ...

N S W E


1N 2S 3W 4E 5N 6S 7W 8E 9N 10S ...
"""


# class CyclicIterator:
#     def __init__(self, iterable):
#         self._iterable = iterable
#         self._index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         """
#         0 % 4 = 0， combined = self._iterable[0] -> N
#         1 % 4 = 1， combined = self._iterable[1] -> S
#         2 % 4 = 2， combined = self._iterable[2] -> W
#         3 % 4 = 3， combined = self._iterable[3] -> E
#         4 % 4 = 0， combined = self._iterable[0] -> N
#         5 % 4 = 1， combined = self._iterable[1] -> S
#         """
#         current = self._iterable[self._index % len(self._iterable)]
#         self._index += 1
#         return current


# cyclic_iter = CyclicIterator("NSWE")
# """cyclic_iter is infinite iterator, which returns something like
# N
# S
# W
# E
# N
# S
# W
# E
# N
# S
# """

# # combined = zip(range(1, 11), cyclic_iter)
# """ zip returns list of tuple
# (1, 'W')
# (2, 'E')
# (3, 'N')
# (4, 'S')
# (5, 'W')
# (6, 'E')
# (7, 'N')
# (8, 'S')
# (9, 'W')
# (10, 'E')
# """

# # for num, direction in list(combined):
# #     print(f"{num}{direction}")

# [print(f"{num}{direction}") for num, direction in zip(range(1, 11), cyclic_iter)]

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


# class CyclicIterator:
#     def __init__(self, iterable):
#         self._iterable = iterable
#         self._index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         """
#         0 % 4 = 0， combined = self._iterable[0] -> N
#         1 % 4 = 1， combined = self._iterable[1] -> S
#         2 % 4 = 2， combined = self._iterable[2] -> W
#         3 % 4 = 3， combined = self._iterable[3] -> E
#         4 % 4 = 0， combined = self._iterable[0] -> N
#         5 % 4 = 1， combined = self._iterable[1] -> S
#         """
#         current = self._iterable[self._index % len(self._iterable)]
#         self._index += 1
#         return current


# cyclic_iter = CyclicIterator("NSWE")
# items = [f"{i}{next(cyclic_iter)}" for i in range(1, 11)]

# print(items)  # ['1N', '2S', '3W', '4E', '5N', '6S', '7W', '8E', '9N', '10S']


# class CyclicIterator:
#     def __init__(self, iterable):
#         self._iterable = iterable

#     def __iter__(self):
#         return self

#     def __next__(self):
#         # delegate the iterator logic to the __iter__ of self._iterable
#         delegated_iterator = iter(self._iterable)
#         current = next(delegated_iterator)
#         return current


# cyclic_iter = CyclicIterator({"N", "S", "W", "E"})

# for _ in range(10):
#     print(next(cyclic_iter))

# """
# E
# E
# E
# E
# ...
# """


# class CyclicIterator:
#     def __init__(self, iterable):
#         self._iterable = iterable
#         self._iterator = iter(self._iterable)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         current = next(self._iterator)
#         return current


# cyclic_iter = CyclicIterator({"N", "S", "W", "E"})

# for _ in range(10):
#     print(next(cyclic_iter))


# """
# W
# N
# S
# E
# Traceback (most recent call last):
#   File "4. Iterables and Iterators/4.cyclic_iterator.py", line 152, in <module>
#     print(next(cyclic_iter))
#   File "4. Iterables and Iterators/4.cyclic_iterator.py", line 145, in __next__
#     current = next(self._iterator)
# StopIteration
# """


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
