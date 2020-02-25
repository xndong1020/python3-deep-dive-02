# 6. Generators

### 1. 'yield' keyword

pseudo code for 'yield' keyword

```py
def factorials(n):
  for i in range(n):
    emit factorial(n)
    pause execution here
    wait for resume
  return 'done'!
```

The 'yield' keyword does exactly what we want:

1. it emits a value
2. the function is effectively **`suspended`** (but it remember its current state)
3. calling next on the function will **`resume`** running the function right after the 'yield' statement
4. if function **`returns`** something instead of yielding, then function stops running -> and raise StopIteration exception

```py
def song():
    print("line 1")
    yield 1
    print("line 2")
    yield 2


nums_gen = song()

print(nums_gen)  # <generator object song at 0x0000019C9F2E5660>

for _ in range(5):
    print(next(nums_gen))


"""
line 1
1
line 2
2
Traceback (most recent call last):
  File "6. Generators/1. yield_baisc.py", line 13, in <module>
    print(next(nums_iter))
StopIteration
"""
```

Generators:

1. a function that uses the yield statement, is called a **`generator function`**
2. calling this function will return a **`generator object`**, we can think of functions that contain the yield statement as **`generator factories`**
3. The **`generator object`** is created by Python when the function is called
4. In fact, generators are **`iterators`**, it implements the iterator protocol, so we can use `next()`, and `iter()`, which returns itself
5. generators are inherently **`lazy`** iterators, it yield a value once at a time
6. When you call next(), the resulting generator:
   - the function body will execute until it encounters a 'yield' statement
   - it yields the value, then it suspends itself
   - until next is called again -> suspended function resumes execution
   - if it encounters a return statement (or reach the end of the function, which implicitly returns `None`), we got a StopIteration exception, and the return value is the exception message

### 1a. 3 way of creating a factorial Iterators:

1. manually create iterator class

```py
from math import factorial


class FactorialIterator:
    def __init__(self, upper_limit):
        self._upper_limit = upper_limit
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= self._upper_limit:
            raise StopIteration

        result = factorial(self._idx)
        self._idx += 1
        return result


factorial_iter = FactorialIterator(5)

for num in factorial_iter:
    print(num)

"""
1
1
2
6
24
```

2. Use the second overloaded version of iter() method: iter(callable, sentinel)

```py
def factorial_func():
    idx = 0

    def calc():
        nonlocal idx
        result = factorial(idx)
        idx += 1
        return result

    return calc


# set the sentinel value to factorial(5),
# meaning when the iteration return value is equal to factorial(5), then stop iteration
factorial_iter = iter(factorial_func(), factorial(5))

for num in factorial_iter:
    print(num)

"""
1
1
2
6
24
"""
```

3. Use generator

When Python sees a function which contains "yield" keyword, this function will NOT be seen as a regular function. Instead it will be treated as a generator function, which will return a generator object

```py
# generator function (generator factory)
def factorial_func(upper_limit):
    for idx in range(upper_limit):
        yield factorial(idx)


# <generator object factorial_func at 0x000001A458BC6660>
factorial_iter = factorial_func(5)

for num in factorial_iter:
    print(num)

"""
1
1
2
6
24
"""
```

### 1b. Fibonacci Sequence (Fibonacci 数列)

1 1 2 3 5 8 13 ...

Recursive formula for Fibonacci sequence:
Fib(n) = Fib(n - 1) + Fib(n - 2)

Fib(0) defined as 1

Fib(1) defined as 1

Simplest way of calculating Fibonacci:

```py
def fibonacci_recursive(upper_limit):
    if upper_limit <= 1:
        return 1

    return fibonacci_recursive(upper_limit - 1) + fibonacci_recursive(upper_limit - 2)


[print(fibonacci_recursive(i)) for i in range(7)]


"""
1
1
2
3
5
8
13
"""
```

However, recursive without caching means we need to calculate everything time during iteration, hence it is very inefficient

```py
# test performance
from timeit import timeit

result = timeit("fibonacci_recursive(29)", globals=globals(), number=10)
print(result)  # 2.3198842
```

use caching will be helpful

```py
from functools import lru_cache

@lru_cache()
def fibonacci_recursive(upper_limit):
    if upper_limit <= 1:
        return 1
    else:
        return fibonacci_recursive(upper_limit - 1) + fibonacci_recursive(
            upper_limit - 2
        )


# test performance
from timeit import timeit

result = timeit("fibonacci_recursive(29)", globals=globals(), number=10)
print(result)  # 2.5799999999999434e-05
```

Another solution is to use tuple unpacking

```py
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


def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


[print(fib(i)) for i in range(7)]


from timeit import timeit

result = timeit("fib(29)", globals=globals(), number=10)
print(result)  # 3.629999999999953e-05 very fast

```

By using this function, we can create an iterator class

```py
def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


class FibonacciIterator:
    def __init__(self, upper):
        self._upper = upper
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= self._upper:
            raise StopIteration
        else:
            result = fib(self._idx)
            self._idx += 1

            return result


fib_iter = iter(FibonacciIterator(7))

for num in fib_iter:
    print(num)
```

We can use generator to create an iterator class

```py
def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


class FibonacciIterator:
    def __init__(self, upper):
        self._upper = upper
        self._idx = 0

    def __iter__(self):
        yield from iter((fib(i) for i in range(self._upper)))


fib_iter = iter(FibonacciIterator(7))

for num in fib_iter:
    print(num)

```

Now, the fib(n) function can be improved by using generator function

```py
def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


[print(num) for num in fib(7)]

"""
2
3
5
8
13
21
"""
```

However, the result is wrong. It should be 1 1 2 3 5 8 13 21, 1 1 is missing. It is because within the loop, 1 1 is not yield
to fix it:

```py
def fib(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n - 1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

# now the fib(n) is a generator function, it will return an generator object
[print(num) for num in fib(7)]

"""
1
1
2
3
5
8
13
21
"""
```

Now the problem is, it returns 8 numbers not 7
To fix it:

```py
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
```
