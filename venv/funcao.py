class Cliente():
    def __init___(self, nome, carro, boleto, nota_fiscal, documento, conta_corrente):
        self.nome = nome
        self.carro = carro
        self.boleto = boleto 
        self.nota_fiscal = nota_fiscal
        self.documento = documento 
        self.conta_corrente = conta_corrente
    def inferior(self):
        print("Nome" + self.nome)
        print("Carro" + str(self.carro))
        print("Boleto" + int(self.boleto))
        print("Nota fiscal" + int(self.nota_fiscal))
        print("Documento" + int(self.documento))
        print("Conta corrente" + int(self.conta_corrente))
                        
class Compras(Cliente):
 def __init___(self,nota_fiscal, documento, conta_corrente):
     self.nota_fiscal = 444444444444
     self.documento = 36428465809
     self.conta_corrente = 20390
     super().__init__(self.nota_fiscal, self.documento, self.conta_corrente)
     def inf(self):
         super(). inferior()
          
s1=Cliente("Nicolas")
s1.inferior()
        
    