from collections import namedtuple

"""
downside of plain tuple is that 
1. the data you store in them can only be pulled out by accessing it through integer indexes. 
You can’t give names to individual properties stored in a tuple. This can impact code readability

2.  It’s hard to ensure that two tuples have the same number of fields and the same properties stored on them. 
This makes it easy to introduce “slip-of-the-mind” bugs by mixing up the field order.
"""
tup = ("hello", object(), 42)
print(tup[2])  # what does index '2' mean?


"""
Namedtuples aim to solve these two problems.

Each object stored in them can be accessed through a unique (human-readable) identifier. 
This frees you from having to remember integer indexes.
"""

# Declaring namedtuple,  we defined a simple Student data type with 3 fields: "name", "age", "DOB".
Student = namedtuple("Student", ["name", "age", "DOB"])

# create "Student" object with values
S = Student("Jeremy", "19", "2541997")

# Access using index
print("The Student age using index is : ", end="")
print(S[0])

# Access using field
print("The Student age using filed is : ", end="")
print(S.name)
