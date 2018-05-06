class Hello:

    def __init__(self,name):
        self._name = name

    def sayHello(self):
        print('Hello {0}'.format(self._name))


class Hi(Hello):

    def __init__(self,name):
        Hello.__init__(self,name)

    def sayHi(self):
        print("Hi {0}".format(self._name))

h = Hello("baidu")
h.sayHello()

hi = Hi("xwh")
hi.sayHi()
