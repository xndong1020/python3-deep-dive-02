from itertools import repeat

iter1 = [1, 2, 3]  # sequence
iter2 = repeat("spam", 3)  # lazy iterator
iter3 = (5, 6)  # tuple

# manually chain iterables
def chain_(*args):
    for itor in args:
        yield from itor


itor = chain_(iter1, iter2, iter3)

print(itor)  # <generator object chain_ at 0x0000023DA6085660>
print(list(itor))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]


# use chain as follows:

from itertools import chain

iter2 = repeat("spam", 3)  # iter2 was exhausted in previous code
lazy_itor = chain(iter1, iter2, iter3)

iter2 = repeat("spam", 3)  # iter2 was exhausted in previous code
lazy_itor02 = chain.from_iterable([iter1, iter2, iter3])

print(list(lazy_itor))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]
print(list(lazy_itor02))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]

# manually create from_iterable
def _from_iterable(it):
    for sub_it in it:
        yield from sub_it


iter2 = repeat("spam", 3)  # iter2 was exhausted in previous code
lazy_iter03 = _from_iterable([iter1, iter2, iter3])

print(list(lazy_iter03))  # [1, 2, 3, 'spam', 'spam', 'spam', 5, 6]

