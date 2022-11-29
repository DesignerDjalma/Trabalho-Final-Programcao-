nossa_lista = [1,2,3,4,1,5,7,1,9,10]
print("Forneça a lista com 10 items.")
nossa_lista = input("lista: ")
def retornoDeMaiorElemento(lista):
    print(max(lista))
    pass
def retorneSomaDeElementos(lista):
    print(sum(lista))
    pass
def retorneNumeroOcorrenciaPrimeiroElementoDaLista(lista):
    PrimeiroElemento = lista[0]
    NumeroDeRepeticao = lista.count(PrimeiroElemento)
    print(NumeroDeRepeticao)
    pass
def retorneMediaElementos(lista):
    Comprimento=len(lista)
    Soma=sum(lista)
    Media=Soma/Comprimento
    print(Media)
    pass
def retorneValorMaisProximoDaMediaDosElementos(lista):
    pass
def retorneSomaDosElementoComValorNegativo(lista):
    SomaDosElementos=0
    for item in lista:
        if item<0:
            SomaDosElementos=SomaDosElementos+item
    print(SomaDosElementos)
    pass
print("Maior elemento:")
retornoDeMaiorElemento(lista=nossa_lista)
print("Soma dos elementos:")
retorneSomaDeElementos(lista=nossa_lista)
print("Ocorrencia do primeiro elemento:")
retorneNumeroOcorrenciaPrimeiroElementoDaLista(lista=nossa_lista)
print("Media dos elementos:")
retorneMediaElementos(lista=nossa_lista)
print("Soma dos valores negativos:")
retorneSomaDosElementoComValorNegativo(lista=nossa_lista)