def questao1():
    print("==============================")
    print("= Tradutor de mensagem v1.0 = ")
    print("==============================")
    Condicao = True
    Letras = ' abcdefghijklmnopqrstuvwxyz'
    while Condicao > 0:
        print("Forneça a mensagem secreta:")
        print("Ex.: 1,2,3,4,1,5,7,1,9,10,11")
        Mensagem = input("-> ")
        ListaNumeros = Mensagem.split(',')
        ListaNumerosFormatados = []
        for i in ListaNumeros:
            if i:
                ListaNumerosFormatados.append(Letras[int(i.strip())])
        print(f"Mensagem Traduzida *: ", *ListaNumerosFormatados, sep='')
        Novamente=input("Traduzir mais uma mensagem? (Sim/Não): ")
        if Novamente[0].lower()=="s":
            continue
        else:
            break

def questao2():
    NossaLista = [1,2,3,4,1,5,7,1,9,10]
    print("Forneça a lista com 10 items. Ex.: [1,2,3,4,1,5,7,1,9,10]")
    NossaLista = input("lista: ")
    NossaLista2 = []
    for i in NossaLista.replace("[","").replace("]","").split(','):
        NossaLista2.append(float(i))
    def retornoDeMaiorElemento(lista):
        print("Maior elemento:", max(lista))
        pass
    def retorneSomaDeElementos(lista):
        print("Soma dos elementos:", sum(lista))
        pass
    def retorneNumeroOcorrenciaPrimeiroElementoDaLista(lista):
        PrimeiroElemento = lista[0]
        NumeroDeRepeticao = lista.count(PrimeiroElemento)
        print("Ocorrencia do primeiro elemento:", NumeroDeRepeticao)
        pass
    def retorneMediaElementos(lista):
        Comprimento=len(lista)
        Soma=sum(lista)
        Media=Soma/Comprimento
        print("Media dos elementos:", Media)
        pass
    def retorneValorMaisProximoDaMediaDosElementos(lista):
        pass
    def retorneSomaDosElementoComValorNegativo(lista):
        SomaDosElementos=0
        for item in lista:
            if item<0:
                SomaDosElementos=SomaDosElementos+item
        print("Soma dos valores negativos:", SomaDosElementos)
        pass
    for i in range(999999):
        print('1 -> Retorna o Maior Valor')
        print('2 -> Retorna Soma Dos Elementos')
        print('3 -> Retorna Numero Ocorrencias Primeiro Elemento Da Lista')
        print('4 -> Retorna Media Elementos')
        print('5 -> Retorna Soma Dos Valores Negativos')
        print('6 -> Introduzir Lista')
        print('-> Enter Para Sair')
        Funcao=input("Escolha: ")
        if Funcao =='':
            break
        if Funcao=='6':
            print("Forneça a lista com 10 items. ")
            NossaLista = input("lista: ")
            NossaLista2 = []
            for i in NossaLista.replace("[","").replace("]","").split(','):
                NossaLista2.append(float(i))
        if Funcao=='1':
            retornoDeMaiorElemento(lista=NossaLista2)
        if Funcao=='2':
            retorneSomaDeElementos(lista=NossaLista2)
        if Funcao=='3':
            retorneNumeroOcorrenciaPrimeiroElementoDaLista(lista=NossaLista2)
        if Funcao=='4':
            retorneMediaElementos(lista=NossaLista2)
        if Funcao=='5':
            retorneSomaDosElementoComValorNegativo(lista=NossaLista2)

def questao3():
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



def main():
    while True:
        print("\n\n### Trabalho Final! ###")
        print("\nEscolher Questão:")
        print("1 -> Questão 1")
        print("2 -> Questão 2")
        print("3 -> Questão 3")
        print("4 -> Sair\n")
        questao = input("-> ")
        if questao == '4':
            break
        elif questao == '3':
            questao3()
        elif questao == '2':
            questao2()
        elif questao == '1':
            questao1()
        else:
            print("Opção Invalida!")
    print("Saindo! Fim!")



main()
# Feito com muito Suor, Desespero, e Carinho
# Não garanto lembrar do que fiz mas tudo bem
# ;)