from functools import reduce

users = [
    {"name": "Jeremy", "department": "IT"},
    {"name": "Nicole", "department": "IT"},
    {"name": "Allen", "department": "Accounting"},
    {"name": "Sarah", "department": "Accounting"},
    {"name": "Josh", "department": "Finance"},
]


def group_user(accumulator, user):
    if user["department"] in accumulator:
        accumulator[user["department"]]["users"].append(user["name"])
    else:
        accumulator[user["department"]] = {}
        accumulator[user["department"]].update({"users": [user["name"]]})
    return accumulator


results = reduce(group_user, users, {})
print("results", results)
# {'IT': {'users': ['Jeremy', 'Nicole']}, 'Accounting': {'users': ['Allen', 'Sarah']}, 'Finance': {'users': ['Josh']}}

# using map
l = [[1, 2], [3, 4]]
result = map(lambda item: item[0] * item[1], l)
print(list(result))  # [2, 12]

# using starmap
from itertools import starmap
from operator import mul  # mul expected 2 arguments

l = [[1, 2], [3, 4]]
result1 = starmap(mul, l)
print(list(result1))  # [2, 12]

# using generator expression
result2 = (mul(*item) for item in l)
print(list(result2))  # [2, 12]

# more than 2 arguments
l = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
result3 = starmap(lambda x, y, z: x + y + z, l)
print(list(result3))  # [6, 60, 600]

# using accumulate function
from itertools import accumulate
from operator import add

l = [1, 2, 3, 4, 5, 6]
results4 = accumulate(l, add)

print(results4)  # <itertools.accumulate object at 0x1057121e0>
for num in results4:
    print(num)  # 1 3 6 10 15 21, all the intermediate results
