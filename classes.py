class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        else:
            print("Diminuir o canal")


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
print(controle_remoto.cor)
controle_remoto.passar_canal("+")


controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')
print(controle_remoto2.altura)
controle_remoto2.passar_canal("-")


#     caracteristicas / atributos:
#     - cor
#     - altura
#     - profundidade
#     - largura

# métodos do controle remoto:
#     - passar de canal
#     - alterar o volume
#     - abrir a netflix
#     - desligar a tv     