

import random
import gc


def aleatorioInt() -> int:
    return random.randint(1000, 10000)

def aleatorioFloat() -> float:
    return round(random.random()*10000, 2)



class Textos:

    """Alguns textos úteis usados pelo código"""
    
    
    alterarPropriedade = "{} >> Informação alterado com sucesso! > {:<12} > Valor anterior: {:<11} > Valor atual: {:<13}"
    naoAdicionado = "{} >> Carga {} Não Adicionada! {}"
    adicionado = "{} >> Carga {} Adicionada! {}"
    naoHaCargas = "Não há Cargas no Caminhão."
    alterarCargaMaximoNaoPermitido = "Não é possível alterar a carga Máxima do Caminhão com cargas dentro do caminhão!"


class Carga:

    """Responsável pela criação de uma Carga."""


    idCaminhao = "Sem Caminhão"
    localDeOrigem: str = "Sem Local de Origem"
    localDeDestino: str = "Sem Local de Destino"
    distancia: float = 0.0
    peso: float = 0.0

    def __init__(self, local_de_origem: str="", local_de_destino: str="", distancia: float=0, peso: float=0) -> None:
        self.localDeOrigem = local_de_origem if local_de_origem != "" else "A"
        self.localDeDestino = local_de_destino if local_de_destino != "" else "B"
        self.distancia = distancia if distancia != 0 else 0
        self.peso = peso if peso != 0 else 0

    def __repr__(self) -> str:
        descricao = [
            f"ID do Caminhão: {self.idCaminhao}",
            f"Local de Destino: {self.localDeDestino}",
            f"Local de Origem: {self.localDeOrigem}",
            f"Distância: {self.distancia} km",
            f"Peso: {self.peso} kg"
        ]
        mostrar = ' | '.join(descricao)
        return f"{mostrar}"

    @staticmethod
    def listarTodasAsCargas():
        print("Listagem de Cargas:")
        contador = 0
        lista_de_instancias = []
        for i in gc.get_objects():
            if isinstance(i, Carga):
                contador += 1
                print(f"[{contador}]: {i}")
                lista_de_instancias.append(i)
        return lista_de_instancias
    


