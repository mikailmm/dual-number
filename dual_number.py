from numbers import Number


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

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.a + other.a, self.b + other.b)
        elif isinstance(other, Number):
            return Dual(self.a + other, self.b)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.a - other.a, self.b - other.b)
        elif isinstance(other, Number):
            return Dual(self.a - other, self.b)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Dual):
            return Dual(other.a - self.a, self.b - other.b)
        elif isinstance(other, Number):
            return Dual(other - self.a, -self.b)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.a*other.a, self.a*other.b + self.b*other.a)
        elif isinstance(other, Number):
            return Dual(self.a*other, self.b*other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, Dual):
            return Dual(self.a*other.a, self.b*other.a + self.a*other.b)
        elif isinstance(other, Number):
            return Dual(self.a*other, self.b*other)
        else:
            return NotImplemented