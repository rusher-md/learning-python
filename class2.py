class Laptop:
    attr = 'dell'

    def __init__(self, name):
        self.name = name


    def work(self):
        print('typing')


class Mouse:
    attr = 'red gear'

    def __init__(self, name):
        self.name = name

    def gaming(self):
        return ' best mouse'


class Bag:
    attr = 'hrx'

    def __init__(self, name):
        self.name = name

    def use(self):
        return'commercial use'


class Gta:
    attr = 'best game'

    def __init__(self, name):
        self.name = name

    def andreas(self):
        return'gta5'


class Ac:
    attr = 'o general'

    def __init__(self, name):
        self.name = name

    def carrier(self):
        return 'value plus'


if __name__ == "__main__":
    Laptop1 = Laptop('core')
    Mouse1 = Mouse('quantum')
    Gta1 = Gta('cj')
    Ac1 = Ac('klklk')
    Bag1 = Bag('nike')

    Laptop1.work()
    print(dir(Laptop))
    # my_value2 = Mouse1.gaming()
    # my_value3 = Gta1.andreas()
    # my_value4 = Ac1.carrier()
    # my_value5 = Bag1.use()

    # print(my_value, my_value2, my_value3, my_value4, my_value5)





