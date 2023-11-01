class Cliente: 
    def __int__(self, nome, email, planos):
        self.nome = nome
        self.email = email
        self.listas_planos = ["basic", "premium"]
        if planos in self.listas_planos:
            self.listas_planos = planos
        else:
            print(" Plano inválido ")
        
        def mudar_de_plano(self, novo_plano):
         if novo_plano in self.listas_planos:
            self.planos = novo_plano 
         else:
             print("Plano inválido")
             
        def ver_outros_apto(self, apto, ver_outrosapto):
            if self.planos == ver_outrosapto:
                print(f'Você pode ver outros apartamento{apto}')
            elif self.planos == "premium":
                print(f'Voce pode ver outros apartamentos{apto}')
            elif self.plano == "basic" and ver_outrosapto == "premium":
                print(" Faça um upgrade para ver os outros apartamentos")
            else:
                print("Plano inválido ")
             
             
             
             
cliente = ("Nicolas", "nicolas.mleim@hotmail.com", "Basic")  
cliente.mudar_de_plano("basic")  
   