class Caminhao:

    """Responsável pela criação de um Caminhão."""

    
    __idCaminhao: int = 0
    __cargaMaxima: float = 0.0
    __cargaRestante: float = 0.0
    __custoPorKm: float = 0.0
    __cargas = f"{Textos.naoHaCargas}"

    def __init__(self, id_caminhao:int=0, carga_maxima:float=0, custo_por_km:float=0) -> None:
        self.__idCaminhao = id_caminhao if id_caminhao != 0 else aleatorioInt()
        self.__cargaMaxima = carga_maxima if carga_maxima != 0 else aleatorioFloat() 
        self.__custoPorKm = custo_por_km if custo_por_km != 0 else aleatorioFloat()
        self.__cargaRestante = carga_maxima

    def __repr__(self) -> str:
        representacao = [
            f" {self.__getProprioNome()} >> ID: {self.__getId()}",
            f"Carga Máxima: {self.__getCargaMaxima(1)}",
            f"Custo por Kilometro: {self.__getCustoPorKm(1)}"
        ]
        return f"[{' | '.join(representacao)} ]"

    @staticmethod
    def listarTodaFronta() -> None:
        print("Listagem da Frota de Caminhões:")
        contador = 0
        lista_de_instancias = []
        for i in gc.get_objects():
            if isinstance(i, Caminhao):
                contador += 1
                print(f"[{contador}]: {i}")
                lista_de_instancias.append(i)
        return lista_de_instancias

    def __getProprioNome(self):
        """Retorna o próprio nome da variável que foi instânciada."""

        return [i for i in globals() if globals()[i] is self][0]

    def __calcularCargaRestante(self) -> float:
        """Calcula a Carga Restante disponível para as Cargas no Caminho."""
        return self.__getCargaMaxima() - self.__calcularPesoTotalDasCargas()

    def __calcularPesoTotalDasCargas(self) -> float:
        """Calcula o peso total das Cargas do Caminhão."""

        if not isinstance(self.__cargas, str):
            return sum([i.peso for i in list(self.__cargas.values())])
        else:
            return 0

    def __getId(self) -> int:
        return self.__idCaminhao

    def __getCargaMaxima(self, formatado=False) -> float:
        if formatado:
            return "{:.2f} Kg".format(self.__cargaMaxima).replace('.',',')
        return self.__cargaMaxima

    def __getCustoPorKm(self, formatado=False) -> float:
        if formatado:
            return f"R$ {self.__custoPorKm:.2f}".replace('.',',')
        return self.__custoPorKm

    def mostrarInfo(self) -> None:
        """Mostra todas as informações do Caminhão ao mesmo tempo."""

        print(f"{self.__getProprioNome()} >> MOSTRANDO TODAS AS INFORMAÇÕES DO CAMINHÃO:")
        self.mostrarId(True)
        self.mostrarCargaMaxima(True)
        self.mostrarCustoPorKm(True)

    def mostrarId(self, sem_nome=False) -> None:
        """Mostra na tela o valor correspondente ao ID do Caminhão."""

        if not sem_nome:
            print(f"{self.__getProprioNome()} >> ID: {self.__getId()}")
        else:
            print(f"> ID: {self.__getId()}")

    def mostrarCargaMaxima(self, sem_nome=False) -> None:
        """Mostra na tela o valor correspondente a Carga Máxima do Caminhão."""

        if not sem_nome:
            print(f"{self.__getProprioNome()} >> Carga Máxima: {self.__getCargaMaxima(1)}")
        else:
            print(f"> Carga Máxima: {self.__getCargaMaxima(1)}")

    def mostrarCustoPorKm(self, sem_nome=False) -> None:
        """Mostra na tela o valor correspondente ao Custo por Km do Caminhão."""

        if not sem_nome:
            print(f"{self.__getProprioNome()} >> Custo Por Kilometro: {self.__getCustoPorKm(1)}")
        else:
            print(f"> Custo Por Kilometro: {self.__getCustoPorKm(1)}")

    def alterarId(self, novo_id: int) -> None:
        """Altera o ID atual para um novo valor fornecido."""

        old = self.__idCaminhao
        new = novo_id
        self.__idCaminhao = novo_id
        print(Textos.alterarPropriedade.format(self.__getProprioNome(), "ID", old, new))

    def alterarCargaMaxima(self, nova_carga_maxima: float) -> None:
        """Altera a Carga Máxima atual para um novo valor fornecido."""
        
        if self.__cargas == f"{Textos.naoHaCargas}":
            old = f"{self.__cargaMaxima:.2f} Kg"
            new = f"{nova_carga_maxima:.2f} Kg"
            self.__cargaMaxima = nova_carga_maxima
            self.__cargaRestante = self.__calcularCargaRestante()
            print(Textos.alterarPropriedade.format(self.__getProprioNome(), "Carga Máxima", old, new).replace('.',','))
        else:
            print(Textos.alterarCargaMaximoNaoPermitido)

    def alterarCustoPorKm(self, novo_custo_por_km: float) -> None:
        """Altera a Custo Por Km atual para um novo valor fornecido."""

        if novo_custo_por_km >= 0:
            old = f"R$ {self.__custoPorKm:.2f}"
            new = f"R$ {novo_custo_por_km:.2f}"
            self.__custoPorKm = novo_custo_por_km
            print(Textos.alterarPropriedade.format(self.__getProprioNome(), "Custo Por Km", old, new).replace('.',','))
        else:
            print("Valor Inválido!")

    def inserirCargas(self, carga: Carga) -> None:
        """Adiciona uma carga ao Caminhão se o mesmo puder suporta-lá."""

        nome_carga = [i for i in globals() if globals()[i] is carga][0]
        
        if not self.__cargas or isinstance(self.__cargas, str):
            self.__cargas = {}

        if carga.idCaminhao == "Sem Caminhão":
            if carga.peso <= self.__cargaRestante:
                # self.__cargas[f"Carga {len(self.__cargas)+1}"] = carga
                self.__cargas[f"Carga {aleatorioInt()}"] = carga
                self.__cargaRestante -= carga.peso
                carga.idCaminhao = self.__getId()
                print(Textos.adicionado.format(self.__getProprioNome(), nome_carga, ""))
            else:
                ultrapssado = carga.peso - self.__cargaRestante 
                msg = f"Essa Carga excede os limites de Carga Máxima em {ultrapssado:.2f} Kg!".replace('.',',')
                print(Textos.naoAdicionado.format(self.__getProprioNome(), nome_carga, msg))
        else:
            if carga.idCaminhao == self.__getId():
                msg = f"Essa Carga já está nesse Caminhão!"
                print(Textos.naoAdicionado.format(self.__getProprioNome(), nome_carga, msg))
            else:
                msg = f"Essa Carga já está em algum outro Caminhão da Frota!"
                print(Textos.naoAdicionado.format(self.__getProprioNome(), nome_carga, msg))
        
    def listarCargas(self) -> None:
        """Lista as Cargas que estão atualmente no Caminhão."""

        if not self.__cargas:
            self.__cargas = f"{Textos.naoHaCargas}"
        
        print(f"{self.__getProprioNome()} >> LISTANDO CARGAS. Cargas Atuais:\n{self.__cargas}")
            
    def removerCarga(self) -> None:
        """Remove uma Carga escolhida dentre todas do Caminhão."""

        print(f"{self.__getProprioNome()} >> REMOVENDO CARGAS...")
        if not isinstance(self.__cargas, str):
            lista_cargas = [k for k,_ in self.__cargas.items()]
            if len(lista_cargas) == 1:
                opcoes = "Opção Única."
            else:
                opcoes = f"Opções de 1 a {len(lista_cargas)}"
            print(f"{self.__getProprioNome()} >> Qual Carga deseja remover? {opcoes}.")
            print()
            for index, valor in enumerate(lista_cargas):
                print(f"[{index+1}] > {valor}")
                
            escolha = input("\nOpção: ")
            if escolha.isnumeric():
                if not int(escolha) > len(lista_cargas):
                    del self.__cargas[lista_cargas[int(escolha)-1]]
                    print(f"{self.__getProprioNome()} >> {lista_cargas[int(escolha)-1]} foi removida com sucesso!")
                else:
                    print(f"{self.__getProprioNome()} Opção Inválida!")
            else:
                print(f"{self.__getProprioNome()} Opção Inválida!")
        else:
            print(f"{Textos.naoHaCargas}")
                
    def removerTodasAsCargas(self) -> None:
        """Remove todas as Cargas de um Caminhão."""

        if not isinstance(self.__cargas, str):
            lista_cargas = [k for k,_ in self.__cargas.items()]
            print(f"{self.__getProprioNome()} >> Removendo todas as {len(lista_cargas)} cargas!")
        else:
            print(f"{Textos.naoHaCargas}")



