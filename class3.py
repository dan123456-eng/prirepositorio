# UMA CLASS SIMPLES QUALQUER

class Calc:
    def __init__(self, a, b):
        self.a =a
        self.b =b
    def soma(self):
        s = self.a + self.b
        return s
    def sub(self):
        m = self.a - self.b
        return m
    def div(self):
        d = self.a/self.b
        return d
    def mult(self):
        mu = self.a * self.b
        return mu

calculos = Calc(2,9)

print(calculos.soma())
print(calculos.sub())