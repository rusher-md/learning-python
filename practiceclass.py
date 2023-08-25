class Dell:
    attr = 'laptop'

    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2

    def best(self):
        return 'best3'


class Python:
    attr = 'react'

    def __init__(self, java, reactjs):
        self.java = java
        self.reactjs = reactjs

    def boring(self):
        return 'boring2'


class Laptop:
    attr = 'dell'

    def __init__(self, name, name3):
        self.name = name
        self.name3 = name3

    def work(self):
        return 'typing'


class Mouse:
    attr = 'red gear'

    def __init__(self, name, name4):
        self.name = name
        self.name4 = name4

    def gaming(self):
        return 'best mouse'


class Bag:
    attr = 'hrx'

    def __init__(self, name, name5):
        self.name = name
        self.name5 = name5

    def use(self):
        return 'commercial use'


class Gta:
    attr = 'best game'

    def __init__(self, name, name6):
        self.name = name
        self.name6 = name6

    def andreas(self):
        return 'gta5'


class Fan:
    attr = 'bajaj'

    def __init__(self, name, name7):
        self.name = name
        self.name7 = name7

    def speed(self):
        return 'quality'


if __name__ == "__main__":
    Dell1 = Dell('best laptop', 'best laptop2')
    Python1 = Python('best language', 'best language2')
    Laptop1 = Laptop('best laptop', 'best laptop2')
    Mouse1 = Mouse('best mouse', 'best mouse 2')
    Bag1 = Bag('best bag', 'Best bag2')
    Gta1 = Gta('best game', 'best game2')
    Fan1 = Fan('best fan', 'Best fan2')

    my_value1 = Dell1.best()
    my_value2 = Python1.boring()
    my_value3 = Laptop1.work()
    my_value4 = Mouse1.gaming()
    my_value5 = Bag1.use()
    my_value6 = Gta1.andreas()
    my_value7 = Fan1.speed()

    print(my_value1, my_value2, my_value3, my_value4, my_value5, my_value6, my_value7)










