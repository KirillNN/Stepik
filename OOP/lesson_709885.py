class Server:
    pass


class Router:
    def __init__(self):
        self.buffer = []

    @staticmethod
    def link(server):
        pass

    @staticmethod
    def unlink(server):
        pass

    @staticmethod
    def send_data():
        pass


class Data:
    pass


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
