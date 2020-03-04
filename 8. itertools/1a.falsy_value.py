empty_list = []
print(bool(empty_list))  # False

empty_tuple = ()
print(bool(empty_tuple))  # False

empty_str = ""
print(bool(empty_tuple))  # False


# Empty ranges range(0)
empty_range = range(0)
print(bool(empty_range))  # False

empty_dict = {}
print(bool(empty_str))  # False


class Account:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        print("__bool__ called")
        return self.balance > 0


account1 = Account(500)
print(bool(account1))  # True
account2 = Account(0)
print(bool(account2))  # False


class Inventory:
    def __init__(self, inventories):
        self.inventories = inventories

    def __len__(self):
        return len(self.inventories)


stocks1 = Inventory(["banana", "apple"])
print(bool(stocks1))  # True

stocks2 = Inventory([])
print(bool(stocks2))  # False
