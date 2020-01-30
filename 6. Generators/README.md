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
