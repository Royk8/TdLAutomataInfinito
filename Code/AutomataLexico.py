from Code.Nodo import Nodo


class AutomataLexico:

    def cambiarEstado(self,cambio):

        def estado0(nodo:Nodo):
            clase = nodo.clase
            if clase == "Tipo":
                self.funcionEstado = self.cambiarEstado(1)
            elif clase == "Variable":
                self.funcionEstado = self.cambiarEstado(2)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(31)
            elif clase == "Reservada":
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == "Variable":
                self.funcionEstado = self.cambiarEstado(32)
            elif clase == "Variable":
                self.funcionEstado = self.cambiarEstado(33)


        def estado1(nodo:Nodo):
            clase = nodo.clase
            print("Hola, este es el estado 1 " + clase)

        def estado2(nodo: Nodo):
            clase = nodo.clase
            print("Hola, este es el estado 2" + clase)

        if cambio == 0:
            return estado0
        elif cambio == 1:
            return estado1
        elif cambio == 2:
            return estado2
        elif cambio == 3:
            return estado3
        elif cambio == 4:
            return estado4
        elif cambio == 5:
            return estado5
        elif cambio == 6:
            return estado6
        elif cambio == 7:
            return estado7
        elif cambio == 8:
            return estado8
        elif cambio == 9:
            return estado9
        elif cambio == 10:
            return estado10
        elif cambio == 11:
            return estado11
        elif cambio == 12:
            return estado12
        elif cambio == 13:
            return estado13
        elif cambio == 14:
            return estado14
        elif cambio == 15:
            return estado15
        elif cambio == 16:
            return estado16
        elif cambio == 17:
            return estado17
        elif cambio == 18:
            return estado18
        elif cambio == 19:
            return estado19
        elif cambio == 20:
            return estado20
        elif cambio == 21:
            return estado21

    def __init__(self):
        self.funcionEstado = self.cambiarEstado(0)


auto = AutomataLexico()
nodo = Nodo("Tipo","int")
auto.funcionEstado(nodo)
auto.funcionEstado(nodo)


