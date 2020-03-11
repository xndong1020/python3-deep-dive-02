s = [1, 2, 3]

# 1. simple loop
cp1 = []
for item in s:
    cp1.append(item)
print(cp1)
print(cp1 is s)  # False
print(cp1[0] is s[0])  # True. Shallow Copy


# 2. list comprehension
cp2 = [item for item in s]
print(cp2 is s)  # False
print(cp2[0] is s[0])  # True. Shallow Copy

# 3. The copy method. which only implemented for mutable type
cp3 = s.copy()
print(cp3 is s)  # False
print(cp3[0] is s[0])  # True. Shallow Copy

# 4. The copy method. which only implemented for mutable type
cp4 = s[:]
print(cp4 is s)  # False
print(cp4[0] is s[0])  # True. Shallow Copy

# 5. list() constructor
cp5 = list(s)
print(cp5 is s)  # False
print(cp5[0] is s[0])  # True. Shallow Copy

# shallow copy may be a problem for mutable type
s1 = [[1, 2], [3, 4]]
cp6 = s1.copy()
cp6[0][1] = 100
print(cp6)  # [[1, 100], [3, 4]]
print(s1)   # [[1, 100], [3, 4]]


# use copy, deepcopy from 'copy' module
from copy import copy, deepcopy

s2 = [[1, 2], [3, 4]]
cp7 = copy(s2)

cp7[0][1] = 100

print(cp7)  # [[1, 100], [3, 4]]
print(s2)   # [[1, 100], [3, 4]]


s3 = [[1, 2], [3, 4]]
cp8 = deepcopy(s3)

cp8[0][1] = 100

print(cp8)  # [[1, 100], [3, 4]]
print(s3)   # [[1, 2], [3, 4]]
