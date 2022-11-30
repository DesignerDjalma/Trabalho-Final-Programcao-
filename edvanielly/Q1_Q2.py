
# QUESTÃO 1

while True:
    opt = input('Traduzir uma mensagem screta? [Sim/Nao]\n')

    if opt.lower().startswith('n'):
        break

    msg = input("Mensagem secreta: ")
    print("\nTradução: ")

    for n in msg.split(','):
        if n == '0':
            print(" ",end="",sep="")
        else:
            print(chr(int(n)+96),end="",sep="")

    print("\n")


# QUESTÃO 2

while True:
    repetir = True
    opt = input('Fazer operações com uma lista (10 items)? [Sim/Nao]\n')

    if opt.lower().startswith('n'):
        break
    

    while True:
        msg = input("Inserir Lista (apenas números inteiros separados por vírgula): ")
        lista = msg.strip().split(',')
        if len(lista) != 10:
            print("lista Inserida Incorretamente. Tente novamente!\n")
        else:
            listaf = []
            for n in lista:
                listaf.append(int(n))
            break
    
    

    print("Funções (Escolha uma letra para exibir o resultado): ")
    print("a -> O maior valor de todos.")
    print("b -> A soma dos valores.")
    print("c -> Número de ocorrencias primeiro item.")
    print("d -> A média dos valores.")
    print("e -> soma dos items negativos.")
    print("f -> Sair")

    
    while repetir == True:
        opt2 = input("função: ")

        if opt2 == "a":
            print("\nResultado: ")
            print(max(listaf))


        if opt2 == "b":
            print("\nResultado: ")
            print(sum(listaf))


        if opt2 == "c":
            print("\nResultado: ")
            print(listaf.count(listaf[0]))


        if opt2 == "d":
            print("\nResultado: ")
            print(sum(listaf)/10)

        if opt2 == "e":
            print("\nResultado: ")
            print(sum([x for x in listaf if x < 0]))


        if opt2 == "f":
            break

        opt3 = input("Outra Função? [Sim/Nao]\n")
        if opt3.lower().startswith('n'):
            break
            repetir = False
        else:
            repetir = True


# QUESTÃO 3


class Caminhao:
    # Construtor
    def __init__(self) -> None:
        pass

    # Adiciona uma carga
    def addCarga(self, carga):
        self.carregamento.append(carga)
    
    # Remove ultima carga
    def rmCarga(self):
        if self.carregamento:
            del self.carregamento[-1]

    # Modifica A Carga Maxima Para um outro Valor
    #...implementar as outras no mesmo modelo, toda função mod vai ser igual
    def modMaxCarga(self, valor):
        self.maxCarga = valor

    def modCustKm():
        pass

    def modIdCaminhao():
        pass



class Cargas:
    # Construtor
    def __init__(self) -> None:
        pass

    # idCaminhao
    def adicionarIdCaminhao(self, idCaminhao):
        self.idCaminhao = idCaminhao

    def modOrigem(): #...implementar função mod
        pass

    def modDestino(): #...implementar função mod
        pass

    def modPeso(): #...implementar função mod
        pass

    def modDistancia(): #...implementar função mod
        pass

##

# QUESTÃO 3

def printInfoCam(cam):
    # Informacoes do Caminhao
    print(f"Id = {cam.Id}") 
    print(f"CargaMaxima = {cam.CargaMaxima}") 
    print(f"CustoPorKm = {cam.CustoPorKm}") 

def printInfoCarga(car):
    # As informacoes da Carga
    print(f"Peso = {car.Peso}")
    print(f"Distancia = {car.Distancia}")
    print(f"Origem = {car.Origem}")
    print(f"Destino = {car.Destino}")

def addCargaCam(cam, car):
    cam.carregamento.append(car)

def rmCarga(cam, car): # Remove ultima carga
    if cam.carregamento:
        del cam.carregamento[-1]

def addCarga(frota):
    print("Nova Carga:")
    kar1 = Carga()
    kar1.Peso = input("Peso: ")
    kar1.Distancia = input("Distancia: ")
    kar1.Origem = input("Origem: ")
    kar1.Destino = input("Destino: ")
    frota.cargas.append(kar1)

def addCaminhao(frota):
    print("Novo Caminhão:")
    car1 = Caminhao() # novo Filho
    car1.Id = input("Id: ")
    car1.CargaMaxima = input("CargaMaxima: ")
    car1.CustoPorKm = float(input("CustoPorKm: "))
    frota.caminhoes.append(car1)

class Carga:
    pass

class Caminhao:
    carregamento = []

class Frota:
    caminhoes = []
    cargas = []

    def listarCaminhoes(self):
        cont = 0
        if self.caminhoes:
            cont += 1
            for i in self.caminhoes:
                print("Caminhão", cont)
                printInfoCam(i)
                print()
                cont += 1
        print()
        

    def listarCargas(self):
        cont = 0
        if self.cargas:
            cont += 1
            for i in self.cargas:
                print("Carga",cont)
                printInfoCarga(i)
                print()
                cont += 1

        print()

    def listarTudo(self):
        self.listarCaminhoes()
        self.listarCargas()

    def custoTotal(self):
        total = 0
        if self.caminhoes:
            for i in self.caminhoes:
                total += i.CustoPorKm
        print("Custo Tutal: $", total)

menu = """
\n\tMENU\n
a -> Novo Caminhão
b -> Nova Carga
c -> Listar Caminhões 
d -> Listar Cargas
e -> Inserir Carga em Caminhão
f -> Calcular Os Custos Totais
g -> Sair
-> """

frota = Frota()

while True:

    opt = input(menu)
    print()

    if opt == 'g':
        break

    if opt == 'a':
        addCaminhao(frota)

    if opt == 'b':
        addCarga(frota)

    if opt == 'c':
        frota.listarCaminhoes()

    if opt == 'd':
        frota.listarCargas()

    if opt == 'f':
        frota.custoTotal()

    if opt == 'e':
        frota.listarCaminhoes()
        c = int(input("Caminhão: ")) - 1
        frota.listarCargas()
        k = int(input("Carga: ")) - 1
        addCargaCam(frota.caminhoes[c], frota.cargas[k])
   