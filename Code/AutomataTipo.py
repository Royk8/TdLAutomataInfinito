from Singleton import Simbols
from Code.AutomataInterface import AutomataInteface


class AutomataTipo(AutomataInteface):

    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.numeroEstados = len(secuencia) + 1
        self.estados = [False for i in range(self.numeroEstados)]
        self.actual = None
        self.error = False

    def getEstados(self):
        return self.estados

    def getSecuencia(self):
        return self.secuencia

    def getActual(self):
        return self.actual

    def getNumeroEstados(self):
        return self.numeroEstados

    def isActivo(self):
        return not (self.error and self.estados[-1])

    def finLectura(self) -> bool:
        return self.estados[-1]

    def reiniciar(self):
        if self.actual is not None:
            self.estados[self.actual] = False
            self.actual = None
        self.error = False

    def avError(self):
        if not self.error:
            self.estados[self.actual] = False
            self.actual = None
            self.error = True

    def actualizar(self):
        if self.estados[-1]:
            self.avError()
            return
        for i in range(self.numeroEstados):
            if self.estados[i]:
                self.estados[i+1] = True
                self.estados[i] = False
                break

    def leerSimbolo(self, simbolo: str):
        if not self.error:
            simbolos = Simbols()
            #Si termina la palabra con un espacio
            if simbolo == " ":
                if self.estados[-2]:
                    self.actual += 1
                    self.actualizar()
                    return
                if self.error:
                    self.error = False
                    self.actual = None
            #Si entra un simbolo valido
            elif simbolo.lower() in simbolos.getSimbolos('alfanumericos'):
                if self.actual is None:
                    if self.secuencia[0] == simbolo:
                        self.actual = 0
                        self.estados[self.actual] = True
                elif self.actual <= self.numeroEstados - 2:
                    if self.secuencia[self.actual + 1] == simbolo:
                        self.estados[self.actual] = False
                        self.actual += 1
                        self.estados[self.actual] = True
                else:
                    #Sino, error.
                    self.avError()
        else:
            if simbolo == ' ':
                self.error = False





