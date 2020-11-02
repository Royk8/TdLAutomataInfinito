from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


class AutomataSimbolo(AutomataInteface):

    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.numeroEstados = len(secuencia) + 1
        self.estados = [False for i in range(self.numeroEstados)]
        self.estadoActual = None
        self.estadoError = False

    def leerSimbolo(self, simbolo: str):
        if not self.estadoError:
            if self.estadoActual is None:
                if simbolo == self.secuencia[0]:
                    self.estados[0] = True
                    self.estadoActual = 0
            else:
                if self.estadoActual < self.numeroEstados - 2:
                    if self.secuencia[self.estadoActual + 1] == simbolo:
                        self.estados[self.estadoActual] = False
                        self.estadoActual += 1
                        self.estados[self.estadoActual] = True
                if self.estados[-2]:
                    if self.numeroEstados < 3:
                        self.avError()
                    else:
                        self.estados[self.estadoActual] = False
                        self.estadoActual += 1
                        self.estados[self.estadoActual] = True


    def isActivo(self) -> bool:
        return not (self.estadoError or self.estados[-1])

    def finLectura(self) -> bool:
        return self.estados[-1]

    def reiniciar(self):
        if self.estadoActual is not None:
            self.estados[self.estadoActual] = False
            self.estadoActual = None
        self.estadoError = False

    def avError(self):
        if not self.estadoError:
            if self.estadoActual is not None:
                self.estados[self.estadoActual] = False
                self.estadoActual = None
            self.estadoError = True

    def getClase(self) -> str:
        simbolos = Simbols()
        if(self.secuencia in simbolos.getSeparadores()):
            return "Separador"
        elif(self.secuencia in simbolos.getAsignacion()):
            return "Asignacion"
        elif(self.secuencia in simbolos.getModificadores()):
            return "Modificador"
        elif (self.secuencia in simbolos.getLogicos()):
            return "Operador Logico"
        return None

    def getSecuencia(self) -> str:
        return self.secuencia