import random
import gc


def aleatorioInt():
    return random.randint(1000, 10000)

def aleatorioFloat():
    return round(random.random()*10000, 2)



class Textos:
    alterarPropriedade = "{} >> Informação alterado com sucesso! > {:<12} > Valor anterior: {:<11} > Valor atual: {:<13}"
    naoAdicionado = "{} >> Carga {} Não Adicionada! {}"
    adicionado = "{} >> Carga {} Adicionada! {}"
    naoHaCargas = "Não há Cargas no Caminhão."
    alterarCargaMaximoNaoPermitido = "Não é possível alterar a carga Máxima do Caminhão com cargas dentro do caminhão!"


class Carga:

    idCaminhao = "Sem Caminhão"
    localDeOrigem = "Sem Local de Origem"
    localDeDestino = "Sem Local de Destino"
    distancia = 0.0
    peso = 0.0

    def __init__(self, local_de_origem, local_de_destino, distancia, peso):
        self.localDeOrigem = local_de_origem
        self.localDeDestino = local_de_destino
        self.distancia = distancia
        self.peso = peso

    def __repr__(self):
        descricao = [f"ID do Caminhão: {self.idCaminhao}",f"Local de Destino: {self.localDeDestino}",
            f"Local de Origem: {self.localDeOrigem}",f"Distância: {self.distancia} km",f"Peso: {self.peso} kg"]
        return ' | '.join(descricao)

    @staticmethod
    def listarTodasAsCargas():
        print("Listagem de Cargas:")
        contador = 0
        for i in gc.get_objects():
            if isinstance(i, Carga):
                contador += 1
                print(f"[{contador}]: {i}")
    
class Caminhao:

    idCaminhao = 0
    cargaMaxima = 0.0
    cargaRestante = 0.0
    custoPorKm = 0.0
    cargas = f"{Textos.naoHaCargas}"

    def __init__(self, id_caminhao=0, carga_maxima=0, custo_por_km=0):
        self.idCaminhao = id_caminhao if id_caminhao != 0 else aleatorioInt()
        self.cargaMaxima = carga_maxima if carga_maxima != 0 else aleatorioFloat() 
        self.custoPorKm = custo_por_km if custo_por_km != 0 else aleatorioInt()/100
        self.cargaRestante = carga_maxima

    def __repr__(self) -> str:
        representacao = [f" {self.getProprioNome()} >> ID: {self.getId()}",
            f"Carga Máxima: {self.getCargaMaxima(1)}",f"Custo por Kilometro: {self.getCustoPorKm(1)}"]
        return f"[{' | '.join(representacao)} ]"

    @staticmethod
    def listarTodaFronta():
        print("Listagem da Frota de Caminhões:")
        contador = 0
        for i in gc.get_objects():
            if isinstance(i, Caminhao):
                contador += 1
                print(f"[{contador}]: {i}")

    def getProprioNome(self):
        return [i for i in globals() if globals()[i] is self][0]

    def calcularCargaRestante(self):
        return self.getCargaMaxima() - self.calcularPesoTotalDasCargas()

    def calcularPesoTotalDasCargas(self):
        if not isinstance(self.cargas, str):
            return sum([i.peso for i in list(self.cargas.values())])
        else:
            return 0

    def getId(self) -> int:
        return self.idCaminhao

    def getCargaMaxima(self, formatado=False):
        if formatado:
            return "{:.2f} Kg".format(self.cargaMaxima).replace('.',',')
        return self.cargaMaxima

    def getCustoPorKm(self, formatado=False):
        if formatado:
            return f"R$ {self.custoPorKm}".replace('.',',')
        return self.custoPorKm

    def mostrarInfo(self):
        print(f"{self.getProprioNome()} >> MOSTRANDO TODAS AS INFORMAÇÕES DO CAMINHÃO:")
        self.mostrarId(1)
        self.mostrarCargaMaxima(1)
        self.mostrarCustoPorKm(1)

    def mostrarId(self, sem_nome=False):
        if not sem_nome:
            print(f"{self.getProprioNome()} >> ID: {self.getId()}")
        else:
            print(f"> ID: {self.getId()}")

    def mostrarCargaMaxima(self, sem_nome=False):
        if not sem_nome:
            print(f"{self.getProprioNome()} >> Carga Máxima: {self.getCargaMaxima(1)}")
        else:
            print(f"> Carga Máxima: {self.getCargaMaxima(1)}")

    def mostrarCustoPorKm(self, sem_nome=False):
        if not sem_nome:
            print(f"{self.getProprioNome()} >> Custo Por Kilometro: {self.getCustoPorKm(1)}")
        else:
            print(f"> Custo Por Kilometro: {self.getCustoPorKm(1)}")

    def alterarId(self, novo_id):
        old = self.idCaminhao
        new = novo_id
        self.idCaminhao = novo_id
        print(Textos.alterarPropriedade.format(self.getProprioNome(), "ID", old, new))

    def alterarCargaMaxima(self, nova_carga_maxima):
        if self.cargas == f"{Textos.naoHaCargas}":
            old = f"{self.cargaMaxima:.2f} Kg"
            new = f"{nova_carga_maxima:.2f} Kg"
            self.cargaMaxima = nova_carga_maxima
            self.cargaRestante = self.calcularCargaRestante()
            print(Textos.alterarPropriedade.format(
                self.getProprioNome(), "Carga Máxima", old, new
                ).replace('.',','))
        else:
            print(Textos.alterarCargaMaximoNaoPermitido)

    def alterarCustoPorKm(self, novo_custo_por_km):
        old = f"R$ {self.custoPorKm:.2f}"
        new = f"R$ {novo_custo_por_km:.2f}"
        self.custoPorKm = novo_custo_por_km
        print(Textos.alterarPropriedade.format(
            self.getProprioNome(), "Custo Por Km", old, new
            ).replace('.',','))

    def inserirCargas(self, carga):
        nome_carga = [i for i in globals() if globals()[i] is carga][0]
        
        if not self.cargas or isinstance(self.cargas, str):
            self.cargas = {}

        if carga.idCaminhao == "Sem Caminhão":
            if carga.peso <= self.cargaRestante:
                self.cargas[f"Carga {aleatorioInt()}"] = carga
                self.cargaRestante -= carga.peso
                carga.idCaminhao = self.getId()
                print(Textos.adicionado.format(self.getProprioNome(), nome_carga, ""))
            else:
                ultrapssado = carga.peso - self.cargaRestante 
                msg = f"Essa Carga excede os limites de Carga Máxima em {ultrapssado:.2f} Kg!".replace('.',',')
                print(Textos.naoAdicionado.format(self.getProprioNome(), nome_carga, msg))
        else:
            if carga.idCaminhao == self.getId():
                msg = f"Essa Carga já está nesse Caminhão!"
                print(Textos.naoAdicionado.format(self.getProprioNome(), nome_carga, msg))
            else:
                msg = f"Essa Carga já está em algum outro Caminhão da Frota!"
                print(Textos.naoAdicionado.format(self.getProprioNome(), nome_carga, msg))
        
    def listarCargas(self):
        if not self.cargas:
            self.cargas = f"{Textos.naoHaCargas}"
        
        print(f"{self.getProprioNome()} >> LISTANDO CARGAS. Cargas Atuais:\n{self.cargas}")
            
    def removerCarga(self):
        print(f"{self.getProprioNome()} >> REMOVENDO CARGAS...")
        if not isinstance(self.cargas, str):
            lista_cargas = [k for k,_ in self.cargas.items()]
            if len(lista_cargas) == 1:
                opcoes = "Opção Única."
            else:
                opcoes = f"Opções de 1 a {len(lista_cargas)}"
            print(f"{self.getProprioNome()} >> Qual Carga deseja remover? {opcoes}.")
            print()
            for index, valor in enumerate(lista_cargas):
                print(f"[{index+1}] > {valor}")
                
            escolha = input("\nOpção: ")
            if escolha.isnumeric():
                if not int(escolha) > len(lista_cargas):
                    del self.cargas[lista_cargas[int(escolha)-1]]
                    print(f"{self.getProprioNome()} >> {lista_cargas[int(escolha)-1]} foi removida com sucesso!")
                else:
                    print(f"{self.getProprioNome()} Opção Inválida!")
            else:
                print(f"{self.getProprioNome()} Opção Inválida!")
        else:
            print(f"{Textos.naoHaCargas}")
                
    def removerTodasAsCargas(self):
        if not isinstance(self.cargas, str):
            lista_cargas = [k for k,_ in self.cargas.items()]
            print(f"{self.getProprioNome()} >> Removendo todas as {len(lista_cargas)} cargas!")
        else:
            print(f"{Textos.naoHaCargas}")

