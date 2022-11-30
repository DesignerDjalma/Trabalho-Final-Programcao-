
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
    id: int
    maxCarga: float
    custoKm: float
    carregamento: list

    def __init__(self) -> None:
        pass

class Cargas:
    origem: str
    destino: str
    peso: float
    distancia: float

    def __init__(self) -> None:
        pass

