"""
class Person:
    def __init__(self, name, data):
        self.__name = name
        self.__old = data

    @property
    def data(self):
        return self.__old

    @data.setter
    def data(self, data):
        self.__old = data

    @data.deleter
    def data(self):
        del self.__old


p = Person('Kirill', 20)
p.data = 35
del p.data
print(p.__dict__)

# step 5
class Car:
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if type(model) == str and 2 <= len(model) <= 100:
            self.__model = model

# step 6
class WindowDlg:
    def __init__(self, title, width, height):
        self.__height = height
        self.__width = width
        self.__title = title

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__width:
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__height:
                self.show()
            self.__height = value

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')



# step 7
class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):
        if self.last:
            self.last.next = obj

        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        h = self.top
        if h is None:
            return
        while h and h.next != self.last:
            h = h.next
        if h:
            h.next = None
        last = self.last
        self.last = h
        if self.last is None:
            self.top = None
        return last

    def get_data(self):
        s = []
        h = self.top
        while h:
            s.append(h.data)
            h = h.next
        return s



# step 8
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.__check(x) else 0
        self.__y = y if self.__check(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check(y):
            self.__y = y

    @classmethod
    def __check(cls, data):
        if not isinstance(data, (int, float)):
            return False
        if not (cls.MIN_COORD <= data <= cls.MAX_COORD):
            return False
        return True

    @staticmethod
    def norm2(vector):
        return vector.__x ** 2 + vector.__y ** 2


r = RadiusVector2D()
r.x = 100
r.y = 10
print(r.__dict__)

x = RadiusVector2D.norm2(r)
print(x)
"""
#step 9
class TreeObj:
    def __init__(self,indx,value=None):
        self.indx=indx