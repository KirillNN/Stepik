"""
# step 3
# здесь объявляйте класс Money
class Money:
    def __init__(self, money):
        self.money = money


my_money = Money(100)
your_money = Money(1000)



# step 4
class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
for i in range(1000):
    x = y = i * 2 + 1
    points.append(Point(x, y))

points[1].color = 'yellow'

# step 5
import random


class Line:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Rect:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = a, b
        self.ep = c, d


elements = []
for _ in range(217):
    a, b, c, d = (random.randint(0, 100) for _ in range(4))
    elements.append(random.choice([Line(0, 0, 0, 0), Rect(a, b, c, d), Ellipse(a, b, c, d)]))


# step 6
class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        a, b, c = self.a, self.b, self.c
        if not all(map(lambda x: type(x) in (int, float), (a, b, c))):
            return 1
        if not all(map(lambda x: x > 0, (a, b, c))):
            return 1
        a, b, c = sorted([self.a, self.b, self.c])
        if c > a + b:
            return 2
        return 3


a, b, c = map(int, input().split())
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())

# step 7
class Graph:
    def __init__(self, data: list, is_show: bool = True):
        self.data = data[::]
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        print('Графическое отображение данных:', *self.data if self.is_show else 'Отображение данных закрыто')

    def show_bar(self):
        print('Столбчатая диаграмма:', *self.data if self.is_show else 'Отображение данных закрыто')

    def set_show(self, fl_show: bool):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

# step 8
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память: ' + "; ".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))]


mb = MotherBoard('1', CPU('1', 5000), Memory('1', 1024), Memory('2', 1024))

# step 9
class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return list(map(lambda x: f'{x.name}: {x.price}', self.goods))


cart = Cart()
cart.add(TV('1', 1000))
cart.add(TV('2', 1000))
cart.add(Table('3', 1000))
cart.add(Notebook('4', 1000))
cart.add(Notebook('5', 1000))
cart.add(Cup('6', 1000))
print(cart.get_list())



# step 10
class ListObject:
    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = list(map(str.strip, sys.stdin.readlines()))

head_obj = ListObject(lst_in[0])
obj = head_obj
for i in range(1, len(lst_in)):
    obj_new = ListObject(lst_in[i])
    obj.link(obj_new)
    obj = obj_new
"""

# step 11
import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines  # число мин вокруг данной клетки поля
        self.mine = mine  # наличие мины в текущей клетке
        self.fl_open = False  # открыта/закрыта клетка


class GamePole:
    def __init__(self, N, M):
        self.n = N  # размер поля
        self.m = M  # общее число мин на поле
        self.pole = [[Cell() for _ in range(self.n)] for _ in range(self.n)]
        self.init()

    def init(self):
        m = self.m
        counter = 1
        while m:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            # print(counter, x, y)
            counter += 1
            if not self.pole[x][y].mine:
                self.pole[x][y].mine = True
                _xy = (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
                for _x, _y in _xy:
                    if 0 <= x + _x < self.n and 0 <= y + _y < self.n:
                        self.pole[x + _x][y + _y].around_mines += 1
                m -= 1
        return True

    def show(self):
        for item in self.pole:
            print(*[x.around_mines if not x.mine else '*' for x in item])


pole_game = GamePole(10, 12)
pole_game.show()
# print(True)
