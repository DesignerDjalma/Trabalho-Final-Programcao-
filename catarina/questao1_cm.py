import string

def descriptografarMensagem(mensagem:str):
    mensagem = mensagem.replace("[","").replace("]","").replace(" ","").split(",")
    chave = {str(i):v for i,v in enumerate(f" {string.ascii_lowercase}")}
    return ''.join([chave[i] for i in mensagem if i])

def criptografarMensagem(mensagem:str):
    chave = {v:i for i, v in enumerate(f" {string.ascii_lowercase}")}
    return ', '.join([str(chave[i]) for i in [i.lower() for i in mensagem] if i])

def tradutorDeMensagem():
    msgSecreta = input("Fornaça uma mensagem secreta: ")
    traduzido = descriptografarMensagem(msgSecreta)
    print(f"\nMensagem traduzida: {traduzido}")

def destradutorDeMensagem():
    msgNormal = input("Fornaça uma mensagem normal: ")
    destraduzido = criptografarMensagem(msgNormal)
    print(f"\nMensagem secreta: {destraduzido}")

class Interface:
    def start():
        while True:
            print("\n\n\tMENU")
            print("Opções:\n")
            print("1  ->  Fornecer mensagem para traduzir:")
            print("2  ->  Fornecer mensagem para tornar secreta:")
            print("3  ->  Sair")
            esc = int(input("Opção: "))
            if esc == 1:
                tradutorDeMensagem()
            if esc == 2:
                destradutorDeMensagem()
            if esc == 3:
                break

Interface.start()
