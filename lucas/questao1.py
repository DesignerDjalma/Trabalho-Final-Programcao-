def funcao():
    m = input('Tradutor de mensagem: Ex.: 2, 15, 13, 0, 4, 9, 1 = bom dia\nTraduzir mensagem: ')
    print("Mensagem Secreta: "+''.join([' abcdefghijklmnopqrstuvwxyz'[int(i)] for i in m.split(',')]))
    continuar = int(input("[1]Continuar Traduzindo?\n[0]Sair\nOpção: "))
    if continuar: return funcao()

funcao()