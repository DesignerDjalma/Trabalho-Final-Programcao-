

# retorna maior valor
import time


def a(l):
    print("maior valor.:".capitalize())
    return max(l)

# retorna a soma
def b(l):
    print("a soma.:".capitalize())
    return sum(l)

# retorna numero de ocorrencias primeiro item
def c(l):
    print("numero de ocorrencias primeiro item.:".capitalize())
    return l.count(l[0])

# retorna a media
def d(l):
    print("a media.:".capitalize())
    return sum(l)/len(l)

# retorna item mais proxima da media
def e(l):
    print("item mais proxima da media.:".capitalize())
    l2 = [d(l)]*len(l);
    l3=[abs(l2[i]-l[i]) for i in range(len(l))];
    l4 = l3[:];
    l4.sort();
    vmpz=l4[0];
    p=l3.index(vmpz);
    return l[p]

# retorna soma dos items negativos
def f(l):
    print("soma dos items negativos.:".capitalize())
    vn = [i for i in l if i < 0]
    return sum(vn)

# retorna contagem da quantidade de vizinhos iguais
def g(l):
    print("contagem da quantidade de vizinhos iguais.:".capitalize())
    cont = 0 
    for i,v in enumerate(l):
        if i==0:
            va=v
            continue
        if v==va:
            cont+=1
            va=v
        else:
            va=v
    return cont


def fs():
    print("\n\nEscolha uma função: ")
    print("[1] maior valor.".capitalize(),)
    print("[2] a soma.".capitalize(),)
    print("[3] numero de ocorrencias primeiro item.".capitalize(),)
    print("[4] a media.".capitalize(),)
    print("[5] item mais proxima da media.".capitalize(),)
    print("[6] soma dos items negativos.".capitalize(),)
    print("[7] contagem da quantidade de vizinhos iguais.".capitalize(),)
    print("[8] Sair")
    return int(input("Função número: "))

loop = 1
l = []
for i in range(10):
    l.append(int(input(f"Forneça um número para a lista (item[{i}]): ")))
print("Lista:", l)

while loop > 0:
    r = fs()
    if r == 1:
        print('\n\n')
        print(a(l))
        time.sleep(3)
    if r == 2:
        print('\n\n')
        print(b(l))
        time.sleep(3)
    if r == 3:
        print('\n\n')
        print(c(l))
        time.sleep(3)
    if r == 4:
        print('\n\n')
        print(d(l))
        time.sleep(3)
    if r == 5:
        print('\n\n')
        print(e(l))
        time.sleep(3)
    if r == 6:
        print('\n\n')
        print(f(l))
        time.sleep(3)
    if r == 7:
        print('\n\n')
        print(g(l))
        time.sleep(3)
    if r == 8:
        loop -= 1000



