"""
without lazy evaluation
"""
import math


# class Circle:
#     def __init__(self, r):
#         self.radius = r

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, r):
#         print("calculating area ...", r)
#         self._radius = r
#         # no lazy evaluation, whenever r is changed, self.area is re-calculated
#         self.area = math.pi * (r ** 2)


# circle = Circle(10)
# print(circle.radius)  # 10
# print(circle.area)  #  314.1592653589793


# class Circle:
#     def __init__(self, r):
#         self.radius = r

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, r):
#         self._radius = r

#     @property
#     def area(self):
#         print("calculating area ...")
#         # still no lazy evaluation, but not re-calculate when radius change
#         return math.pi * (self.radius ** 2)


# circle = Circle(10)
# print(circle.radius)
# print(circle.area)
# print(circle.area)
# print(circle.area)

# """
# 10
# calculating area ...
# 314.1592653589793
# calculating area ...
# 314.1592653589793
# calculating area ...
# 314.1592653589793
# """


# class Circle:
#     def __init__(self, r):
#         self._radius = r
#         self._area = None

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, r):
#         if self._radius != r:
#             self._radius = r
#             # when radius changed, reset the area property to None.
#             self._area = None

#     @property
#     def area(self):
#         if self._area == None:
#             print("calculating area ...")
#             # lazy evaluation, only re-calculate when self._area is none
#             self._area = math.pi * (self.radius ** 2)
#             return self._area

#         # returns cached value
#         return self._area


# circle = Circle(10)
# print(circle.radius)
# print(circle.area)
# print(circle.area)
# print(circle.area)
# circle.radius = 11
# print(circle.area)


# """
# 10
# calculating area ...
# 314.1592653589793
# 314.1592653589793
# 314.1592653589793
# calculating area ...
# 380.132711084365
# """

"""

Factorials (阶乘). for example,  6! is 1×2×3×4×5×6 = 720
"""


class Factorials:
    def __iter__(self):
        return self.FactorialsIterator()

    class FactorialsIterator:
        def __init__(self):
            self.current = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.current)
            self.current += 1
            return result


factorials = Factorials()
factorials_iter = iter(factorials)
facts = [next(factorials_iter) for _ in range(7)]

print(facts)  # [1, 1, 2, 6, 24, 120, 720]
