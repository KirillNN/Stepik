# step 5
"""
class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f'Воспроизведение {self.filename}')


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open('filemedia1')
media2.open('filemedia2')
media1.play()
media2.play()



# step 6
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(' '.join([str(x) for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]]))


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

# step 8
import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for i in range(len(fields)):
                setattr(self, fields[i], lst_values[i])
            return True
        else:
            return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()


# step 10
import sys

# программу не менять, только добавить два метода
lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def select(self, a, b):
        b = min(b, len(self.lst_data) - 1)
        return self.lst_data[a:b + 1]

    def insert(self, data):
        for line in data:
            self.lst_data.append(dict(zip(DataBase.FIELDS, line.split())))


db = DataBase()
db.insert(lst_in)
"""


# step 11
class Translator:
    trans_dict = {}

    def add(self, eng, rus):
        if eng not in self.trans_dict:
            self.trans_dict[eng] = [rus]
        else:
            if rus not in self.trans_dict[eng]:
                self.trans_dict[eng] += [rus]

    def remove(self, eng):
        self.trans_dict.pop(eng)

    def translate(self, eng):
        return self.trans_dict[eng]


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(*tr.translate('go'))
