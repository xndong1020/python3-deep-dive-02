from itertools import count

count1 = count(10)  # start from 10, step default to 1
print(count1)  # lazy, infinite iterator

###
10
11
12
13
14
15
16
17
18
19
###

for _ in range(10):
    print(next(count1))

count2 = count(1, 2)

for _ in range(10):
    print(next(count2))

###
1
3
5
7
9
11
13
15
17
19
###

count3 = count(10.6, 0.1)

for _ in range(10):
    print(next(count3))

###
10.6
10.7
10.799999999999999
10.899999999999999
10.999999999999998
11.099999999999998
11.199999999999998
11.299999999999997
11.399999999999997
11.499999999999996
###


from itertools import cycle

cycled = cycle(["a", "b", "c"])
print(cycled)  # <itertools.cycle object at 0x00000196D3EDF3C0>

for _ in range(5):
    print(next(cycled))

# a b c a b

from itertools import repeat

# infinite iterator
infinite_spam = repeat("spam")  # Lazy iterator

for _ in range(10):
    print(next(infinite_spam))

# spam spam spam spam spam spam spam spam spam spam

# Optionally, you can specify a count to make the iterator finite
finite_spam = repeat("spam", 3)

print(list(finite_spam))  # ['spam', 'spam', 'spam']
