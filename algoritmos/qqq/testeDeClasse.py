
# Classe Pessoa
class Pessoa:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def saudacao(self):
        print(f"Prazer, meu nome é {self.nome} e tenho {self.idade} anos.")




# Classe Aluno, que também é uma Pessoa (Herança: Ele herda tudo da classe que é passada)
class Aluno(Pessoa):

    def setUniversidade(self, universidade):
        self.universidade = universidade

    def ondeEstuda(self):
        print(f"Eu estudo na {self.universidade}!")
    





# Criando os objetos(instancias) e chamando seus métodos(funções)
print("\nPrimeira Pessoa:")

p1 = Pessoa("Maria", 20, 1.60)
p1.saudacao()


print("\nSegunda Pessoa:")

p2 = Pessoa("Kleber", 25, 1.65)
p2.saudacao()



print("\nPrimeiro Aluno:")

a1 = Aluno("João", 22, 1.70)
a1.setUniversidade("UFRA")
a1.saudacao()
a1.ondeEstuda()