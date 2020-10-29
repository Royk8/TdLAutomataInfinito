from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


class AutomataSimbolos(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLectura = False
        self.estadoExito = False

    def leerSimbolo(self, simbolo: str):
        simbolos = Simbols()
        if not self.estadoLectura and simbolo in simbolos.getSimbolosSimples():
            if simbolo in "=*/%><":
                self.estado = "esperando ="
            elif simbolo == "+":
                self.estado = "esperando + o ="
            elif simbolo == "-":
                self.estado = "esperando - o ="
            elif simbolo == "!":
                self.estado = "!"
            elif simbolo == "|":
                self.estado = "|"
            elif simbolo == "&":
                self.estado = "&"
            elif simbolo == ",":
                self.estado = ","
            elif simbolo == ";":
                self.estado = ";"
            elif simbolo in "()":
                self.estado = "()"
            self.estadoLectura = True
            self.estadoExito = False
            self.secuencia = simbolo

        elif self.estadoLectura:
            if simbolo not in simbolos.getSimbolosSimples():
                if self.estado != "!":
                    self.estadoExito = True
                else:
                    self.estadoExito = False
                self.estadoLectura = False
            else:
                if simbolo == "=":
                    if self.estado in ["esperando =", "esperando + o =", "esperando - o =", "!"]:
                        self.secuencia += "="
                elif simbolo == "+" and self.estado == "esperando + o =":
                    self.secuencia += "+"
                elif simbolo == "-" and self.estado == "esperando - o =":
                    self.secuencia += "-"
                elif simbolo == "|" and self.estado == "|":
                    self.secuencia += "|"
                elif simbolo == "&" and self.estado == "&":
                    self.secuencia += "&"
                else:
                    self.estadoLectura = False
                    self.estadoExito = True

    def isActivo(self) -> bool:
        return super().isActivo()

    def finLectura(self) -> bool:
        return self.estadoExito

    def reiniciar(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLectura = False
        self.estadoExito = False

    def getClase(self) -> str:
        simbolos = Simbols()
        if self.secuencia in simbolos.getSeparadores():
            return "Separador"
        elif self.secuencia in simbolos.getAsignacion():
            return "Asignacion"
        elif self.secuencia in simbolos.getModificadores():
            return "Modificador"
        elif self.secuencia in simbolos.getLogicos():
            return "Operador Logico"
        elif self.secuencia in simbolos.getAritmeticos():
            return "Operador Aritmetico"
        elif self.secuencia in ["++", "--"]:
            return "Suma/Resta 1"
        elif self.secuencia in "()":
            return "Parentesis"
        elif self.secuencia == ";":
            return "Fin de linea"
        return None

    def getSecuencia(self) -> str:
        return self.secuencia