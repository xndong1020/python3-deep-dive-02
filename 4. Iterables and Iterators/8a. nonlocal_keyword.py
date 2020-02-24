"""
The nonlocal keyword is used to work with variables inside nested functions, 
where the variable should not belong to the inner function.

Use the keyword nonlocal to declare that the variable is not local.
"""


def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc


counter_inc = counter()  # get the nested inc function, and its closure (i)

print(counter_inc())  # 1
print(counter_inc())  # 2
print(counter_inc())  # 3
