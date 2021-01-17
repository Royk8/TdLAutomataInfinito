from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


# Automata que reconocer simbolos especiales
class AutomataSimbolos(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLectura = False
        self.estadoExito = False
        self.estadoSolapado = False
        self.secuenciaSolapada = ""

    def leerSimbolo(self, simbolo: str):
        simbolos = Simbols()
        if not self.estadoLectura and simbolo in simbolos.getSimbolosSimples():
            self.primerSimbolo(simbolo)
        elif self.estadoLectura:
            if simbolo not in simbolos.getSimbolosSimples():
                self.estadoExito = True
                self.estadoLectura = False
            else:
                if self.estado in '"()':
                    self.estadoSolapado = True
                    self.primerSimbolo(simbolo)
                    return

                if simbolo == "=":
                    if self.estado in ["esperando =", "esperando + o =", "esperando - o =", "!"]:
                        self.secuencia += "="
                elif simbolo == "+" and self.estado == "esperando + o =":
                    self.secuencia += "+"
                elif simbolo == "-":
                    if self.estado == "esperando - o =":
                        self.secuencia += "-"
                    if self.secuencia in ["=","+","*","/","%",",","<",">"]:
                        self.estadoSolapado = True
                        self.primerSimbolo(simbolo)
                elif simbolo == "|" and self.estado == "|":
                    self.secuencia += "|"
                elif simbolo == "&" and self.estado == "&":
                    self.secuencia += "&"
                elif simbolo in ['(', '"', '{']:
                    self.estadoSolapado = True
                    self.primerSimbolo(simbolo)
                else:
                    self.estadoLectura = False
                    self.estadoExito = True

    def primerSimbolo(self, simbolo):
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
        elif simbolo in "(":
            self.estado = "("
        elif simbolo == '{':
            self.estado = '{'
        elif simbolo in ")":
            self.estado = ")"
        elif simbolo in "}":
            self.estado = "}"
        elif simbolo == '"':
            self.estado = '"'
        self.estadoLectura = True
        self.estadoExito = False
        if self.estadoSolapado:
            self.secuencia += simbolo
        else:
            self.secuencia = simbolo

    def isActivo(self) -> bool:
        return super().isActivo()

    def finLectura(self) -> bool:
        if self.estadoSolapado:
            self.secuenciaSolapada = self.secuencia[0:-1]
            self.secuencia = self.secuencia[-1]
            return True
        return self.estadoExito

    def reiniciar(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLectura = False
        self.estadoExito = False

    def getClase(self) -> str:
        simbolos = Simbols()
        secuenciaAEntregar = self.secuencia
        if self.estadoSolapado:
            secuenciaAEntregar = self.secuenciaSolapada
        if secuenciaAEntregar in simbolos.getSeparadores():
            return "Separador"
        elif secuenciaAEntregar in simbolos.getAsignacion():
            return "Asignacion"
        elif secuenciaAEntregar in simbolos.getModificadores():
            return "Modificador"
        elif secuenciaAEntregar in simbolos.getLogicos():
            return "Operador Logico"
        elif secuenciaAEntregar in simbolos.getAritmeticos():
            return "Operador Aritmetico"
        elif secuenciaAEntregar in ['++', '--']:
            return "Suma/Resta 1"
        elif secuenciaAEntregar in '(':
            return "Abre Parentesis"
        elif secuenciaAEntregar in ')':
            return "Cierra Parentesis"
        elif secuenciaAEntregar in '{':
            return "Abre Llave"
        elif secuenciaAEntregar in '}':
            return "Cierra Llave"
        elif secuenciaAEntregar == ';':
            return "Fin de linea"
        elif secuenciaAEntregar == simbolos.getComillas():
            return "Comillas"
        return None

    def getSecuencia(self) -> str:
        if self.estadoSolapado:
            secuanciaAEntregar = self.secuenciaSolapada
            self.secuenciaSolapada = ""
            self.estadoSolapado = False
            return secuanciaAEntregar
        return self.secuencia

    def isReading(self):
        return self.estadoLectura