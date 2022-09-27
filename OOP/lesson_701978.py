# step 3
# class Loader:
#     @classmethod
#     def json_parse(cls):
#         return "2"
#
# ld = Loader()
#
#
# print(ld.json_parse(Loader))

# step 4
# class Math:
#     @staticmethod
#     def sqrt(x):
#         return x ** 0.5
#
# m = Math()
# res = m.sqrt(2)
# print()
# step 7
# class Factory:
#     @staticmethod
#     def build_sequence():
#         return []
#
#     @staticmethod
#     def build_number(string):
#         return int(string)
#
#
# class Loader:
#     @staticmethod
#     def parse_format(string, factory):
#         seq = factory.build_sequence()
#         for sub in string.split(","):
#             item = factory.build_number(sub)
#             seq.append(item)
#
#         return seq
#
#
# # эти строчки не менять!
# res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
# step 8
# from string import ascii_lowercase, digits
#
#
# class TextInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.name = self.check_name(name)
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         for char in name:
#             if char not in cls.CHARS_CORRECT:
#                 raise ValueError("некорректное поле name")
#         return name
#
#
# class PasswordInput:
#     CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
#     CHARS_CORRECT = CHARS + CHARS.upper() + digits
#
#     def __init__(self, name, size=10):
#         self.name = self.check_name(name)
#         self.size = size
#
#     def get_html(self):
#         return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"
#
#     @classmethod
#     def check_name(cls, name):
#         if len(name) < 3 or len(name) > 50:
#             raise ValueError("некорректное поле name")
#         for char in name:
#             if char not in cls.CHARS_CORRECT:
#                 raise ValueError("некорректное поле name")
#         return name
#
#
# class FormLogin:
#     def __init__(self, lgn, psw):
#         self.login = lgn
#         self.password = psw
#
#     def render_template(self):
#         return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
#
#
# # эти строчки не менять
# login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
# html = login.render_template()

# step 9
# from string import ascii_lowercase, digits
#
#
# class CardCheck:
#     CHARS_FOR_NAME = ascii_lowercase.upper() + digits
#
#     @staticmethod
#     def check_card_number(number: str):
#         if len(number) != 19:
#             return False
#         for x in number.split('-'):
#             if len(x) != 4 or any([_ not in digits for _ in x]):
#                 return False
#         return True
#
#     @classmethod
#     def check_name(cls, name: str):
#         name_ = name.split()
#         if len(name_) != 2:
#             return False
#         for x in name_:
#             if any([_ not in cls.CHARS_FOR_NAME for _ in x]):
#                 return False
#         return True
#
#
# is_number = CardCheck.check_card_number("1244-5678-9012-0000-5643")
# print(is_number)
# is_name = CardCheck.check_name("SERGEI BALAKIEV")
# print(is_name)

# step 10
# class Video:
#     def create(self, name):
#         self.name = name
#
#     def play(self):
#         print(f'воспроизведение видео {self.name}')
#
#
# class YouTube:
#     videos = []
#
#     @classmethod
#     def add_video(cls, video: Video):
#         cls.videos.append(video)
#
#     @classmethod
#     def play(cls, video_indx):
#         Video.play(cls.videos[video_indx])
#
#
# v1 = Video()
# v2 = Video()
# v1.create('Python')
# v2.create('Python ООП')
# YouTube.add_video(v1)
# YouTube.add_video(v2)
# YouTube.play(0)
# YouTube.play(1)

# step 11
# class AppStore:
#     applications = []
#
#     def add_application(self, app):
#         AppStore.applications.append(app)
#
#     def remove_application(self, app):
#         AppStore.applications.remove(app)
#
#     def block_application(self, app):
#         app.blocked = True
#
#     def total_apps(self):
#         return len(AppStore.applications)
#
#
# class Application:
#     def __init__(self, name, blocked=False):
#         self.name = name
#         self.blocked = blocked


# store = AppStore()
# app_youtube = Application("Youtube")
# store.add_application(app_youtube)
# store.block_application(app_youtube)
# store.remove_application(app_youtube)
# print()

# step 11
class Viber:
    messages = []

    @staticmethod
    def add_message(msg):
        Viber.messages.append(msg)

    @staticmethod
    def remove_message(msg):
        Viber.messages.remove(msg)

    @staticmethod
    def set_like(msg):
        msg.fl_like = not msg.fl_like

    @staticmethod
    def show_last_message(count):
        print(Viber.messages[-count:])

    @staticmethod
    def total_messages():
        return len(Viber.messages)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.set_like(msg)
Viber.remove_message(msg)
