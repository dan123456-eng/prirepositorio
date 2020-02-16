from class1 import*

lisp = Carro()
p1 = Produto('pneu', 30) #dados de entrada da classe
p2 = Produto('pneu', 40)
lisp.trocaspneu(p1)
lisp.trocaspneu(p2)
print(lisp.valortotal())
print(lisp.listap())