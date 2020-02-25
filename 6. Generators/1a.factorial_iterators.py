from math import factorial


# class FactorialIterator:
#     def __init__(self, upper_limit):
#         self._upper_limit = upper_limit
#         self._idx = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._idx >= self._upper_limit:
#             raise StopIteration

#         result = factorial(self._idx)
#         self._idx += 1
#         return result


# factorial_iter = FactorialIterator(5)

# for num in factorial_iter:
#     print(num)

# """
# 1
# 1
# 2
# 6
# 24
# """


# def factorial_func():
#     idx = 0

#     def calc():
#         nonlocal idx
#         result = factorial(idx)
#         idx += 1
#         return result

#     return calc


# # set the sentinel value to factorial(5),
# # meaning when the iteration return value is equal to factorial(5), then stop iteration
# factorial_iter = iter(factorial_func(), factorial(5))

# for num in factorial_iter:
#     print(num)

# """
# 1
# 1
# 2
# 6
# 24
# """

# when Python sees factorial_func function as a generator function, which will return a generator object
def factorial_func(upper_limit):
    for idx in range(upper_limit):
        yield factorial(idx)


# <generator object factorial_func at 0x000001A458BC6660>
factorial_iter = factorial_func(5)

for num in factorial_iter:
    print(num)

# """
# 1
# 1
# 2
# 6
# 24
# """
