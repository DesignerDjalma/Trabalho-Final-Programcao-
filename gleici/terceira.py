
def criarCaminhao(novo=''):
    return Caminhao(
        input(f"{novo}Nome Caminhão: "),
        int(input(f"{novo}número do ID: ")),
        float(input(f"{novo}Carga Máxima: ")),
        float(input(f"{novo}Custo por Km: ")))

def criarCarga(novo=''):
    return Carga(
        float(input(f"{novo}Peso: ")),
        float(input(f"{novo}Distancia: ")),
        input(f"{novo}Local de Origem: "),
        input(f"{novo}Local de Destino: "))

def listaCarga():
    print("Lista de Cargas: ")
    for i in range(len(cargas)):
        print(i+1,"->", 
        "Peso:", cargas[i].peso,
        "Distancia:", cargas[i].distancia,
        "Local Origem:", cargas[i].origem,
        "Destino:", cargas[i].destino,)

def listaCaminhao():
    print("Lista de Caminhões: ")
    for i in range(len(caminhoes)):
        print(i+1,"->",
        "Nome:",caminhoes[i].nome,
        "ID:",caminhoes[i].id2,
        "Carga máxima:",caminhoes[i].carga_max,
        "Custo por Km:",caminhoes[i].custo,
        "Cargas: ",end='')
        listaCargaCaminhao(caminhoes[i].cargas)

def listaCargaCaminhao(caminhao):
    
    if caminhao:
        for i in range(len(caminhao)):
            print(f"carga [{i+1}] ",end='')
    print()

def listaCustoCaminhao(caminhao):
    custo_cargas = []
    for i in caminhao.cargas:
        valor = caminhao.custo * i.distancia/1000
        custo_cargas.append(valor)
    return sum(custo_cargas)

def listaCustoTotal():
    custo_caminhoes = []
    for i in caminhoes:
        custo_caminhoes.append(listaCustoCaminhao(i))
    return sum(custo_caminhoes)

cargas = []
caminhoes = []


class Carga:
    
    def __init__(self, peso, distancia, origem, destino) -> None:
        self.peso = peso
        self.distancia = distancia
        self.origem = origem
        self.destino = destino   


class Caminhao:
    
    def __init__(self, nome, id2, carga_max, custo) -> None:
        self.nome = nome
        self.id2 = id2
        self.carga_max = carga_max
        self.custo = custo
        self.cargas = []


while 1:
    print("\nMenu\n")
    print("1 -> Criar Caminhão")
    print("2 -> Lista Caminhões")
    print("3 -> Deletar Caminhão")
    print("4 -> Alterar Caminhão\n")
    print("5 -> Criar Carga")
    print("6 -> Lista Cargas")
    print("7 -> Deletar Carga")
    print("8 -> Alterar Carga\n")
    print("9 -> Adicionar Carga no Caminhão")
    print("10-> Lista os custos dos Caminhões")
    print("11-> Enter para Sair")
    funcao=int(input("\nEscolha: "))
    print('\n\t',end='')
    
    if funcao==11:
        break
    
    if funcao==1:
        caminhoes.append(criarCaminhao())
    
    if funcao==2:
        listaCaminhao()
    
    if funcao==3:
        print("Deletar Qual Caminhões: ")
        listaCaminhao()
        del caminhoes[int(input("Caminhão número: "))-1]
    
    if funcao==4:
        print("Modificar Qual Caminhões: ")
        listaCaminhao()
        caminhoes[int(input("Caminhão número: "))-1] = criarCaminhao("Novo Valor para ")
    
    if funcao==5:
        cargas.append(criarCarga())
    
    if funcao==6:
        listaCarga()
    
    if funcao==7:
        print("Deletar Qual Carga: ")
        listaCarga()
        del cargas[int(input("Carga número: "))-1]
    
    if funcao==8:
        print("Modificar Qual Carga: ")
        listaCarga()
        caminhoes[int(input("Caminhão número: "))-1] = criarCarga("Novo Valor para ")
    
    if funcao==9:
        print("Adicionar Qual Carga em Qual Caminhão: ")
        listaCaminhao()
        listaCarga()
        carg = int(input("Carga número: "))
        cami = int(input("Caminhão número: "))
        pesosTotais = 0
        for i in caminhoes[cami-1].cargas:
            pesosTotais += i.peso
        
        if cargas[carg-1].peso <= caminhoes[cami-1].carga_max - pesosTotais:
            caminhoes[cami-1].cargas.append(cargas[carg-1])
        else:
            print("Carga muito pesado pro caminhão!")
    
    if funcao==10:
        print("Lista o Custo dos Caminhões:")
        contador = 0
        for i in caminhoes:
            contador += 1
            print(f"Custo Caminhão {contador} ->", listaCustoCaminhao(i))
        print(f"Custo Total: {listaCustoTotal()}")


print("saindo")

