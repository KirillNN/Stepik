"""
attribute (без подчеркиваний) - публичное свойство (public)
_attribute - режим доступа protected (служит для обращения внутри класса и во всех его дочерних классах)
__attribute - режим доступа private (служит для обращения только внутри класса)

class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y


pt = Point(1, 2)
print(pt._x, pt._y)

class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')

    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
# print(pt.get_coord())
print(dir(pt))
print(pt._Point__x)
"""

"""
step 4
"""


class Clock:
    def __init__(self, tm):
        self.__time = 0
        if self.__check_time(tm):
            self.__time = tm

    @classmethod
    def __check_time(cls, tm):
        return isinstance(tm, int) and 0 <= tm < 100_000

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


clock = Clock(4530)
print()
