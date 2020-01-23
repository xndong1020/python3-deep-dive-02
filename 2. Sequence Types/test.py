# set is not a sequence type, and it doesn't have positional index
s = {1, 2, "x"}
# s[2] # 'set' object is not subscriptable (no indexing)


# tuple is immutable
t = (
    1,
    2,
    3,
)

# t[1] = 4 # TypeError: 'tuple' object does not support item assignment

# but you can do something like
s = (
    [0, 0],
    2,
    4,
)
s[0][1] = 100  # ([0, 100], 2, 4)


# enumerate function
s = "jeremy"

# if you want to loop through a  string, and find the index for each character

for idx, item in enumerate(s):
    print(idx, item)

"""
0 j
1 e
2 r
3 e
4 m
5 y
"""

# reverse a string by using slicing negative steps
s1 = s[-1]  # output 'y'. because if step of -1, means start from the end
s2 = s[
    3:0:-1
]  # output 'ere', start from s[3], which is 'e', and end at s[0], which is 'j'. but upper bound 'j' not included
rev = s[
    ::-1
]  # this means start from very end, stop at very beginning, with step of -1 (from back to start)
