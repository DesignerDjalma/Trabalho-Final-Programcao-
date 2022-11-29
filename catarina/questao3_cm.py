import datetime
import getpass
import math
import os
import time

def limpar():
    os.system('cls')

def linhasBase(_=100):
    simb = '-='
    print('\n'+simb*(math.ceil(_/len(simb)))+'\n')

def dataAtual(formato="%d/%m/%Y as %H:%M:%S"):
    return datetime.datetime.now().strftime(formato)

def num(num):
    emojis = {'0':'0️⃣','1':'1️⃣','2':'2️⃣','3':'3️⃣','4':'4️⃣','5':'5️⃣','6':'6️⃣','7':'7️⃣','8':'8️⃣','9':'9️⃣'}
    num = str(num)
    emoji_num = []
    for i in num:
        emoji_num.append(emojis[i])
    return ' ' + ' '.join(emoji_num) + '  ->'

def listarTodasAsCargas():
    variaveis = list(globals().items())
    contador = 0
    for (var, classe) in variaveis:
        if isinstance(classe, Carga):
            print(f"Carga [{var}]")
            print(f"\n\tDetalhes:")
            print(f"{classe.listarAtributos()}")
    if contador == 0:
        print("\nNão há nenhuma Carga na Frota no momento.\n")

def listarTodaosOsCaminhões():
    variaveis = list(globals().items())
    contador = 0
    for (var, classe) in variaveis:
        if isinstance(classe, Caminhão):
            contador += 1
            print(f"\nCaminhão [{var}]")
            print(f"\n\tDetalhes:")
            print(f"{classe.listarAtributos()}")
    if contador == 0:
        print("\nNão há nenhum Caminhão na Frota no momento.\n")

def mostrarOpcoes(opcoes):
    for i, opc in enumerate(opcoes):
        print(f"{num(i+1)} {opc}")
    linhasBase()


class Frota:
    caminhoes = []
    cargas = []


class Empresa:
    nome = "MilRodas™"


class Carga:
    idCaminhao = None

    def __init__(self, local_de_origem="Sem Local de Origem", local_de_destino="Sem Local de Destino", distancia=0.0, peso=0.0):
        self.local_de_origem = local_de_origem
        self.local_de_destino = local_de_destino
        self.distancia = distancia
        self.peso = peso

    def listarAtributos(self):
        print(f"id do Caminhão: {self.idCaminhao}.")
        print(f"Local de origem: {self.local_de_origem}.")
        print(f"Local de destino: {self.local_de_destino}.")
        print(f"Distância: {self.distancia:.2f} metros")
        print(f"Peso: {self.peso:.2f} Kilogramas.")
        return ''
    

class Caminhão:
    iD = ''
    carga_maxima = 0
    custo_km = 0
    cargas = []

    def __init__(self, iD=None, carga_maxima=0.0, custo_km=0.0):
        self.iD = iD
        self.carga_maxima = carga_maxima
        self.custo_km = custo_km

    def listarAtributos(self):
        print(f"ID: {self.iD}.")
        print(f"Carga Máxima: {self.carga_maxima} Kilogramas.")
        print(f"Custo por kilometro: R$ {self.custo_km}.")


