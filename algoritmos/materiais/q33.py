

from typing import Dict, List


class Carga:

    idCaminhao: int = 0
    localDeOrigem: str = ""
    localDeDestino: str = ""
    distancia: float = 0.0
    peso: float = 0.0

    def __init__(self, local_de_origem: str, 
                local_de_destino: str, distancia: float, peso: float ) -> None:
        self.localDeOrigem = local_de_origem
        self.localDeDestino = local_de_destino
        self.distancia = distancia
        self.peso = peso

    def __repr__(self) -> str:
        descricao = [
            f"ID do Caminhão: {self.idCaminhao}",
            f"Local de Destino: {self.localDeDestino}",
            f"Local de Origem: {self.localDeOrigem}",
            f"Distância: {self.distancia} km",
            f"Peso: {self.peso} kg"
        ]
        mostrar = ' | '.join(descricao)
        return f"\n{mostrar}"

    


class Caminhao:

    idCaminhao: int = 0
    cargaMaxima: float = 0.0
    cargaRestante: float = 0.0
    custoPorKm: float = 0.0
    cargas: Dict[int, Carga] = "Não há Cargas no Caminhão."

    def __init__(self, id_caminhao: int, carga_maxima: float,
                 custo_por_km: float) -> None:
        self.idCaminhao = id_caminhao
        self.cargaMaxima = carga_maxima
        self.custoPorKm = custo_por_km
        self.cargaRestante = carga_maxima

    def __repr__(self) -> str:
        representacao = [
            f"Caminhões ID: {self.idCaminhao}",
            f"Carga Máxima: {self.cargaMaxima} Kg",
            f"Carga Restante: {self.cargaRestante} Kg",
            f"Custo por Kilometro: R${self.custoPorKm:.2f}".replace('.',',')
        ]
        return f"[{' | '.join(representacao)}]\n"

    def inserirCargas(self, carga: Carga) -> None:
        if not self.cargas or isinstance(self.cargas, str):
            self.cargas = {}

        if sum(self.cargas.values()) + carga.peso <= self.cargaMaxima:
            self.cargas[f"Carga {len(self.cargas)+1}"] = carga
            self.cargaRestante -= carga.peso

        carga.idCaminhao = self.idCaminhao

    def listarCargas(self) -> None:
        print(f"CARGAS ATUAIS:\n{self.cargas}")


# caminhao_1 = Caminhao(
#     id_caminhao=1,
#     carga_maxima=5000,
#     custo_por_km=19.90
#     )

# carga_1 = Carga(
#     local_de_origem="Ananindeua",
#     local_de_destino="Belém",
#     distancia=12000,
#     peso=1500)

# caminhao_1.inserirCargas(carga=carga_1)

# print(caminhao_1)
# caminhao_1.listarCargas()

caminhao = Caminhao()

caminhao(Carga("Belém","Icoaraci",4000,4000))
caminhao(Carga("Belém","Ananindeua",4000,1000))