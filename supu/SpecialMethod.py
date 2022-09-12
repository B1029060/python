# __○○__
# (1) __add__: Define the plus symbol when it exists between two objects.

class AddUpNumber:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return f'{self.value}{other.value}'

strnum1 = AddUpNumber(10)
strnum2 = AddUpNumber(20)
print((result := strnum1 + strnum2))    # 1020

# (2) __new__: Customize the initial value of immutable variable before __init__.

class Adds1(int):
    def __new__(cls, value):
        new_value = value + 1
        return super().__new__(cls, new_value)

Ten = Adds1(10)
print(Ten, type(Ten))

# (3) __eq__: Define equal symbol between two objects.
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def __eq__(self, other):
        if isinstance(other, User):
            if self.id == other.id:
                return 'Same'
            else:
                return 'Not same'
        else:
            return 'Wrong Class Using'
User1 = User(10, 'Cookie')
User2 = User(10, 'Candy')
print(User1 == User2)   # Same

# (4) __setitem__, __getitem__: Set and get value in class, used by [].
class SpecialNumber:
    def __setitem__(self, idx, value):
        if idx == 0:
            self.value0 = str(value)
        elif idx == 1:
            self.value1 = str(value) * 2
        elif idx == 2:
            self.value2 = str(value) * 3
        else:
            raise IndexError('Index is only 0, 1, and 2')
    def __getitem__(self, idx):
        if idx == 0:
            return self.value0
        elif idx == 1:
            return self.value1
        elif idx == 2:
            return self.value2
        else:
            raise IndexError('Index is only 0, 1, and 2')
SpNum1 = SpecialNumber()
SpNum1[2] = 40  # __setitem__
print(SpNum1.__getitem__(2))    # 404040

# (5) __str__: Return string when using print(), format(), and so on.
class Hello:
    def __init__(self, name):
        self.name = str(name)
    def __str__(self):
        return 'Hello, ' + self.name + '.'
Person1 = Hello('Annie')
print(Person1)  # Hello, Annie.
