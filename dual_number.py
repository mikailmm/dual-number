class Dual:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b == 1:
            return f'{self.a}+ε'
        if self.b >= 0:
            return f'{self.a}+{self.b}ε'
        return f'{self.a}{self.b}ε'

    def __repr__(self):
        return self.__str__()