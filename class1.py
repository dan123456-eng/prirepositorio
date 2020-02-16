# MANUTENÇÃO DO CARRO
class Carro:
    def __init__(self):
        self.pneu = []
        self.oleo = []
        self.fluido = []

    def trocaspneu(self,tp):#  EU POSSO TER PROPRIEDADE SO DESSA FUNÇÃO
# ESSA FYNÇÃO CONTABILIZA AS TROCAS DE PNEU.
        self.pneu.append(tp)
    def valortotal(self):
        total = 0
        for tp in self.pneu:
            total +=tp.valor
        return total
    def listap(self):
        for tp in self.pneu:
            print(tp.nome,tp.valor)
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

lisp = Carro()
p1 = Produto('pneu', 30) #dados de entrada da classe
p2 = Produto('pneu', 40)
lisp.trocaspneu(p1)
lisp.trocaspneu(p2)
print(lisp.valortotal())
print(lisp.listap())