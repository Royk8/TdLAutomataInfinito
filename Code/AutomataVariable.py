from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


class AutomataVariable(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.estadoLectura = False
        self.estadoError = False
        self.estadoExito = False

    def leerSimbolo(self, simbolo: str):
        if not self.estadoError:
            simbolos = Simbols()
            simbolosLectura = simbolos.getAlfanumericos()
            simbolosFin = simbolos.getAritmeticos()
            simbolosFin.extend(simbolos.getAsignacion())
            simbolosFin.extend(simbolos.getLogicos())
            simbolosFin.append(" ")
            if not self.estadoLectura and simbolo in simbolos.getNumericos():
                self.estadoError = True
            elif simbolo in simbolosLectura:
                self.secuencia += simbolo
                self.estadoLectura = True
            elif self.estadoLectura and simbolo in simbolosFin:
                self.estadoExito = True

    def getSecuencia(self) -> str:
        return self.secuencia

    def isActivo(self) -> bool:
        return not (self.estadoError or self.estadoExito)

    def finLectura(self) -> bool:
        return self.estadoExito

    def reiniciar(self):
        self.secuencia = ""
        self.estadoLectura = False
        self.estadoError = False
        self.estadoExito = False

    def getClase(self):
        return "Variable"

