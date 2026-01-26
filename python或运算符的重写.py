class Test(object):
    def __init__(self,name):
        self.name = name

    def __or__(self, other):
        return MySequece(self, other)
    def __str__(self):
        return str(self.name)
class MySequece(object):
    def __init__(self, *args):
        self.sequence = []
        self.args = args
        for arg in args:
            self.sequence.append(arg)
    
    def __or__(self, other):
        self.sequence.append(other)
        return self
    def run(self):
        for i in self.sequence:
            print(i)
if __name__ == '__main__':
    a= Test("a")
    b= Test("b")
    c= Test("c")

    d=a | b | c
    d.run()
    print(type(d))