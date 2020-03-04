# for sequence types we use index
numbers = [1, 2, 3, 4, 5]

bits1 = numbers[0:3]
print(bits1)  # [1, 2, 3]

bits2 = numbers[0:3:2]  # with step of 2
print(bits2)  # [1, 3]

# for sequence types we use slice
slice1 = slice(0, 3)
print(type(slice1))  # <type 'slice'>

bits3 = numbers[slice1]
print(bits3)  # [1, 2, 3]

slice2 = slice(0, 3, 2)
bits4 = numbers[slice2]
print(bits4)  # [1, 3]

from math import factorial


def factorials_infinite():
    index = 0
    while True:
        yield factorial(index)
        index += 1


def factorials_finite(n):
    for i in range(n):
        yield factorial(i)


# generator object
facts = factorials_finite(10)
# print(facts[0:3])


# our own islice_ function:
def islice_(iterable, start, stop):
    # skip any item from 0 to start position
    for _ in range(0, start):
        next(iterable)

    for _ in range(start, stop):
        yield next(iterable)


bits5 = islice_(factorials_infinite(), 3, 10)
print(list(bits5))  # [6, 24, 120, 720, 5040, 40320, 362880]


from itertools import islice

bits6 = islice(factorials_infinite(), 0, 10)
print(bits6)  # <itertools.islice object at 0x102954470>

print(list(bits6))
