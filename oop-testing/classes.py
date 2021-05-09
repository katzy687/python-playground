class MyBase(object):
    data1 = "test1"
    data2 = "test2"

    def __init__(self, input1):
        self.input1 = input1

    def hey(self):
        print("hey")


class MySub1(MyBase):
    data1 = "test3"

    def __init__(self):
        super(MySub1, self).__init__('asdf')
        self.lol = "haha"
        super(MySub1, self).hey()
        self.hey()

        # self.hey()

    def hey(self):
        print('yo')

x = MySub1()
print(x.input1)