x = float(input("Informe o primeiro valor numérico: "))
y = float(input("Informe o segundo valor numérico: "))

if x > y:
    print(f"Valor {x} é maior que valor {y}")
elif x < y:
    print(f"Valor {x} é menor que valor {y}")
else:
    print(f"Os valores de {x} e {y} são iguais")

print("\n" + "-"*50 + "\n")

texto1 = input("Informe o primeiro texto: ")
texto2 = input("Informe o segundo texto: ")

if texto1 == texto2:
    print("Os valores informados são iguais")
else:
    print(f"Valor '{texto1}' é diferente do valor '{texto2}'")

print("\n" + "-"*50 + "\n")

idade = int(input("Informe sua idade: "))

if idade < 18:
    print("Você é menor de idade.")
elif idade < 60:
    print("Você é adulto.")
else:
    print("Você é idoso.")

print("\n" + "-"*50 + "\n")

print("Loop for de 1 a 10:")
for i in range(1, 11):
    print(i, end=" ")

print("\n" + "-"*50 + "\n")

print("Loop while de 1 a 10:")
contador = 1
while contador <= 10:
    print(contador, end=" ")
    contador += 1

print("\n" + "-"*50 + "\n")

dados = {'a': 'primeiro', 'b': 'segundo', 'c': 'terceiro', 'd': 'quarto', 'e': 'quinto'}

print("Dicionário com índice, chave e valor:")
for indice, (chave, valor) in enumerate(dados.items()):
    print(f"Índice: {indice} | Chave: {chave} | Valor: {valor}")

print("\n" + "-"*50 + "\n")

lista = [9, 25, 5, 6, 5815, 985, 1, 22, 2, 7, 3]
valores_desejados = [1, 2, 5, 6]

print("Valores 1, 2, 5 e 6 da lista:")
for valor in lista:
    if valor in valores_desejados:
        print(valor, end=" ")
