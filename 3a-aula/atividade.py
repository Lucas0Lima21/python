# 1. Função que soma dois números
def somar(a, b):
    return a + b


# 2. Função que diminui dois números
def subtrair(a, b):
    return a - b


# 3. Função que multiplica dois números
def multiplicar(a, b):
    return a * b


# 4. Função que divide dois números
def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b


# 5. Função que soma um número indeterminado de números
def somar_varios(*numeros):
    return sum(numeros)


# 6. Classe com métodos estáticos para as operações básicas
class Calculadora:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Erro: divisao por zero!"
        return a / b


# 7. Classe com variável global e métodos de instância
class ValorFixo:
    valor = 10  # variável de classe (global dentro da classe)

    def dobra_valor(self):
        return self.valor * 2

    def triplica_valor(self):
        return self.valor * 3


# 8. Classe Aluno
class Aluno:
    def __init__(self, nome, cpf, idade, telefone, email=None, ativo=True):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.telefone = telefone
        self.email = email
        self.ativo = ativo

    def mostrar_informacoes(self):
        return (
            f"Aluno: {self.nome} - {self.cpf} com idade {self.idade}; "
            f"Contato: {self.telefone} - {self.email}; Ativo: {self.ativo}"
        )


# ======= Exemplos de uso =======

print(somar(5, 3))                #  8
print(subtrair(10, 4))            #  6
print(multiplicar(6, 7))          #  42
print(dividir(20, 4))             #  5.0
print(somar_varios(1, 2, 3, 4))   #  10

# Classe Calculadora
print(Calculadora.somar(2, 3))          # 5
print(Calculadora.dividir(10, 0))       # Erro: divisão por zero!

# Classe ValorFixo
obj = ValorFixo()
print(obj.dobra_valor())         # 20
print(obj.triplica_valor())      # 30

# Classe Aluno
aluno1 = Aluno("Lucas Lima", "123.456.789-00", 25, "(11) 99999-9999", "lul@granjafaria.com.br", True)
print(aluno1.mostrar_informacoes())
