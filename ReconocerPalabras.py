from AutomataTipo import AutomataTipo


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

listaReservadas = [rString, rInt, rFloat, rDouble, rFor, rWhile, rIf, rElse]

lecturas = []

for letra in linea:
    for rReservada in listaReservadas:
        if rReservada.isActivo():
            rReservada.leerSimbolo(letra)
            if rReservada.finLectura():
                #Trabajarle
                lecturas.append(rReservada.secuencia)
                for autotomata in listaReservadas:
                    autotomata.reiniciar()
                break
"""else:
    leido = None
    for rReservada in listaReservadas:
        if rReservada.isActivo():
            leido = rReservada
            break
    print("Lectura Terminada\nSe leyo: " + leido.getSecuencia())"""
print(lecturas)


