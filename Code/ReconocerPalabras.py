from Code.AutomataTipo import AutomataTipo
from Code.AutomataVariable import AutomataVariable
from Code.Nodo import Nodo


linea = "int perico = cafe + leche"

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

def reconocedor(texto):
    leidos = []
    estados = iniciarEstados()
    #for i in texto:



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

listaAutomatas = [rString, rInt, rFloat, rDouble, rFor, rWhile, rIf, rElse, aVariable]

lecturas = []

for letra in linea:
    for automata in listaAutomatas:
        if automata.isActivo():
            automata.leerSimbolo(letra)
            if automata.finLectura():
                #Trabajarle
                nodo = Nodo(automata.getClase(), automata.getSecuencia())
                lecturas.append(nodo)
                for i in listaAutomatas:
                    i.reiniciar()
                break
"""else:
    leido = None
    for rReservada in listaReservadas:
        if rReservada.isActivo():
            leido = rReservada
            break
    print("Lectura Terminada\nSe leyo: " + leido.getSecuencia())"""
print(len(lecturas))
for objeto in lecturas:
    print("[" + objeto.clase + " | " + objeto.valor + " ] ", end="")


