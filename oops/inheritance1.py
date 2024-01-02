class Father():
    def walk(self):
        print('walking')

    def talk(self):
        print('talking')


class child(Father):
    def sing(self):
        print('singing')


ch = child()
ch.walk()