# Criando Cargas
q1 = Carga("Belém", "Ananinde", distancia=4000, peso=aleatorioFloat())
q2 = Carga("Barca", "Icoaraci", distancia=2000, peso=aleatorioFloat())
q3 = Carga("Mojui", "Ituarana", distancia=1000, peso=aleatorioFloat())
q4 = Carga("Bande", "Ourilano", distancia=5500, peso=aleatorioFloat())


# Criando Caminhões
caminhao_A = Caminhao(1010, 25000, 45.65) # Caminhao criado manual
caminhao_B = Caminhao()                   # Caminhao criado aleatoriamente
caminhao_C = Caminhao()                   # Caminhao criado aleatoriamente
caminhao_D = Caminhao()                   # Caminhao criado aleatoriamente

caminhao_A.inserirCargas(q1)
caminhao_B.inserirCargas(q2)
caminhao_C.inserirCargas(q3)
caminhao_C.inserirCargas(q4)

# Testando Funcionalidades
# caminhao_A.mostrarInfo()    # mostrando
# caminhao_A.alterarId(2022)
# caminhao_A.alterarCargaMaxima(9000)
# caminhao_A.alterarCustoPorKm(48.5)
# caminhao_A.mostrarInfo()            # mostrando denovo alterado agora
# caminhao_A.inserirCargas(q1)
# caminhao_A.alterarCargaMaxima(7000) # Tentando alterar Carga Maxima com cargas dentro do caminhão
# caminhao_A.inserirCargas(q2)        # Muito pesado pra ser adicionado
# caminhao_A.inserirCargas(q3)
# caminhao_A.inserirCargas(q3)        # Tentando Adicionar Denovo

# caminhao_B.inserirCargas(q1)        # Tentando colocar uma carga que ja ta num caminhao em outro
# caminhao_B.inserirCargas(q4) 

# # Listando Cargas
# caminhao_A.listarCargas()
# caminhao_B.listarCargas()

# # Removendo Carga
# # caminhao_A.removerCarga()           # Removendo uma carga
# # caminhao_B.removerTodasAsCargas()   # Removendo todas de uma vez

# # Listando Objetos
# Caminhao.listarTodaFronta()         # lista tudo de caminhao
# Carga.listarTodasAsCargas()         # lista tudo de carga


# import numpy as np
# import matplotlib.pyplot as plt

# # Make a random dataset:




# height = [i.distancia for i in Carga.listarTodasAsCargas()]
# bars = [f"De {i.localDeOrigem}" for i in Carga.listarTodasAsCargas()]
# y_pos = np.arange(len(bars))

# plt.bar(y_pos, height)
# plt.xticks(y_pos, bars)

# plt.show()