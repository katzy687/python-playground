class Yo(object):
    # def __init__(self):
    #     print("hello")
    # def hi(self):
    #     print("hi")
    pass


class Dude(Yo):
    def __init__(self):
        super(Dude, self).__init__()


x = Dude()