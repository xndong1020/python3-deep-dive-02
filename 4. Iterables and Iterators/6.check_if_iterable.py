class SimpleIterable:
    def __iter__(self):
        return "Nope"


print("__iter__" in dir(SimpleIterable))  # True

for i in SimpleIterable:  # TypeError: 'type' object is not iterable
    print(i)


try:
    for i in SimpleIterable:  # TypeError: 'type' object is not iterable
        print(i)
except TypeError:
    print("not iterable")
