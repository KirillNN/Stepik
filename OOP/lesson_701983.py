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

# step 8
class Line:
    def __init__(self, x1, y1, x2, y2):
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


line = Line(1, 2, 3, 4)
line.draw()



# step 9
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, x1, y1, x2=0, y2=0):
        if x2 != 0:
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)
        else:
            self.__sp = x1
            self.__ep = y1

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} '
              f'{self.__ep.get_coords()}')


rect = Rectangle(0, 0, 20, 34)
rect.draw()



# step 10
class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.tail:
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj
        if not self.head:
            self.head = obj

    def remove_obj(self):
        if self.tail is None:
            return
        prev = self.tail.get_prev()
        if prev:
            prev.set_next(None)
        self.tail = prev
        if self.tail is None:
            self.head = None

    def get_data(self):
        s = []
        h = self.head
        while h:
            s.append(h.get_data())
            h = h.get_next()
        return s


lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
"""
# step 11
from random import randint
from string import ascii_lowercase, digits, ascii_uppercase


class EmailValidator:
    EMAIL_CHARS = ascii_uppercase + ascii_lowercase + digits + '_.@'
    EMAIL_RANDOM_CHARS = ascii_uppercase + ascii_lowercase + digits + '_'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email):
        if not cls.__is_email_str(email):
            return False
        if not set(email) < set(cls.EMAIL_CHARS):
            return False
        s = email.split('@')
        if len(s) != 2:
            return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if '.' not in s[1]:
            return False
        if email.count('..') > 0:
            return False

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def get_random_email(cls):
        n = randint(4, 20)
        length = len(cls.EMAIL_RANDOM_CHARS) - 1
        return ''.join(cls.EMAIL_RANDOM_CHARS[randint(0, length)] for i in range(n)) + '@gmail.com'


print(EmailValidator.check_email('sc_lib@list.ru'))










