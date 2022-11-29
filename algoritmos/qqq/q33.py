from typing import Dict, List
import gc


class Carga:

    idCaminhao: int = 0
    localDeOrigem: str = ""
    localDeDestino: str = ""
    distancia: float = 0.0
    peso: float = 0.0

    def __init__(self, local_de_origem: str, local_de_destino: str, distancia: float, peso: float ) -> None:
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
        return f"\n{mostrar}\n"

    

class Caminhao:

    idCaminhao: int = 0
    cargaMaxima: float = 0.0
    cargaRestante: float = 0.0
    custoPorKm: float = 0.0
    cargas: Dict[str, Carga] = "Não há Cargas no Caminhão."

    def __init__(self, id_caminhao: int, carga_maxima: float,
                 custo_por_km: float) -> None:
        self.idCaminhao = id_caminhao
        self.cargaMaxima = carga_maxima
        self.custoPorKm = custo_por_km
        self.__cargaRestante = carga_maxima

    def __repr__(self) -> str:
        representacao = [
            f"Caminhões ID: {self.idCaminhao}",
            f"Carga Máxima: {self.cargaMaxima} Kg",
            #f"Carga Restante: {self.__cargaRestante} Kg",
            f"Custo por Kilometro: R${self.custoPorKm:.2f}".replace('.',',')
        ]
        return f"[{' | '.join(representacao)}]\n"

    def inserirCargas(self, carga: Carga) -> None:
        nome_carga = [i for i in globals() if globals()[i] is carga][0]
        if not self.cargas or isinstance(self.cargas, str):
            self.cargas = {}
        if carga.peso <= self.__cargaRestante:
            self.cargas[f"Carga {len(self.cargas)+1}"] = carga
            self.__cargaRestante -= carga.peso
            print(f"Carga {nome_carga} adicionada com sucesso!")
        else:
            ultrapssado = carga.peso - self.__cargaRestante 
            msg = f"Essa Carga excede os limites de Carga Máxima em {ultrapssado} Kg!"
            print(f"Carga {nome_carga} Não Adicionada! {msg}") 
        carga.idCaminhao = self.idCaminhao

    def listarCargas(self) -> None:
        nome_caminhao = [i for i in globals() if globals()[i] is self][0]
        print(f"\n[ {nome_caminhao} ] Cargas Atuais:\n{self.cargas}")

    @staticmethod
    def listarTodaFronta():
        print("\nFrota de Caminhoes:")
        contador = 0
        for obj in gc.get_objects():
            if isinstance(obj, Caminhao):
                contador += 1
                print(f"[{contador}]: {obj}")



caminhao_1 = Caminhao(24, 5000, 40)
caminhao_2 = Caminhao(63, 3000, 20)

q1 = Carga("Belém","Icoaraci",4000,4000)
q2 = Carga("Belém","Ananindeua",4000,1000)
q3 = Carga("Icoaraci","Ananindeua",4000, 2000)


caminhao_1.inserirCargas(q1)
caminhao_1.inserirCargas(q2)
caminhao_1.inserirCargas(q3)

caminhao_1.listarCargas()
caminhao_2.listarCargas()

Caminhao.listarTodaFronta()


