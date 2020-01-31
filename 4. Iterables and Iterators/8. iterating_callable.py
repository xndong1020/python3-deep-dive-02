# def counter():
#     i = 0

#     def inc():
#         nonlocal i
#         i += 1
#         return i

#     return inc


# class CounterIterator:
#     def __init__(self, counter_callable, sentinel):
#         self._counter_callable = counter_callable
#         self._sentinel = sentinel

#     def __iter__(self):
#         return self

#     def __next__(self):
#         result = self._counter_callable()
#         if result == self._sentinel:
#             raise StopIteration
#         else:
#             return result


# counter = counter()  # returns inc() function, with 'i' as its closure
# print(counter)  # <function counter.<locals>.inc at 0x0000023109FEDB80>
# counter_iter = CounterIterator(counter, 5)
# print(counter_iter)  # <__main__.CounterIterator object at 0x0000026EBD5C8DF0>

# [print(i) for i in counter_iter]

# """
# 1
# 2
# 3
# 4
# """


# def counter():
#     i = 0

#     def inc():
#         nonlocal i
#         i += 1
#         return i

#     return inc


# class CounterIterator:
#     def __init__(self, counter_callable, sentinel):
#         self._counter_callable = counter_callable
#         self._sentinel = sentinel

#     def __iter__(self):
#         return self

#     def __next__(self):
#         result = self._counter_callable()
#         if result == self._sentinel:
#             raise StopIteration
#         else:
#             return result


# counter = counter()  # returns inc() function, with 'i' as its closure
# print(counter)  # <function counter.<locals>.inc at 0x0000023109FEDB80>

# counter()  # closure i changed to 1
# counter()  # closure i changed to 2

# # # now the counter function closure is 3
# counter_iter = CounterIterator(counter, 5)
# print(counter_iter)  # <__main__.CounterIterator object at 0x0000026EBD5C8DF0>

# for i in counter_iter:
#     print(i)

# print(next(counter_iter))  # 6

# """
# 3
# 4
# 6
# """


# def counter():
#     i = 0

#     def inc():
#         nonlocal i
#         i += 1
#         return i

#     return inc


# class CounterIterator:
#     def __init__(self, counter_callable, sentinel):
#         self._counter_callable = counter_callable
#         self._sentinel = sentinel
#         self.is_consumed = False

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.is_consumed:
#             raise StopIteration

#         result = self._counter_callable()
#         if result == self._sentinel:
#             self.is_consumed = True
#             raise StopIteration
#         else:
#             return result


# counter = counter()  # returns inc() function, with 'i' as its closure
# # # now the counter function closure is 3
# counter_iter = CounterIterator(counter, 5)

# for i in counter_iter:
#     print(i)

# print(next(counter_iter))  # StopIteration

# """
# 1
# 2
# 3
# 4

# StopIteration
# """

# def counter():
#     i = 0

#     def inc():
#         nonlocal i
#         i += 1
#         return i

#     return inc


# counter = counter()  # returns inc() function, with 'i' as its closure

# # now the counter function closure is 4
# counter_iter = iter(counter, 5)
# print(counter_iter)  # <callable_iterator object at 0x0000029AB3B28DF0>

# [print(i) for i in counter_iter]
# """
# 1
# 2
# 3
# 4
# """
# print(next(counter_iter))  # StopIteration

# import random

# random_iter = iter(lambda: random.randint(0, 10), 8)  # random number cannot equal to 8

# for num in random_iter:
#     print(num)


def countdown():
    start = 6

    def dec():
        nonlocal start
        start -= 1
        return start

    return dec


countdown_iter = iter(countdown(), 0)

for i in countdown_iter:
    print(i)

"""
5
4
3
2
1
"""
