from Code.Nodo import Nodo


class AutomataLexico:

    def __init__(self):
        self.estado = ""
        self.estados = dict()
        self.funcionEstado = None

    def cambiarEstado(self,nodo:Nodo):
        self.funcionEstado(nodo)

    def estado0(self, nodo:Nodo):
        clase = nodo.clase
        if clase == "Tipo":
            self.estado = 1
            self.funcionEstado = self.estado0()
