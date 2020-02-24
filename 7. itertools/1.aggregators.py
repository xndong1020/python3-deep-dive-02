numbers = [1, 10, 20, 100]
pred = lambda x: x < 100

result = any([pred(num) for num in numbers])
print(result)  # True


result = all((pred(num) for num in numbers))
print(result)  # False


doubled = map(lambda x: x * 2, numbers)
print(doubled)  # [2, 20, 40, 200]
