inteiro = 10
decimal = 3.14
booleano = True
texto = "Python é incrível!"
nulo = None
bytes_exemplo = b"Exemplo em bytes"
bytearray_exemplo = bytearray(b"Python")

print(inteiro, type(inteiro))
print(decimal, type(decimal))
print(booleano, type(booleano))
print(texto, type(texto))
print(nulo, type(nulo))
print(bytes_exemplo, type(bytes_exemplo))
print(bytearray_exemplo, type(bytearray_exemplo))

print("\n" + "-"*50 + "\n")

numeros = [8, 3, 1, 6, 9]
print("Lista original:", numeros)
print("Tamanho:", len(numeros))
print("Ordem crescente:", sorted(numeros))
print("Ordem decrescente:", sorted(numeros, reverse=True))

print("\n" + "-"*50 + "\n")

cores = ("vermelho", "azul", "azul")
print("Tupla:", cores)
print("Primeira cor:", cores[0])
print("Quantidade de 'azul':", cores.count("azul"))
print("Índice de 'vermelho':", cores.index("vermelho"))

print("\n" + "-"*50 + "\n")

frutas = {"maçã", "banana", "maçã", "laranja", "banana"}
print("Conjunto (sem duplicados):", frutas)

print("\n" + "-"*50 + "\n")

pessoa = {
    "nome": "Lucas Lima",
    "idade": 23,
    "curso": "Sistemas de Informação"
}
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Curso:", pessoa["curso"])

print("\n" + "-"*50 + "\n")

import datetime
data_hoje = datetime.date.today()
print("Data de hoje:", data_hoje)

print("\n" + "-"*50 + "\n")

Valor1 = 5
Valor2 = 7

soma = Valor1 + Valor2

nome = "Lucas"
curso = "Python"

mensagem = f"Olá {nome}, bem-vindo ao curso de {curso}!"

print(f"Soma: {Valor1} + {Valor2} = {soma}")
print(mensagem)
