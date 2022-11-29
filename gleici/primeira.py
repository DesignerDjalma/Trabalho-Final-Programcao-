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
