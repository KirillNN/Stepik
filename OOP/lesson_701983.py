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
# step 4



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

# step 5
class Money:
    def __init__(self, money):
        self.__money = 0
        if self.__check_money(money):
            self.__money = money

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()

    @classmethod
    def __check_money(cls, money):
        return isinstance(money, int) and money >= 0

mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()    # 100
m2 = mn_2.get_money()    # 120
pass



# step 7
class Book:
    def __init__(self, author, title, price):
        self.__author = author
        self.__title = title
        self.__price = price
        pass

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


book = Book('Lutzh', 'Python', 2000)
"""
# step 8
class Line:
    def __init__(self, x1, y1, x2, y2):
        pass

    def set_coords(self, x1, y1, x2, y2):
        pass

    def get_coords(self):
        pass

    def draw(self):