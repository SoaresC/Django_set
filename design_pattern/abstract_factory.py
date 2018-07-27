"""
抽象工厂模式
"""


class ToyFactory(object):
    def __init__(self, toy_kind=None):
        self.toy_kind = toy_kind

    def show_toy(self):
        print(self.toy_kind.show())


class Thomas(object):
    @staticmethod
    def show():
        return "I'm Thomas"


class SuperMan(object):
    @staticmethod
    def show():
        return "I'm Superman"


if __name__ == '__main__':
    toy_factory = ToyFactory(SuperMan)
    toy_factory.show_toy()
