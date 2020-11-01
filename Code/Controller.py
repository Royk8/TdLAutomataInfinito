from Code.AutomataReservada import AutomataReservada
from Code.AutomataVariable import AutomataVariable
from Code.AutomataSimbolos import AutomataSimbolos
from Code.AutomataNumeros import AutomataNumeros
from Code.AutomataReservadaTipo import AutomataReservadaTipo
from Code.AutomataReservadaBool import AutomataReservadaBool
from Code.AutomataLexico import AutomataLexico
from Code.Nodo import Nodo

class Controller:

    def __init__(self):
        self.lecturas = []

    def reconocedor(self, linea):

        rString = AutomataReservadaTipo('String')
        rInt = AutomataReservadaTipo('int')
        rFloat = AutomataReservadaTipo('float')
        rDouble = AutomataReservadaTipo('double')
        rBooblean = AutomataReservadaTipo('boolean')
        rFor = AutomataReservada('for')
        rWhile = AutomataReservada('while')
        rIf = AutomataReservada('if')
        rElse = AutomataReservada('else')
        rTrue = AutomataReservadaBool('true')
        rFalse = AutomataReservadaBool('false')
        aVariable = AutomataVariable()

        listaPalabras = [rString, rInt, rFloat, rDouble, rBooblean,
                         rFor, rWhile, rIf, rElse, rTrue, rFalse, aVariable]
        cSimbolos = AutomataSimbolos()
        numeros = AutomataNumeros()

        self.lecturas = []
        linea = linea.replace("\n", "")
        linea += " "
        for simbolo in linea:
            for automata in listaPalabras:
                automata.leerSimbolo(simbolo)
                if automata.finLectura():
                    nodo = Nodo(automata.getClase(), automata.getSecuencia())
                    if nodo.valor != "":
                        self.lecturas.append(nodo)
                    for i in listaPalabras:
                        i.reiniciar()
                    break
            cSimbolos.leerSimbolo(simbolo)
            if cSimbolos.finLectura():
                nodoCaracter = Nodo(cSimbolos.getClase(),
                                    cSimbolos.getSecuencia())
                self.lecturas.append(nodoCaracter)
                if not cSimbolos.isReading():
                    cSimbolos.reiniciar()
            numeros.leerSimbolo(simbolo)
            if numeros.finLectura():
                nodoNumeros = Nodo(numeros.getClase(), numeros.getSecuencia())
                self.lecturas.append(nodoNumeros)
                numeros.reiniciar()

    def evaluador(self):
        automataEvaluador = AutomataLexico()
        nodoError = 0
        for i in range(len(self.lecturas)):
            automataEvaluador.funcionEstado(self.lecturas[i])
            if automataEvaluador.mensajeError:
                nodoError = i
                break
        return nodoError, automataEvaluador.mensajeError

    def getLecturas(self):
        retornador = ''
        for objeto in self.lecturas:
            retornador += "[" + str(objeto.clase) + \
                " | " + str(objeto.valor) + " ] "
        retornador += ("\n")
        return retornador