class Interface:
    def menu():
        pass

    def start(self):
        while True:
            self.menu()


    




# Criando Cargas
q1 = Carga("Belém", "Ananinde", distancia=4000, peso=2000)
q2 = Carga("Barca", "Icoaraci", distancia=2000, peso=8000)
q3 = Carga("Mojui", "Ituarana", distancia=1000, peso=1000)
q4 = Carga("Bande", "Ourilano", distancia=5500, peso=2200)


# Criando Caminhões
caminhao_A = Caminhao(1010, 25000, 45.65) # Caminhao criado manual
caminhao_B = Caminhao()                   # Caminhao criado aleatoriamente
caminhao_C = Caminhao()                   # Caminhao criado aleatoriamente
caminhao_D = Caminhao()                   # Caminhao criado aleatoriamente


# Testando Funcionalidades
caminhao_A.mostrarInfo()    # mostrando
caminhao_A.alterarId(2022)
caminhao_A.alterarCargaMaxima(9000)
caminhao_A.alterarCustoPorKm(48.5)
caminhao_A.mostrarInfo()            # mostrando denovo alterado agora
caminhao_A.inserirCargas(q1)
caminhao_A.alterarCargaMaxima(7000) # Tentando alterar Carga Maxima com cargas dentro do caminhão
caminhao_A.inserirCargas(q2)        # Muito pesado pra ser adicionado
caminhao_A.inserirCargas(q3)
caminhao_A.inserirCargas(q3)        # Tentando Adicionar Denovo

caminhao_B.inserirCargas(q1)        # Tentando colocar uma carga que ja ta num caminhao em outro
caminhao_B.inserirCargas(q4) 

# Listando Cargas
caminhao_A.listarCargas()
caminhao_B.listarCargas()

# Removendo Carga
caminhao_A.removerCarga()           # Removendo uma carga
caminhao_B.removerTodasAsCargas()   # Removendo todas de uma vez

# Listando Objetos
Caminhao.listarTodaFronta()         # lista tudo de caminhao
Carga.listarTodasAsCargas()         # lista tudo de carga


