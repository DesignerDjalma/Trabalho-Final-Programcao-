def vmpm(lista):
    valores = {valor: abs(valor - sum(lista) / len(lista)) for valor in lista}
    return min(valores, key=valores.get)

def vi(lista):
    contador = -1
    for i in range(len(lista)):
        if i == 0:
            contador += 1
        else:
            if lista[i] == lista[i-1]:
                contador += 1
    return contador

class Interface:
    def start():
        lista = []
        while True:
            print("\n\n\tMENU")
            print("Opções:\n")
            print("1  ->  Resetar lista:")
            print("2  ->  Maior Valor:",)
            print("3  ->  Ocorrências 1º Elemento:",)
            print("4  ->  Soma dos elementos:",)
            print("5  ->  Média dos elementos:",)
            print("6  ->  Elemento mais proximo da média:",)
            print("7  ->  Soma dos elementos negativos:",)
            print("8  ->  Vizinhos iguais:",)
            print("9  ->  Cancelar:")
            esc = int(input("Opção: "))
            
            if len(lista) < 1:
                print("Digite os valores da Lista:")
                lista = [float(input(f"Valor {i+1}: ")) for i in range(0,10,1)]
            if esc == 1:
                lista = []
                continue
            if esc == 2:
                print("Maior Valor:",max(lista))
            if esc == 3:
                print("Ocorrências 1º Elemento:",lista.count(lista[0]))
            if esc == 4:
                print("Soma dos elementos:",sum(lista))
            if esc == 5:
                print("Média dos elementos:",sum(lista)/10)
            if esc == 6:
                print("Elemento mais proximo da média:",vmpm(lista))
            if esc == 7:
                print("Soma dos elementos negativos:",sum([i for i in lista if i < 0]))
            if esc == 8:
                print("Vizinhos iguais:",vi(lista))
            if esc == 9:
                break
            if esc > 9:
                continue
            if esc < 1:
                continue


Interface.start()