# concatenation is not mutation
names = ["Eric", "John"]
print(id(names))  # 4518273504

names = names + ["Mike"]
print(id(names))  #  4520652064


s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s2 = ["A", "B", "C"]

s[1:7:2] = s2
print(s)  # [1, 'A', 3, 'B', 5, 'C', 7, 8, 9]
