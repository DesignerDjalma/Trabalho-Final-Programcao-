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