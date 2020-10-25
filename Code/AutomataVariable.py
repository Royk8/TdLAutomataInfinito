from Code.AutomataInterface import AutomataInteface


class AutomataVariable(AutomataInteface):

    def __init__(self):
        pass

    def leerSimbolo(self, simbolo: str):
        pass

    def isActivo(self) -> bool:
        return super().isActivo()

    def finLectura(self) -> bool:
        return super().finLectura()

    def reiniciar(self):
        super().reiniciar()