class Interface:

    def __init__(self):
        self.frota = Frota()

    def linhas(self, *args):
        if args: linhasBase(_=args[0])
        else: linhasBase()

    def retorne(self):
        return input("  Número: ")

    def start(self):
        self.cabecalho()
        texto_entrada = f"Seja Bem Vindo(a) {getpass.getuser()}!"
        print("\n{:^100}\n\n{:^100}".format(
            texto_entrada, "Acessando em: " + dataAtual()
            ))
        self.linhas()
        time.sleep(2)
        self.menuPrincipal()

    def cabecalho(self, titulo=''):
        limpar()
        self.linhas()
        cabeca = f"{Empresa.nome} Management System"
        print("{:^100}".format(cabeca))
        self.linhas()
        if titulo: print("{:^100}".format(f"{titulo}\n".upper()))

    def opcaoInvalida(self):
        self.cabecalho()
        print("\n\tOpção Inválida!\n")
        self.linhas()
        time.sleep(2)
        self.voltarMenuPrincipal()

    def opcoesPadraoMP(self):
        self.cabecalho("Menu Principal")

        mostrarOpcoes([
            "Gerenciar Frota de Caminhões",
            "Gerenciar Cargas",
            "Sair",
            ])
        return self.retorne()
    
    def opcoesPadraoGF(self):
        self.cabecalho("Gerenciar Frota")

        mostrarOpcoes([
            "Adicionar novo Caminhão a Frota de Caminhões",
            "Modificar um Caminhão já existente",
            "Atribuir uma Carga a um Caminhão",
            "Listar toda a Frota de Caminhões",
            "Deletar Caminhão",
            "Lista Custo Total de Operação",
            "Voltar ao Menu Anterior",
            ])
        return self.retorne()

    def opcoesPadraoGC(self):
        self.cabecalho("Gerenciar Cargas")

        mostrarOpcoes([
            "Criar uma nova Carga",
            "Deletar uma Carga já existente",
            "Listar Cargas",
            "Voltar ao Menu Anterior",
        ])
        return self.retorne()

    def opcoesPadraoModNow(self, tipo="Caminhão"):
        print(f"\n{tipo} Adicionado com Sucesso.\n")
        print("\nDeseja Modificá-lo agora?\n")
        mostrarOpcoes([
            "Sim",
            "Não",
        ])
        return self.retorne()

    def opcoesPadraoModCam(self):
        print("Qual atributo modificar?\n")
        mostrarOpcoes([
            "ID",
            "Carga máxima",
            "Custo por Km",
            "Todos",
            "Voltar ao Menu Anterior",
            ])
        return self.retorne()

    def opcoesPadraoListar(self):
        mostrarOpcoes([
            "Voltar ao Menu Anterior"
            ])
        return self.retorne()

    def menuPrincipal(self):
        opção = self.opcoesPadraoMP()
        if opção == '0':
            self.sair()

        elif opção == '1': self.menuGerenciarFrota()
        elif opção == '2': self.menuGerenciarCargas()
        elif opção == '3': self.sair()

        else:
            self.opcaoInvalida()
        
    def menuGerenciarFrota(self):
        opção = self.opcoesPadraoGF()
        if opção == '0':
            self.menuPrincipal()

        elif opção == '1': self.novoCaminhao()
        elif opção == '2': self.modificarCaminhao()
        elif opção == '3': self.atribuirCarga()
        elif opção == '4': self.listarFrota()
        elif opção == '5': self.deletarCaminhao()
        elif opção == '6': self.custosCaminhao()
        elif opção == '7': self.menuPrincipal()

        else:
            self.opcaoInvalida()

    def menuGerenciarCargas(self):
        opção = self.opcoesPadraoGC()
        if opção == '0':
            self.menuPrincipal()
        
        elif opção == '1': self.novaCarga()
        # elif opção == '2': self.modificarCarga()
        elif opção == '2': self.deletarCarga()
        elif opção == '3': self.listarCargas()
        elif opção == '4': self.menuPrincipal()

        else:
            self.opcaoInvalida()

    def novoCaminhao(self):
        self.cabecalho("Gerenciar Frota")
        novo_caminhao = Caminhão()
        self.frota.caminhoes.append(novo_caminhao)

        opção = self.opcoesPadraoModNow()
        if opção == '0':
            self.menuGerenciarFrota()

        elif opção == '1': self.modificarCaminhao(True)
        elif opção == '2': self.menuGerenciarFrota()

        else:
            self.opcaoInvalida()

    def escolherCaminhao(self, show=False):
        if not show:
            return self.retorne()

        for i, valor in enumerate(self.frota.caminhoes):
            print(f"Caminha {i+1}: {valor}")

        return self.retorne()

    def informacoesAlteradas(self):
        print("\nInformações Alteradas com Sucesso!")
        self.linhas()
        time.sleep(2)
        self.menuGerenciarFrota()

    def modificarCaminhao(self, modificar_ultimo=False):
        if modificar_ultimo:
            caminhao = self.frota.caminhoes[-1]

        else:
            self.listarFrota(modo=2)
            index_caminhao = int(self.escolherCaminhao()) -1
            caminhao = self.frota.caminhoes[index_caminhao]

        self.cabecalho("Modificar Caminhão")
        opção = self.opcoesPadraoModCam()

        if opção == '0':
            self.menuGerenciarFrota()
        
        # De um por um
        elif opção == '1': caminhao.iD = int(input(f"iD: Valor antigo: {caminhao.iD} >> Novo Valor: ")); self.informacoesAlteradas()
        elif opção == '2': caminhao.carga_maxima = float(input(f"Carga Máxima: Valor antigo: {caminhao.carga_maxima} >> Novo Valor: ")); self.informacoesAlteradas()
        elif opção == '3': caminhao.custo_km = float(input(f"Custo por Km: Valor antigo: R$ {caminhao.custo_km} >> Novo Valor: R$ ")); self.informacoesAlteradas()
        
        # Tudo 
        elif opção == '4': 
            caminhao.iD = int(input(f"iD: Valor antigo: {caminhao.iD} >> Novo Valor: "))
            caminhao.carga_maxima = float(input(f"Carga Máxima: Valor antigo: {caminhao.carga_maxima} >> Novo Valor: "))
            caminhao.custo_km = float(input(f"Custo por Km: Valor antigo: R$ {caminhao.custo_km} >> Novo Valor: R$ "))
            self.informacoesAlteradas()
        
        elif opção == '5': self.menuGerenciarFrota()
        
        else:
            self.opcaoInvalida()

    def atribuirCarga(self):
        self.cabecalho("Atribuir carga")

        if not self.frota.caminhoes:
            print("Não há caminhões disponíveis.")
            time.sleep(2)
            self.menuGerenciarFrota()

        if not self.frota.cargas:
            print("Não há cargas disponíveis.")
            time.sleep(2)
            self.menuGerenciarFrota()

        if self.frota.caminhoes:
            print("Escolher o caminhão.")
            self.listarFrota(2)
            escolha_caminhao = self.retorne()

        if self.frota.cargas:
            print("Escolher carga.")
            self.listarCargas(2)
            escolha_carga = self.retorne()

        carga_escolhida = self.frota.cargas[int(escolha_carga)-1]
        caminhao_escolhido = self.frota.caminhoes[int(escolha_caminhao)-1]

        carga_escolhida.idCaminhao = caminhao_escolhido.iD
        caminhao_escolhido.cargas.append(carga_escolhida)

        print("Carga atribuida com sucesso! (Pressione Enter Para Continuar...)")
        self.retorne()
        self.menuGerenciarFrota()

    def deletarCaminhao(self):
        self.cabecalho("Deletar um Caminhao")
        for i, cam in enumerate(self.frota.caminhoes):
            print(f"Caminhão{num(i+1)}: ID: {cam.iD} | Carga Máxima: {cam.carga_maxima:.0f} | Custo por Km: R$ {cam.custo_km:.2f}")
        
        if self.frota.caminhoes:
            self.linhas()
            print("Qual Caminhão excluir?\n")
            escolha = self.retorne()
            del self.frota.caminhoes[int(escolha)-1]
            print("Caminhão Excluido com Sucesso!")
            time.sleep(2)
            self.menuGerenciarFrota()
        else:
            print("Sem Caminhoes Disponíveis\n")
            time.sleep(2)
            self.menuGerenciarFrota()
        
    def custosCaminhao(self):
        self.cabecalho("Listagem dos Custos")
        custo_total = 0
        for i, cam in enumerate(self.frota.caminhoes):
            custo_individual = 0
            print(f"Caminhão{num(i+1)}: ID: {cam.iD} | Carga Máxima: {cam.carga_maxima:.0f} | Custo por Km: R$ {cam.custo_km:.2f} | Cargas: {len(cam.cargas)}")
            for car in cam.cargas:
                custo_individual += cam.custo_km * car.distancia/1000
            print(f"Custo Individual: {custo_individual}")
            custo_total += custo_individual
        print(f"Custo Total: {custo_total}")
        self.linhas()
        opção = self.opcoesPadraoListar()
        if   opção == '0': self.menuGerenciarFrota()
        elif opção == '1': self.menuGerenciarFrota()
        else: self.opcaoInvalida()
        pass


    def listarFrota(self, modo=1):
        self.cabecalho("Listagem da Frota")
        for i, cam in enumerate(self.frota.caminhoes):
            print(f"Caminhão{num(i+1)}: ID: {cam.iD} | Carga Máxima: {cam.carga_maxima:.0f} | Custo por Km: R$ {cam.custo_km:.2f} | Cargas: {len(cam.cargas)}")
        self.linhas()
        
        if modo == 1:
            opção = self.opcoesPadraoListar()
            if   opção == '0': self.menuGerenciarFrota()
            elif opção == '1': self.menuGerenciarFrota()
            else: self.opcaoInvalida()
        if modo == 2:
            pass
            
    def listarCargas(self, modo=1):
        self.cabecalho("Listagem das Cargas")
        for i, car in enumerate(self.frota.cargas):
            print(f"Carga{num(i+1)}: ID do Caminhão: {car.idCaminhao} | Local de Origem: {car.local_de_origem} | Local de Destino: {car.local_de_destino} | Distancia: {car.distancia} | Peso: {car.peso} ")
        self.linhas()
        
        if modo == 1:
            opção = self.opcoesPadraoListar()
            if   opção == '0': self.menuGerenciarCargas()
            elif opção == '1': self.menuGerenciarCargas()
            else: self.opcaoInvalida()
        if modo == 2:
            pass

    def novaCarga(self):
        self.cabecalho("Nova Carga")
        print("Informe os dados da carga:")
        nova_carga = Carga()
        local_de_origem = input("Local de Origem: ")
        local_de_destino = input("Local de Destino: ")
        distancia = float(input("Distância: "))
        peso = input("Peso: ")
        nova_carga.local_de_origem = local_de_origem
        nova_carga.local_de_destino = local_de_destino
        nova_carga.distancia = distancia
        nova_carga.peso = peso

        self.frota.cargas.append(nova_carga)

        print("\nCarga Adicionada com Sucesso.")
        self.linhas()
        time.sleep(2)
        self.menuGerenciarCargas()

    def modificarCarga(self):
        pass

    def deletarCarga(self):
        self.cabecalho("Deletar uma Carga")
        self.listarCargas(2)
        if self.frota.cargas:
            print("Qual carga desejas excluir?")
            escolha = self.retorne()
            del self.frota.cargas[int(escolha)-1]
            print("Carga excluida com sucesso!")
            time.sleep(2)
            self.menuGerenciarCargas()


        else:
            print("Não há cargas disponiveis.")
            time.sleep(2)
            self.menuGerenciarCargas()

    def voltarMenuPrincipal(self):
        self.menuPrincipal()

    def confirmar(self):
        self.cabecalho("Confirmação Necessária")
        print("{:^100}".format("Você tem certeza, que deseja Sair?"))
        mostrarOpcoes([
            "Sim",
            "Não, Cancelar",
        ])
        return self.retorne()

    def sair(self):
        opção = self.confirmar()
        if   opção == '0': self.menuPrincipal()
        elif opção == '1':
            self.cabecalho("Saindo...")
            print("{:^100}".format('Obrigado Por usar o Aplicativo!'))
            print("{:^100}".format(f'A {Empresa.nome} agradece!'))
            print("{:^100}".format('Brasil: Rumo Ao Hexa!'))
            self.linhas()
        elif opção == '2': self.menuPrincipal()
        else: self.opcaoInvalida()


interface = Interface()
interface.start()
