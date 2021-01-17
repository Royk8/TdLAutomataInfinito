from Code.AutomataReservada import AutomataReservada
from Code.AutomataVariable import AutomataVariable
from Code.AutomataSimbolos import AutomataSimbolos
from Code.AutomataNumeros import AutomataNumeros
from Code.AutomataReservadaTipo import AutomataReservadaTipo
from Code.AutomataReservadaBool import AutomataReservadaBool
from Code.AutomataLexico import AutomataLexico
from Code.Nodo import Nodo
from Code.ReconocerdorRecursivo import ReconocedorRecursivo


class Controller:

    def __init__(self):
        self.lecturas = []

    # Reconoce palabras en las lineas del texto
    def reconocedor(self, linea):

        # Se instancian automatas de reconocimiento de palabras reservadas y variables
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

        # Ademas de los automaras de Simbolos y numeros
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

    # Evalua los resultados del reconocedor e identifica errores lexicos basicos
    def evaluador(self):
        automataEvaluador = AutomataLexico()
        nodoError = 0
        mensaje = ''
        for i in range(len(self.lecturas)):
            automataEvaluador.funcionEstado(self.lecturas[i])
            if automataEvaluador.isFinished():
                nodoError = i
                mensaje = automataEvaluador.getMensajeError()
                break
        if automataEvaluador.quotation:
            mensaje = 'Quotation never closed'
            nodoError = len(self.lecturas)
        return nodoError, mensaje

    # Devuelve la lista de lecturas en un String
    def getLecturas(self):
        retornador = ''
        for objeto in self.lecturas:
            retornador += "[" + str(objeto.clase) + \
                " | " + str(objeto.valor) + " ] "
        retornador += ("\n")
        return retornador

#_______________________ PRACTICA 2 ________________________

    def reconocerGramatica(self, nodosTexto):
        recursivo = ReconocedorRecursivo(nodosTexto)
        recursivo.principal()
        return recursivo.codigoLeido

# Metodo para corregir pequeño problema de reconocimiento de la practica anterior
    def preprocesado(texto : str):
        texto.replace('(',' ( ')
        texto.replace('{', ' { ')
        texto.replace('}', ' } ')
        texto.replace(')', ' ) ')
        return texto