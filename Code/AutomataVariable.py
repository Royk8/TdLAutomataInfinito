from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


class AutomataVariable(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.estadoLectura = False
        self.estadoError = False
        self.estadoExito = False
        self.secuenciaError = ""
        self.lecturaInvalida = False

    def leerSimbolo(self, simbolo: str):
        simbolos = Simbols()
        simbolosLectura = simbolos.getAlfanumericos()
        simbolosFin = simbolos.getAritmeticos()
        simbolosFin.extend(simbolos.getAsignacion())
        simbolosFin.extend(simbolos.getLogicos())
        simbolosFin.append(" ")
        if not self.estadoError:
            if not self.estadoLectura and simbolo in simbolos.getNumericos():
                self.estadoError = True
                self.secuenciaError = simbolo
            elif simbolo in simbolosLectura:
                self.secuencia += simbolo
                self.estadoLectura = True
            elif self.estadoLectura and simbolo in simbolosFin:
                self.estadoExito = True
        else:
            self.secuenciaError += simbolo
            if simbolo != "f" and simbolo in simbolos.getAlfabeticos():
                self.lecturaInvalida = True
            elif simbolo in simbolosFin:
                self.estadoExito = True

    def getSecuencia(self) -> str:
        if self.lecturaInvalida:
            return self.secuenciaError
        return self.secuencia

    def isActivo(self) -> bool:
        return True

    def finLectura(self) -> bool:
        return self.estadoExito

    def reiniciar(self):
        self.secuencia = ""
        self.estadoLectura = False
        self.estadoError = False
        self.estadoExito = False
        self.secuenciaError = ""
        self.lecturaInvalida = False

    def getClase(self):
        if self.estadoError:
            return "Variable Invalida"
        return "Variable"

