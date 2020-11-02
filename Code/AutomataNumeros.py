from Code.AutomataInterface import AutomataInteface
from Code.Singleton import Simbols


# Automata que identifica la integridad de las cadenas de numeros
class AutomataNumeros(AutomataInteface):

    def __init__(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLeyendo = False
        self.estadoEnteroValido = False
        self.estadoFloatValido = False
        self.estadoDoubleValido = False
        self.estadoError = False
        self.estadoExito = False

    def leerSimbolo(self, simbolo: str):
        simbolos = Simbols()
        if not self.estadoLeyendo:
            if simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                self.estadoError = False
            elif simbolo in simbolos.getAlfabeticos():
                self.estadoError = True
            if not self.estadoError:
                if simbolo == "0":
                    self.estado = "0"
                    self.secuencia = "0"
                    self.estadoEnteroValido = True
                    self.estadoLeyendo = True
                elif simbolo in simbolos.getNumericos():
                    self.estado = "entero"
                    self.secuencia = simbolo
                    self.estadoEnteroValido = True
                    self.estadoLeyendo = True
                elif simbolo == ".":
                    self.estado = "punto solo"
                    self.secuencia = simbolo
                    self.estadoLeyendo = True

        else:
            if self.estado == "0":
                if simbolo == "0":
                    pass
                elif simbolo in simbolos.getNumericos():
                    self.estado = "entero"
                    self.secuencia = simbolo
                    self.estadoEnteroValido = True
                elif simbolo == ".":
                    self.estado = "0."
                    self.secuencia = "0."
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = True
                elif simbolo == "f":
                    self.estado = "floatConfirmado"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estado = "entero"
                    self.self.estadoEnteroValido = True
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "entero":
                if simbolo in simbolos.getNumericos():
                    self.secuencia += simbolo
                elif simbolo == ".":
                    self.estado = "entero y ."
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = True
                    self.secuencia += "."
                elif simbolo == "f":
                    self.estado = "floatConfirmado"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoEnteroValido = True
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "punto solo":
                if simbolo == "0":
                    self.estado = "0.0"
                    self.secuencia = "0.0"
                    self.estadoDoubleValido = True
                elif simbolo in simbolos.getNumericos():
                    self.estado = "decimal"
                    self.estadoDoubleValido = True
                else:
                    self.reiniciar()
            elif self.estado == "0.":
                if simbolo == "0":
                    self.estado = "0.0"
                    self.secuencia = "0.0"
                    self.estadoDoubleValido = True
                elif simbolo in simbolos.getNumericos():
                    self.estado = "decimal"
                    self.secuencia += simbolo
                    self.estadoDoubleValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.secuencia = "0.0"
                    self.estadoDoubleValido = True
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "entero y .":
                if simbolo == "0":
                    self.secuencia += "0"
                    self.estado = "entero .0"
                elif simbolo in simbolos.getNumericos():
                    self.secuencia += simbolo
                    self.estado = "decimal"
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.secuencia += "0"
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "0.0":
                if simbolo == "0":
                    self.secuencia += simbolo
                elif simbolo in simbolos.getNumericos():
                    self.estado = "decimal"
                    self.secuencia += simbolo
                elif simbolo == "f":
                    self.estado = "float .0"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "decimal":
                if simbolo == "0":
                    self.secuencia += simbolo
                    self.estado == "decimal y 0"
                elif simbolo in simbolos.getNumericos():
                    self.secuencia += simbolo
                elif simbolo == "f":
                    self.estado = "floatConfirmado"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "entero .0":
                if simbolo == "0":
                    self.secuencia += "0"
                elif simbolo in simbolos.getNumericos():
                    self.secuencia += simbolo
                    self.estado = "decimal"
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoLeyendo = False
                    self.estadoExito = True
                elif simbolo == "f":
                    self.estado = "float .0"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                else:
                    self.reiniciar()
            elif self.estado == "decimal y 0":
                if simbolo == "0":
                    self.secuencia += simbolo
                elif simbolo in simbolos.getNumericos():
                    self.secuencia += simbolo
                    self.estado == "decimal"
                elif simbolo == "f":
                    self.estado = "float .0"
                    self.estadoEnteroValido = False
                    self.estadoDoubleValido = False
                    self.estadoFloatValido = True
                elif simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()
            elif self.estado == "floatConfirmado" or self.estado == "float .0":
                if simbolo == " " or simbolo in simbolos.getSimbolosSimples():
                    self.estadoLeyendo = False
                    self.estadoExito = True
                else:
                    self.reiniciar()

    def isActivo(self) -> bool:
        return not self.estadoError

    def finLectura(self) -> bool:
        return self.estadoExito

    def avError(self):
        pass

    def reiniciar(self):
        self.secuencia = ""
        self.estado = ""
        self.estadoLeyendo = False
        self.estadoEnteroValido = False
        self.estadoFloatValido = False
        self.estadoDoubleValido = False
        self.estadoError = False
        self.estadoExito = False

    def getClase(self) -> str:
        if self.estadoEnteroValido:
            return "int"
        if self.estadoDoubleValido:
            return "double"
        if self.estadoFloatValido:
            return "float"

    def getSecuencia(self) -> str:
        if self.estado in ["decimal y 0", "0.0", "entero .0"]:
            return self.borrarCeros(self.secuencia)
        elif self.estado == "float .0":
            return str(self.borrarCeros(self.secuencia)) + "f"
        elif self.estado == "floatConfirmado":
            return self.secuencia + "f"
        else:
            return self.secuencia

    def borrarCeros(self, secuencia):
        borrar = 0
        for i in range(1, len(secuencia)):
            if secuencia[-i] == "0" and secuencia[-(i + 1)] != ".":
                borrar += 1
            else:
                break
        if borrar == 0:
            return secuencia
        return secuencia[0:-borrar]