# step 8
# class SingletonFive:
#     __count = 0
#     __inst = 0
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__count < 5:
#             cls.__count += 1
#             cls.__inst = super().__new__(cls)
#             return cls.__inst
#         else:
#             return cls.__inst
#
#     def __init__(self, name):
#         self.name = name
#
#
# objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять


# step 9
# TYPE_OS = 2  # 1 - Windows; 2 - Linux
#
#
# class DialogWindows:
#     name_class = "DialogWindows"
#
#
# class DialogLinux:
#     name_class = "DialogLinux"
#
#
# class Dialog:
#     def __new__(cls, *args, **kwargs):
#         obj = None
#         if TYPE_OS == 1:
#             obj = super().__new__(DialogWindows)
#         else:
#             obj = super().__new__(DialogLinux)
#         obj.name = args[0]
#         return obj
#
#
# dlg = Dialog('hh')
# print(dlg)

# step 10
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def clone(self):
#         return Point(self.x, self.y)
#
#
# pt = Point(1, 2)
# pt_clone = pt.clone()

# step 11
class Factory:
    def build_sequence(self):
        return []
    def build_number(self, string):
        return float(string)

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
print(res)