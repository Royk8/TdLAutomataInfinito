from Code.AutomataTipo import AutomataTipo
from Code.AutomataVariable import AutomataVariable
from Code.AutomataSimbolo import AutomataSimbolo
from Code.AutomataSimbolos import AutomataSimbolos
from Code.AutomataNumeros import AutomataNumeros
from Code.Singleton import Simbols
from Code.Nodo import Nodo




"""
Tipo
Variable
iVariable
Operadores
"""
"""automata = Automata("String")
automata.leerSimbolo('S')
print(automata.getEstados())
automata.leerSimbolo(' ')
print(automata.getEstados())
automata.leerSimbolo('S')
print(automata.getEstados())
automata.leerSimbolo('t')
print(automata.getEstados())
automata.leerSimbolo('r')
print(automata.getEstados())
automata.leerSimbolo('i')
print(automata.getEstados())
automata.leerSimbolo('n')
print(automata.getEstados())
automata.leerSimbolo('g')
print(automata.getEstados())
automata.leerSimbolo(' ')

print(automata.getEstados())"""
def iniciarEstados():
    estados = {'String': 's0',
               'int': 'i0',
               'float': 'f0',
               'double': 'd0',
               'boolean': 'b0',
               'for': 'f0',
               'if': 'i0',
               'else': 'e0',
               'while': 'w0',
               'variable': 'v0'}
    return estados


class Controller:

    def reconocedor(linea):

        simbolos = Simbols

        rString = AutomataTipo('String')
        rInt = AutomataTipo('int')
        rFloat = AutomataTipo('float')
        rDouble = AutomataTipo('double')
        rBooblean = AutomataTipo('boolean')
        rFor = AutomataTipo('for')
        rWhile = AutomataTipo('while')
        rIf = AutomataTipo('if')
        rElse = AutomataTipo('else')
        aVariable = AutomataVariable()

        #listaPalabras = [rString, rInt, rFloat, rDouble, rBooblean, rFor, rWhile, rIf, rElse, aVariable]
        listaPalabras = [rInt, aVariable]

        """cComa = AutomataSimbolo(",")
        cMasIgual = AutomataSimbolo("+=")
        cMenos = AutomataSimbolo("-")
        cIgual = AutomataSimbolo("=")
        cIgualIgual = AutomataSimbolo("==")
        cDiferente = AutomataSimbolo("!=")
        listaCaracteres = [cComa, cMasIgual, cMenos, cIgual, cIgualIgual, cDiferente]"""
        cSimbolos = AutomataSimbolos()
        numeros = AutomataNumeros()

        lecturas = []
        linea += " "
        siguiente = False
        for simbolo in linea:
            for automata in listaPalabras:
                if automata.isActivo():
                    automata.leerSimbolo(simbolo)
                    if automata.finLectura():
                        # Trabajarle
                        nodo = Nodo(automata.getClase(), automata.getSecuencia())
                        if nodo.valor != "":
                            lecturas.append(nodo)
                        for i in listaPalabras:
                            i.reiniciar()
                        break
            cSimbolos.leerSimbolo(simbolo)
            if cSimbolos.finLectura():
                nodoCaracter = Nodo(cSimbolos.getClase(), cSimbolos.getSecuencia())
                lecturas.append(nodoCaracter)
                if not cSimbolos.isReading():
                    cSimbolos.reiniciar()
            numeros.leerSimbolo(simbolo)
            if numeros.finLectura():
                nodoNumeros = Nodo(numeros.getClase(), numeros.getSecuencia())
                lecturas.append(nodoNumeros)
                numeros.reiniciar()
        print(len(lecturas))

        for objeto in lecturas:
            print("[" + str(objeto.clase) + " | " + str(objeto.valor) + " ] ", end="")