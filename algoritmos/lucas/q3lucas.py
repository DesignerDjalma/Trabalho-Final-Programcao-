import time

class Caminhao:
    iD = ''
    carga_maxima = 0
    custo_km = 0
    cargas = []

    def detalhes(self):
        print("\nDados do Caminhão:")
        print("ID: {}".format(self.iD))
        print("Carga máxima (kg): {}".format(self.carga_maxima))
        print("Custo por kilometro (R$): {}".format(self.custo_km))
        
        if len(self.cargas) > 0:
            print("Cargas: ")
            for i in self.cargas:
                if i.idCam == self.iD:
                    i.detalhes()

    def adicionarPropriedades(self, iD, carga_maxima, custo_km):
        self.iD = iD
        self.carga_maxima = carga_maxima
        self.custo_km = custo_km

    def modificarCargaMaxima(self, valor):
        self.carga_maxima = valor

    def modificarCustoKm(self, valor):
        self.custo_km = valor

    def modificarIdcaminhao(self, valor):
        self.iD = valor

    def removerCarga(self, carga):
        for i in self.cargas:
            if i == carga:
                self.cargas.remove(carga)

    def adicionarCarga(self, carga):
        
        def fpeso(carga):
            return carga.peso
        
        mapp = map(fpeso, self.cargas)
        lista = list(mapp)
        soma = sum(lista)
        
        if self.carga_maxima == 0:
            print("Carga máxima não atual 0.")

        else:
            if self.carga_maxima >= soma + carga.peso:
                self.cargas.append(carga)
                carga.idCam = self.iD
                print("Carga adicionada!")
            else:
                print("Carga não adicionada, limite de peso excedido.")


class Carga:
    idCam = 0
    locOri = ''
    locDes = ''
    distCar = 0
    peso = 0
    
    def detalhes(self):
        print("\nDados da Carga:")
        print("caminhao ID: {}".format(self.idCam))
        print("Origem: {}".format(self.locOri))
        print("Destino: {}".format(self.locDes))
        print("Distancia (m): {}".format(self.distCar))
        print("Peso (Kg): {}\n".format(self.peso))

    def adicionarPropriedades(self, peso, origem, destino, dist):
        self.peso = peso
        self.locOri = origem
        self.locDes = destino
        self.distCar = dist

    def modificaridCam(self, valor):
        self.idCam = valor

    def modificarlocOri(self, valor):
        self.locOri = valor

    def modificarlocDes(self, valor):
        self.locDes = valor

    def modificardistCar(self, valor):
        self.distCar = valor

    def modificarpeso(self, valor):
        self.peso = valor


nomeImpresa = "Mil Rodas"

print("\n\nBem vindo ao App da Empresa {}!".format(nomeImpresa))
print("\nPara acessar a opção digite sempre o número")
print("correspondente a ação que deseja executar.")
print("Ex.: [3] => Digite o número 3 em seguida Enter.")

camReg = []
carReg = []

# ==> Interface do Usuário <==

while True:
    print("\n\tMENU\n")
    print("[1] Registrar Caminhão a Frota.")
    print("[2] Modificar Caminhão.")
    print("[3] Registrar Carga Nova.")
    print("[4] Adicionar Carga a um Caminhão.")
    print("[5] Remover uma Carga de um caminhão.")
    print("[6] Mostrar Detalhes de um Caminhão.")
    print("[7] Sair.")
    print()

    esc = int(input("Opção: "))
    print()

    if esc == 1: # Registrar Caminhao
        print("Novo caminhão: ")
        camGene = Caminhao()
        id_esc = int(input("ID: "))
        cm_esc = float(input("Carga máxima: "))
        km_esc = float(input("Custo por Km: R$"))
        camGene.adicionarPropriedades(id_esc, cm_esc, km_esc)
        camReg.append(camGene)
        print("Caminhao adicionado a frota!\n")
    
    if esc == 2: # Modificar Caminhao
        print("Escolher Caminhão: ")
        for i in camReg:
            print("Caminhão ID", i.iD)

        esc_cam = int(input("Opção > Caminhão ID: "))
        for i in camReg:
            if i.iD == esc_cam:
                id_esc = int(input("ID: "))
                cm_esc = float(input("Carga máxima: "))
                km_esc = float(input("Custo por Km: R$"))
                i.modificarIdcaminhao(id_esc)
                i.modificarCargaMaxima(cm_esc)
                i.modificarCustoKm(km_esc)

                print()

    if esc == 3: # Registrar Carga Nova
        print("Nova Carga: ")
        carga = Carga()
        peso_esc = float(input("Peso: "))
        loc_ori = input("Local de Origem: ")
        loc_dest = input("Local de Destino: ")
        dist = float(input("Distância: "))
        carga.adicionarPropriedades(peso_esc,loc_ori,loc_dest,dist)
        carReg.append(carga)
        print("Carga Registrada.")

    if esc == 4: # Adicionar Carga a um Caminhão
        print("Escolher Caminhão: ")
        for i in camReg:
            print("Caminhão ID", i.iD)

        esc_cam = int(input("Opção > Caminhão ID: "))
        for i in camReg:
            if i.iD == esc_cam:
                cargas_disp = []
                print("\nCargas Disponíveis: ")
                for j in carReg:
                    if j.idCam == 0:
                        cargas_disp.append(j)
                
                for j2 in range(len(cargas_disp)):
                    print(f"\n\tCARGA [{j2+1}]")
                    cargas_disp[j2].detalhes()

                if len(cargas_disp) > 0:
                    carga_esc = int(input("Carga: "))
                    i.adicionarCarga(cargas_disp[carga_esc-1])
                
                if len(cargas_disp) == 0:
                    print("Não há cargas disponiveis.")

    if esc == 5: # Remover uma Carga de um caminhão.
        print("Escolher Caminhão: ")
        for i in camReg:
            print("Caminhão ID", i.iD)

        esc_cam = int(input("Opção > Caminhão ID: "))

        for i in camReg:
            if i.iD == esc_cam:
                cargas_disp = []
                print("\nCargas Disponíveis: ")
                for j in i.cargas:
                    if j.idCam == esc_cam:
                        cargas_disp.append(j)


                for j2 in range(len(cargas_disp)):
                    print(f"\n\tCARGA [{j2+1}]")
                    cargas_disp[j2].detalhes()

                if len(cargas_disp) > 0:
                    carga_esc = int(input("Carga: "))
                    i.removerCarga(cargas_disp[carga_esc-1])
                    print("Carga removida!")
                
                if len(cargas_disp) == 0:
                    print("Não há cargas disponiveis.")

    if esc == 6: # Mostrar Detalhes
        print("Escolher Caminhão: ")

        for i in camReg:
            print("Caminhão ID", i.iD)
        print("Caminhão ID * --> Mostra as informações de todos os Caminhões.")

        esc_cam = input("Opção > Caminhão ID: ")
        if esc_cam != '*':
            esc_cam = int(esc_cam)
        
        if esc_cam == '*':
            for i in camReg:
                i.detalhes()

        for i in camReg:
            if i.iD == esc_cam:
                i.detalhes()
        
    if esc == 7: # Sair
        print("Saindo do aplicativo.")
        break
    
    time.sleep(0.5)
    print('\n...\n')
    time.sleep(0.5)


