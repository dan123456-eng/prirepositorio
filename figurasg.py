# FIGURAS GEOMETRICAS 

class Fig:
    def __init__(self, a, b):
        self.a =a 
        self.b =b
    def tri(self):
        c = (self.b*self.a)/2
        return c
    def quad(self):
        r = self.b*self.a
        return r

res = Fig(2,1)
print(res.tri())
print(res.quad())