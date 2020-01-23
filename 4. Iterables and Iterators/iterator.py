class Cities:
    def __init__(self, cities):
        self.cities = cities

    def __len__(self):
        return len(self.cities)

    def __iter__(self):
        return CitiesIterator(self)

    def __getitem(self, i):
        return self.cities[i]


class CitiesIterator:
    def __init__(self, cities):
        self.cities = cities
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.cities):
            raise StopIteration
        else:
            city = cities[self._index]
            self._index += 1
            return city


# a iterable will not be exhausted, because it always returns a iterator
cities = ["Sydney", "Canberra", "Perth"]
for c in cities:
    print(c)
for c in cities:
    print(c)

print("****************************")

# once iterator is exhausted, it doesn't return anything
cities_iterator = iter(cities)
for c in cities_iterator:
    print(c)
for c in cities_iterator:
    print(c)
