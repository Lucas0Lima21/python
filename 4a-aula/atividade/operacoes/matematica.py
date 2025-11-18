from __future__ import annotations
from typing import Callable, Union

Numero = Union[int, float]
Operacao = Callable[[int, int], int]


def adicionar(a: int, b: int) -> int:
    return a + b


def subtrair(a: int, b: int) -> int:
    return a - b


def multiplicar(a: int, b: int) -> int:
    return a * b


def dividir(a: int, b: int) -> int:
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a // b


def aplicar_operacao(a: int, b: int, operacao: Operacao) -> int:
    return operacao(a, b)


def soma_para_float(a: Numero, b: Numero) -> float:
    return float(a + b)
