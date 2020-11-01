from Code.AutomataReservada import AutomataReservada
from Code.AutomataVariable import AutomataVariable
from Code.AutomataSimbolo import AutomataSimbolo
from Code.AutomataSimbolos import AutomataSimbolos
from Code.AutomataNumeros import AutomataNumeros
from Code.AutomataReservadaTipo import AutomataReservadaTipo
from Code.AutomataReservadaBool import AutomataReservadaBool
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

        listaPalabras = [rString, rInt, rFloat, rDouble, rBooblean, rFor, rWhile, rIf, rElse, rTrue, rFalse, aVariable]
        cSimbolos = AutomataSimbolos()
        numeros = AutomataNumeros()

        lecturas = []
        linea = linea.replace("\n","")
        linea += " "
        for simbolo in linea:
            for automata in listaPalabras:
                automata.leerSimbolo(simbolo)
                if automata.finLectura():
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
        print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")