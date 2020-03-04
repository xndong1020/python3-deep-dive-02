from itertools import tee, repeat, chain

itor = repeat("spam", 3)

itor_copies = tee(itor, 3)

print(itor_copies)
# (<itertools._tee object at 0x000001EB4E33E340>, <itertools._tee object at 0x000001EB4E33E380>, <itertools._tee object at 0x000001EB4E33E3C0>)

print(type(itor_copies))  # tuple

print(
    list(chain.from_iterable(itor_copies))
)  #  ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']


def create_iter():
    return repeat("spam", 3)


iters = []

for _ in range(3):
    iters.append(create_iter())

print(iters)  # [repeat('spam', 3), repeat('spam', 3), repeat('spam', 3)]
print(list(chain.from_iterable(iters)))
# ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam']
