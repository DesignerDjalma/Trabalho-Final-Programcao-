
import os

os.system("cls")


def linediv(funcao):
    def wrapper(*args, **kwargs):
        print('-'*40)       
        return funcao(*args, **kwargs)
    return wrapper


def info(funcao):
    def wrapper(*args, **kwargs):
        print("função executada: {}({}{})".format(
            funcao.__name__,
            str(list(args))[1:-1],
            ', '+', '.join([f"{k}={v}"
            for k,v in kwargs.items()])
            if kwargs else ''))
        print(f"Retornou: {funcao(*args, **kwargs)}")
        return funcao(*args, **kwargs)
    return wrapper


@linediv
@info
def funcaoGenerica(*args, **kwargs) -> None:
    """Aceita quaisquer args e kwargs."""
    return None


@linediv
@info
class Pessoa:
    def __init__(self, nome, *args, **kwargs) -> None:
        self.nome = nome

    def __repr__(self) -> str:
        return f"Um pessoa de nome {self.nome}"

    def falar(self):
        print(f"Oi, meu nome é: {self.nome}!")



funcaoGenerica('argumento 1', 'outro arg', teste=16, variavel='Pedro', lista=[15,4,32,1])

p1 = Pessoa("Megi", 24, "Brasileira")
p2 = Pessoa("Jane", especialidade="Inglês Avançado")
p3 = Pessoa("Mary", curso="Engenharia", ano=2022)