from Code.Singleton import Simbols
from Code.AutomataInterface import AutomataInteface


class AutomataTipo(AutomataInteface):

    def __init__(self, secuencia):
        self.secuencia = secuencia
        self.numeroEstados = len(secuencia) + 1
        self.estados = [False for i in range(self.numeroEstados)]
        self.estadoActual = None
        self.estadoError = False

    def getEstados(self):
        return self.estados

    def getSecuencia(self):
        return self.secuencia

    def getActual(self):
        return self.estadoActual

    def getNumeroEstados(self):
        return self.numeroEstados

    def getClase(self):
        return "Tipo"

    def isActivo(self):
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
        if not self.estadoError:
            simbolos = Simbols()
            #Si termina la palabra con un espacio
            if simbolo == " ":
                if self.estados[-2]:
                    self.estadoActual += 1
                    self.actualizar()
                    return
                else:
                    self.avError()
            #Si entra un simbolo valido
            elif simbolo.lower() in simbolos.getAlfanumericos():
                if self.estadoActual is None:
                    if self.secuencia[0] == simbolo:
                        self.estadoActual = 0
                        self.estados[self.estadoActual] = True
                    else:
                        self.avError()
                elif self.estadoActual < self.numeroEstados - 2:
                    if self.secuencia[self.estadoActual + 1] == simbolo:
                        self.estados[self.estadoActual] = False
                        self.estadoActual += 1
                        self.estados[self.estadoActual] = True
                    else:
                        self.avError()
                else:
                    self.avError()
            del simbolos
        else:
            if simbolo == ' ':
                self.estadoError = False





