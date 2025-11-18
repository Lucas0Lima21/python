from operacoes.matematica import (
    adicionar, subtrair, multiplicar, dividir,
    aplicar_operacao, soma_para_float
)

from instrumentos.instrumentos import (
    Violao, Guitarra, Baixo, Piano, Bateria, InstrumentoMusical
)

from veiculos.veiculos import (
    Carro, Moto, Bicicleta, Aviao, Barco, Veiculo
)


def main() -> None:

    print("\n=== Operações Matemáticas ===")
    print("Adição:", aplicar_operacao(10, 5, adicionar))
    print("Subtração:", aplicar_operacao(10, 5, subtrair))
    print("Multiplicação:", aplicar_operacao(10, 5, multiplicar))
    print("Divisão:", aplicar_operacao(10, 5, dividir))

    print("\n=== Soma para Float ===")
    print(soma_para_float(10, 3.7))

    print("\n=== Instrumentos Musicais ===")
    instrumentos: list[InstrumentoMusical] = [
        Violao(), Guitarra(), Baixo(), Piano(), Bateria(),
        Violao(), Guitarra(), Piano(), Baixo(), Bateria()
    ]
    for inst in instrumentos:
        inst.tocar()

    print("\n=== Veículos ===")
    veiculos: list[Veiculo] = [
        Carro(), Moto(), Bicicleta(), Aviao(), Barco(),
        Carro(), Moto(), Barco(), Bicicleta(), Aviao()
    ]
    for v in veiculos:
        v.mover()


if __name__ == "__main__":
    main()
