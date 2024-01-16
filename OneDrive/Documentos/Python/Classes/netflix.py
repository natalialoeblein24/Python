class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano inválido.")


    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme}")
        elif self.plano == "premum":
            print(f"Ver filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para o premium par ver esse filme")
        else:
            print("Plano inválido.")    
            

cliente = Cliente("Natalia", "nati@loeb", "basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

# botao de upgrade de plano
cliente.mudar_plano("basic")
print(cliente.plano)
