from collections import namedtuple

# create an template for 'Person' namedtuple, with 2 attributes, "first", "last"
Person = namedtuple("Person", ["first", "last"])


class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [
                f"{person.first.capitalize()} {person.last.capitalize()}" for person in persons
            ]
        except (
            TypeError,
            AttributeError,
        ):  # TypeError when persons is not iterable, AttributeError when person doesn't have proper attributes
            print("Error")

    def __iter__(self):
        # the built-in iter(iterable) method will return an iterator, we delegate the iteration logic to that iterator
        return iter(self._persons)


persons = [Person("niCoLE", "dong"), Person("jeREMY", "gU"), Person("hArPER", "gU")]

person_iter = iter(PersonNames(persons))

[print(person) for person in person_iter]


"""
Nicole Dong
Jeremy Gu
Harper Gu
"""
