# import os
# from collections import namedtuple

# # simplest way to read file line by line
# def cast_data_type(data_type, value):
#     if data_type == "DOUBLE":
#         return float(value)
#     elif data_type == "INT":
#         return int(value)
#     else:
#         return str(value)


# def cast_row(data_types, data_row):
#     # return [cast_data_type(data_types[idx], data) for idx, data in enumerate(data_row)]
#     # or another way of doing the same thing
#     return [
#         cast_data_type(data_type, data) for data_type, data in zip(data_types, data_row)
#     ]


# cars_data = []
# with open(f"{os.path.dirname(__file__)}/cars.csv") as file:
#     row_index = 0
#     for line in file:
#         # for first line, which is the 'columns' header
#         if row_index == 0:
#             columns = line.strip("\n").split(";")
#             Car = namedtuple("Car", columns)  #  Declaring namedtuple
#         # for second line, which is the 'data types' header
#         elif row_index == 1:
#             data_types = line.strip("\n").split(";")
#         else:
#             # initializing a "Car" namedtuple object, unpack data, then add to "cars_data" list
#             cars_data.append(Car(*cast_row(data_types, line.strip("\n").split(";"))))

#         row_index += 1


import os
from collections import namedtuple

# simplest way to read file line by line
def cast_data_type(data_type, value):
    if data_type == "DOUBLE":
        return float(value)
    elif data_type == "INT":
        return int(value)
    else:
        return str(value)


def cast_row(data_types, data_row):
    # return [cast_data_type(data_types[idx], data) for idx, data in enumerate(data_row)]
    # or another way of doing the same thing
    return [
        cast_data_type(data_type, data) for data_type, data in zip(data_types, data_row)
    ]


cars_data = []
with open(f"{os.path.dirname(__file__)}/cars.csv") as file:
    # retrieve the iterator from file iterable
    file_iterator = iter(file)
    # manually read first line from iterator
    columns = next(file_iterator).strip("\n").split(";")
    # manually read second line from iterator
    data_types = next(file_iterator).strip("\n").split(";")
    Car = namedtuple("Car", columns)  #  Declaring namedtuple

    # start to read the remaining lines
    cars_data = [
        Car(*cast_row(data_types, line.strip("\n").split(";")))
        for line in file_iterator
    ]


print(cars_data)
