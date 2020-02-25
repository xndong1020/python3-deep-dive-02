"""
Fibonacci 数列
1 1 2 3 5 8 13 ...

Recursive formula for Fibonacci sequence:
Fib(n) = Fib(n - 1) + Fib(n - 2)

Fib(0) defined as 1

Fib(1) defined as 1
"""


# def fibonacci_recursive(upper_limit):
#     if upper_limit <= 1:
#         return 1
#     else:
#         return fibonacci_recursive(upper_limit - 1) + fibonacci_recursive(
#             upper_limit - 2
#         )


# [print(fibonacci_recursive(i)) for i in range(7)]


"""
1
1
2
3
5
8
13
"""


# # test performance
# from timeit import timeit

# result = timeit("fibonacci_recursive(29)", globals=globals(), number=10)
# print(result)  # 2.3198842


# from functools import lru_cache


# @lru_cache()
# def fibonacci_recursive(upper_limit):
#     if upper_limit <= 1:
#         return 1
#     else:
#         return fibonacci_recursive(upper_limit - 1) + fibonacci_recursive(
#             upper_limit - 2
#         )


# # test performance
# from timeit import timeit

# result = timeit("fibonacci_recursive(29)", globals=globals(), number=10)
# print(result)  # 2.5799999999999434e-05


"""
Fibonacci 
1 1 2 3 5 8 13 ...
can be seen as (1, 1), (1, 2), (2, 3), (3, 5)

initially
fib_0 = 1
fib_1 = 1

then (1, 2) -> (2, 3) fib_0 changed from (1, .) to (2, .), which is fib_0 in the next tuple
meanwhile in the next tuple, the value of fib_1 is fib_0 + fib_1
"""


# def fib(n):
#     fib_0 = 1
#     fib_1 = 1
#     for i in range(n - 1):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#     return fib_1


# [print(fib(i)) for i in range(7)]

# from timeit import timeit

# result = timeit("fib(29)", globals=globals(), number=10)
# print(result)  # 3.629999999999953e-05


# def fib(n):
#     fib_0 = 1
#     fib_1 = 1
#     for i in range(n - 1):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#     return fib_1


# class FibonacciIterator:
#     def __init__(self, upper):
#         self._upper = upper
#         self._idx = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self._idx >= self._upper:
#             raise StopIteration
#         else:
#             result = fib(self._idx)
#             self._idx += 1

#             return result


# fib_iter = iter(FibonacciIterator(7))

# for num in fib_iter:
#     print(num)


# def fib(n):
#     fib_0 = 1
#     fib_1 = 1
#     for i in range(n - 1):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#     return fib_1


# class FibonacciIterator:
#     def __init__(self, upper):
#         self._upper = upper
#         self._idx = 0

#     def __iter__(self):
#         yield from iter((fib(i) for i in range(self._upper)))


# fib_iter = iter(FibonacciIterator(7))

# for num in fib_iter:
#     print(num)


# def fib(n):
#     fib_0 = 1
#     fib_1 = 1
#     for i in range(n - 1):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#         yield fib_1


# [print(num) for num in fib(7)]

# """
# 2
# 3
# 5
# 8
# 13
# 21
# """

# now the fib(n) is a generator function, it will return an generator object
# def fib(n):
#     fib_0 = 1
#     yield fib_0
#     fib_1 = 1
#     yield fib_1
#     for i in range(n - 1):
#         fib_0, fib_1 = fib_1, fib_0 + fib_1
#         yield fib_1


# [print(num) for num in fib(7)]

# """
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# """


def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n - 2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


[print(num) for num in fib(7)]

"""
1
1
2
3
5
8
13
"""
