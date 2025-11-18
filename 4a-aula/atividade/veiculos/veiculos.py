from __future__ import annotations
from abc import ABC, abstractmethod


class Veiculo(ABC):

    @abstractmethod
    def mover(self) -> None:
        pass


class Carro(Veiculo):
    def mover(self) -> None:
        print("Carro: rodando no asfalto.")


class Moto(Veiculo):
    def mover(self) -> None:
        print("Moto: acelerando rápido.")


class Bicicleta(Veiculo):
    def mover(self) -> None:
        print("Bicicleta: pedalando na ciclovia.")


class Aviao(Veiculo):
    def mover(self) -> None:
        print("Avião: voando pelos céus.")


class Barco(Veiculo):
    def mover(self) -> None:
        print("Barco: navegando no mar.")
