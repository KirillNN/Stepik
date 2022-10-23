# дескрипторы
"""
class Point3D:
    def __init__(self, x, y, z):
        self.x = x  # при совпадении имен свойств срабатывают сеттеры
        self.y = y
        self.z = z

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


p = Point3D(1, 2, 3)
print(p.__dict__)

# дескриптор не данных
class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


# дескриптор данных
class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)  # лучше записать так

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f'__set__: {self.name} = {value}')
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)  # лучше записать так


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(1, 2, 3)
print(p.__dict__, p.z, p.xr)

class StringField:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y

db = DataBase('hi', 'low')
db.__dict__['x'] = 'top'
print(db.x)
# Будет выведено 'hi', так как StringField - это дескриптор данных
# и он имеет наибольший приоритет при обращении к атрибутам,
# поэтому в строчке db.x будет обращение к дескриптору,
# а не к локальному свойству.
"""


class FloatValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, ow, n):
        self.name = "_" + n

    def __get__(self, ins, ow):
        return getattr(ins, self.name)

    def __set__(self, ins, v):
        self.verify_value(v)
        setattr(ins, self.name, v)


class Cell:
    value = FloatValue()

    def __init__(self, x):
        self.value = x


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell(0.0) for _ in range(m)] for _ in range(n)]


N, M = 5, 3
table = TableSheet(N, M)
count = 1.0
for i in range(N):
    for j in range(M):
        table.cells[i][j].value = count
        count += 1
