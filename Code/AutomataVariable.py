from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


class AutomataVariable(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.leyendo = False
        self.error = False
        self.lecturaExitosa = False

    def leerSimbolo(self, simbolo: str):
        if not self.error:
            simbolos = Simbols()
            simbolosLectura = simbolos.getAlfanumericos()
            simbolosFin = simbolos.getAritmeticos()
            simbolosFin.append(simbolos.getAsignacion())
            simbolosFin.append(" ")
            if not self.leyendo and simbolo in simbolos.getNumericos():
                self.error = True
            elif simbolo in simbolosLectura:
                self.secuencia += simbolo
                self.leyendo = True
            elif self.leyendo and simbolo in simbolosFin:
                self.lecturaExitosa = True

    def getSecuencia(self) -> str:
        return self.secuencia

    def isActivo(self) -> bool:
        return not (self.error or self.lecturaExitosa)

    def finLectura(self) -> bool:
        return self.lecturaExitosa

    def reiniciar(self):
        self.secuencia = ""
        self.leyendo = False
        self.error = False
        self.lecturaExitosa = False

    def getClase(self):
        return "Variable"

