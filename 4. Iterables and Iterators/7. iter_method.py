"""
For sequence type, __iter__ method may not be implemented. 
In stead, __getitem__ method is used to create iterator
"""


# class Squares:
#     def __init__(self, length):
#         self._length = length

#     def __len__(self):
#         return self._length

#     def __getitem__(self, idx):
#         if idx >= self._length:
#             raise IndexError

#         return idx ** 2


# square = Squares(5)
# square_iter = iter(square)

# print(square_iter)  # <iterator object at 0x000002DDFED00DC0>
# print(list(square_iter))  # [0, 1, 4, 9, 16]

# next(square_iter)  # StopIteration


class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._sequence):
            raise StopIteration
        else:
            elem = self._sequence[self._idx]
            self._idx += 1
            return elem


square = [1, 2, 3, 4, 5]
square_iter = iter(SequenceIterator(square))

print(square_iter)  # <__main__.SequenceIterator object at 0x000001D3D11809A0>

print(list(square_iter))  # [1, 2, 3, 4, 5]
