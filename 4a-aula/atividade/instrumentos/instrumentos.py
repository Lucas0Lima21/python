from __future__ import annotations
from abc import ABC, abstractmethod


class InstrumentoMusical(ABC):

    @abstractmethod
    def tocar(self) -> None:
        pass


class Violao(InstrumentoMusical):
    def tocar(self) -> None:
        print("Violão: acordes acústicos.")


class Guitarra(InstrumentoMusical):
    def tocar(self) -> None:
        print("Guitarra: solo distorcido.")


class Baixo(InstrumentoMusical):
    def tocar(self) -> None:
        print("Baixo: grave marcante.")


class Piano(InstrumentoMusical):
    def tocar(self) -> None:
        print("Piano: melodia clássica.")


class Bateria(InstrumentoMusical):
    def tocar(self) -> None:
        print("Bateria: ritmo explosivo.")
