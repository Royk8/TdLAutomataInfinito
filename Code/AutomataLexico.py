from Code.Nodo import Nodo


class AutomataLexico:

    def cambiarEstado(self, cambio):

        # Estado inicial, cuando comienza la linea.
        def estado0(nodo:Nodo):
            clase = nodo.clase
            if clase == "Tipo":
                self.funcionEstado = self.cambiarEstado(1)
            elif clase == "Variable":
                self.funcionEstado = self.cambiarEstado(2)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(31)
            elif clase == "Condicion":
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Separador','Asignacion','Modificador',"Operador Logico",
                           "Operador Aritmetico","Suma/Resta 1",'Abre Parentesis','Cierra Parentesis',"Comillas"]:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase == "Fin de linea":
                self.funcionEstado = self.cambiarEstado(33)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para cuando entra un Tipo de variable Ej: String; int; boolean;
        def estado1(nodo:Nodo):
            clase = nodo.clase
            if clase in ['Tipo','int', 'double', 'float', 'boolean', 'String', 'Separador', 'Asignacion',
                         'Modificador', 'Operador Logico', 'Operador Aritmetico', 'Suma/Resta 1',
                         'Abre Parentesis', 'Cierra Parentesis', 'Comillas', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(34)
            elif clase == "Variable":
                self.funcionEstado = self.cambiarEstado(3)
            elif clase == "Condicion":
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para cuando se tiene una variable y nada mas
        def estado2(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Variable', 'int', 'double', 'float', 'boolean', 'String', 'Separador',
                         'Operador Logico', 'Operador Aritmetico','Abre Parentesis', 'Cierra Parentesis', 'Comillas', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(31)
            elif clase == "Condicion":
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == "Asignacion":
                self.funcionEstado = self.cambiarEstado(4)
            elif clase == 'Modificador':
                self.funcionEstado = self.cambiarEstado(5)
            elif clase == 'Suma/Resta 1':
                self.funcionEstado = self.cambiarEstado(6)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para cuando se tiene un tipo de variable seguido de una variable
        def estado3(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Variable', 'int', 'double', 'float', 'boolean', 'String',
                         'Abre Parentesis', 'Cierra Parentesis', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(31)
            elif clase == "Condicion":
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(7)
            elif clase == 'Asignacion':
                self.funcionEstado = self.cambiarEstado(8)
            elif clase in ['Modificador','Operador Logico', 'Operador Aritmetico','Suma/Resta 1']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para cuando se tiene una variable seguida de un igual
        def estado4(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo','Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(9)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(10)
            elif clase in ['Separador', 'Asignacion', 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                           'Suma/Resta 1','Fin de linea']:
                self.funcionEstado = self.cambiarEstado(36)
            elif clase == "Comillas":
                self.funcionEstado = self.cambiarEstado(11)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para una variable seguida de un modificador +=, -=, *=...
        def estado5(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo','Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(9)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(10)
            elif clase in ['Separador', 'Asignacion', 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                           'Suma/Resta 1','Fin de linea']:
                self.funcionEstado = self.cambiarEstado(36)
            elif clase == "Comillas":
                self.funcionEstado = self.cambiarEstado(11)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para una variable seguida de ++ o --
        def estado6(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Variable', 'int', 'double', 'float', 'boolean', 'String', 'Condicion',
                         'Separador', "Asignacion", 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                         'Suma/Resta 1', 'Abre Parentesis', 'Cierra Parentesis', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)

        # Estado para la secuencia Tipo Variable,
        def estado7(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(12)
            elif clase in ['int', 'double', 'float', 'boolean', 'String',
                         'Separador', "Asignacion", 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                         'Suma/Resta 1', 'Abre Parentesis', 'Cierra Parentesis', 'Comillas', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(34)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable =
        def estado8(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(13)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(14)
            elif clase in ['Separador', 'Asignacion', 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                           'Suma/Resta 1', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(36)
            elif clase == "Comillas":
                self.funcionEstado = self.cambiarEstado(15)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Variable = Variable
        def estado9(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable','int', 'double', 'float', 'boolean', 'String', "Variable Invalida"]:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(31)
            elif clase in ['Asignacion', 'Modificador']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico']:
                self.funcionEstado = self.cambiarEstado(16)
            elif clase == 'Suma/Resta 1':
                self.funcionEstado = self.cambiarEstado(17)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)

        # Estado para la secuencia Variable = dato (siendo dato un valor de cualquier tipo)
        def estado10(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable','int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(31)
            elif clase in ['Asignacion', 'Modificador']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico']:
                self.funcionEstado = self.cambiarEstado(16)
            elif clase == 'Suma/Resta 1':
                self.funcionEstado = self.cambiarEstado(38)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia V = "
        def estado11(nodo: Nodo):
            clase = nodo.clase
            self.quotation = True
            if clase == 'Comillas':
                self.funcionEstado = self.cambiarEstado(18)

        # Estado para la secuencia Tipo Variable, Variable
        def estado12(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable', 'int', 'double', 'float', 'boolean', 'String', 'Comillas', 'Abre Parentesis', 'Cierra Parentesis']:
                self.funcionEstado = self.cambiarEstado(31)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(7)
            elif clase == "Asignacion":
                self.funcionEstado = self.cambiarEstado(8)
            elif clase in ['Modificador', 'Operador Logico', 'Operador Aritmetico', 'Suma/Resta 1']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable = Variable
        def estado13(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable', 'int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(7)
            elif clase in ['Asignacion', 'Modificador', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico', ]:
                self.funcionEstado = self.cambiarEstado(19)
            elif clase == 'Suma/Resta 1':
                self.funcionEstado = self.cambiarEstado(20)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable = dato
        def estado14(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable', 'int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(7)
            elif clase in ['Asignacion', 'Modificador', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico']:
                self.funcionEstado = self.cambiarEstado(19)
            elif clase == 'Suma/Resta 1':
                self.funcionEstado = self.cambiarEstado(38)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable = "
        def estado15(nodo: Nodo):
            clase = nodo.clase
            self.quotation = True
            if clase == 'Comillas':
                self.funcionEstado = self.cambiarEstado(21)

        # Estado para secuencia Variable = Variable Operador (logico o aritmetico)
        def estado16(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(9)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(10)
            elif clase in ['Separador', 'Asignacion', 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                           'Suma/Resta 1', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(36)
            elif clase == '"':
                self.funcionEstado = self.cambiarEstado(11)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)


        # Estado para secuencia Variable = Variable ++ o --
        def estado17(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Variable', 'int', 'double', 'float', 'boolean', 'String', 'Condicion',
                         'Separador', "Asignacion", 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                         'Suma/Resta 1', 'Abre Parentesis', 'Cierra Parentesis', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)

        # Estado para secuencia Variable = "cualquier cadena de texto"
        def estado18(nodo: Nodo):
            clase = nodo.clase
            self.quotation = False
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable', 'int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(31)
            elif clase in ['Asignacion', 'Modificador', 'Suma/Resta 1', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico']:
                self.funcionEstado = self.cambiarEstado(16)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable = Variable Operador (logico o aritmetico)
        def estado19(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase == 'Variable':
                self.funcionEstado = self.cambiarEstado(13)
            elif clase in ['int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(14)
            elif clase in ['Separador', 'Asignacion', 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                           'Suma/Resta 1', 'Fin de linea']:
                self.funcionEstado = self.cambiarEstado(36)
            elif clase == '"':
                self.funcionEstado = self.cambiarEstado(15)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        # Estado para la secuencia Tipo Variable = Variable ++
        def estado20(nodo: Nodo):
            clase = nodo.clase
            if clase in ['Tipo', 'Variable', 'int', 'double', 'float', 'boolean', 'String', 'Condicion',
                         'Separador', "Asignacion", 'Modificador', 'Operador Logico', 'Operador Aritmetico',
                         'Suma/Resta 1', 'Abre Parentesis', 'Cierra Parentesis', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)

        # Estado para la secuencia Tipo Variable = "cadena de texto"
        def estado21(nodo: Nodo):
            clase = nodo.clase
            self.quotation = False
            if clase in ['Tipo', 'Condicion']:
                self.funcionEstado = self.cambiarEstado(35)
            elif clase in ['Variable', 'int', 'double', 'float', 'boolean', 'String']:
                self.funcionEstado = self.cambiarEstado(37)
            elif clase == "Separador":
                self.funcionEstado = self.cambiarEstado(7)
            elif clase in ['Asignacion', 'Modificador', 'Suma/Resta 1', 'Comillas']:
                self.funcionEstado = self.cambiarEstado(32)
            elif clase in ['Operador Logico', 'Operador Aritmetico']:
                self.funcionEstado = self.cambiarEstado(19)
            elif clase == 'Fin de linea':
                self.funcionEstado = self.cambiarEstado(100)
            elif clase == "Variable Invalida":
                self.funcionEstado = self.cambiarEstado(40)

        def estado31(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Not a statement"

        def estado32(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Unexpected token"

        def estado33(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Unnecesary semi-colon"

        def estado34(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Identifier expected"

        def estado35(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Reserved word"

        def estado36(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Expresion expected"

        def estado37(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Semicolon expected"

        def estado38(nodo: Nodo):
            self.finished = True
            self.mensajeError = "Variable expected"

        def estado39(nodo: Nodo):
            self.finished = True
            self.mensajeError = 'Missing "'

        def estado40(nodo: Nodo):
            self.finished = True
            self.mensajeError = 'Invalid variable'

        # Estado de exito
        def estado100(nodo: Nodo):
            self.finished = True
            """Si llegaste aqui coronaste"""

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
        elif cambio == 31:
            return estado31
        elif cambio == 32:
            return estado32
        elif cambio == 33:
            return estado33
        elif cambio == 34:
            return estado34
        elif cambio == 35:
            return estado35
        elif cambio == 36:
            return estado36
        elif cambio == 37:
            return estado37
        elif cambio == 38:
            return estado38
        elif cambio == 39:
            return estado39
        elif cambio == 40:
            return estado40
        elif cambio == 100:
            return estado100

    def __init__(self):
        self.funcionEstado = self.cambiarEstado(0)
        self.mensajeError = ""
        self.quotation = False
        self.finished = False

    def getMensajeError(self):
        return self.mensajeError

    def isFinished(self):
        return self.finished


