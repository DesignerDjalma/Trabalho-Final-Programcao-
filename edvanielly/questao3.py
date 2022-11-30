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
    if opt == 'g':break
    if opt == 'a':addCaminhao(frota)
    if opt == 'b':addCarga(frota)
    if opt == 'c':frota.listarCaminhoes()
    if opt == 'd':frota.listarCargas()
    if opt == 'f':frota.custoTotal()
    if opt == 'e':
        frota.listarCaminhoes()
        c = int(input("Caminhão: ")) - 1
        frota.listarCargas()
        k = int(input("Carga: ")) - 1
        addCargaCam(frota.caminhoes[c], frota.cargas[k])