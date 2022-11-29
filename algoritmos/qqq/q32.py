

from typing import Dict, List


class Carga:

    idCaminhoes: List[int] = None
    cargaMaxima: float = 0.0
    custoPorKm: float = 0.0
  
    def __init__(self, carga_maxima: float, custo_por_km: float) -> None:
        self.cargaMaxima = carga_maxima
        self.custoPorKm = custo_por_km

    def __repr__(self) -> str:
        representacao = [
            f"Caminhões Transportando: {self.idCaminhoes}",
            f"Carga Máxima: {self.cargaMaxima} Kg",
            f"Custo por Kilometro: R${self.custoPorKm:.2f}".replace('.',',')
        ]
        return f"[{' | '.join(representacao)}]\n"

    def listarCaminhoesTransportando(self) -> None:
        nome = [i for i in globals() if globals()[i] is self]
        print(f"{nome[0].capitalize()}: Caminhões Atualmente Transportando (IDs): {self.idCaminhoes}")




class Caminhao:

    idCaminhao: int = 0
    localDeOrigem: str = ""
    localDeDestino: str = ""
    distancia: float = 0.0
    peso: float = 0.0
    cargas: Dict[int, Carga] = {}

    def __init__(self, id_caminhao: int, local_de_origem: str, 
                local_de_destino: str, distancia: float, peso: float ) -> None:
        self.idCaminhao = id_caminhao
        self.localDeOrigem = local_de_origem
        self.localDeDestino = local_de_destino
        self.distancia = distancia
        self.peso = peso

    def inserirCargas(self, carga: Carga) -> None:
        if not self.cargas:
            self.cargas = {}

        if sum()
        self.cargas[f"Carga {len(self.cargas)+1}"] = carga

        if not carga.idCaminhoes:
            carga.idCaminhoes = []
            
        if self.idCaminhao not in carga.idCaminhoes:
            carga.idCaminhoes.append(self.idCaminhao)
            
    def listarCargas(self) -> None:
        print(f"CARGAS ATUAIS:\n{self.cargas}")

    def __repr__(self) -> str:
        descricao = [
            f"Caminhão ID: {self.idCaminhao}",
            f"Local de Destino: {self.localDeDestino}",
            f"Local de Origem: {self.localDeOrigem}",
            f"Distancia {self.distancia} km",
            f"Peso: {self.peso} kg"
        ]
        mostrar = ' | '.join(descricao)
        return f"\n{mostrar}"













carga1 = Carga(1000, 1.90)
carga2 = Carga(2500, 2.90)
carga3 = Carga(3000, 3.90)
carga4 = Carga(3500, 4.90)
carga5 = Carga(4000, 5.90)
carga6 = Carga(4500, 6.90)
carga7 = Carga(5000, 7.90)


caminhao1 = Caminhao(1, "Belém", "São Paulo", 4000 ,8000)
caminhao2 = Caminhao(2, "Ananindeua", "Belém", 20, 9000)
caminhao3 = Caminhao(3, "Mosqueiro", "Belém", 40, 10000)

# Adicionando Cargas no Caminhão 1
caminhao1.inserirCargas(carga1)
caminhao1.inserirCargas(carga2)
caminhao1.inserirCargas(carga3)
caminhao1.inserirCargas(carga4)
caminhao1.inserirCargas(carga5)
# Adicionando Cargas no Caminhão 2
caminhao2.inserirCargas(carga4)
caminhao2.inserirCargas(carga5)
caminhao2.inserirCargas(carga6)
# Adicionando Cargas no Caminhão 3
caminhao3.inserirCargas(carga4)
caminhao3.inserirCargas(carga7)



print(caminhao2)
caminhao2.listarCargas()
carga1.listarCaminhoesTransportando()





