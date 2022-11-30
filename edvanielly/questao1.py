
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