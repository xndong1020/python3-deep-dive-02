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
