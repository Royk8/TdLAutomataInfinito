from Code.Nodo import Nodo

class ReconocedorRecursivo():

    def __init__(self, listaCodigo: list):
        #La lista con los tokens generados anteriormente, y con el codigo completo
        self.lista = listaCodigo
        #Define la posicion actual de la lista
        self.estado = 0
        self.codigoLeido = ''

    def principal(self):
        self.ntS()
        if(self.lista[self.estado]) == 'Fin de Secuencia':
            self.codigoLeido = "COMPILACION COMPLETA\n" + self.codigoLeido
        else:
            self.codigoLeido = "EL CODIGO CONTIENE ERRORES\n" + self.codigoLeido

    # Devuelve el tipo del simbolo actual que esta siendo leido en la lista
    def simbolo(self):
        nodo = self.lista[self.estado]
        return str(nodo.clase)

    # Avanza en la lista al siguiente simbolo ya que el actual fue aceptado.
    def lea(self):
        self.codigoLeido += str(self.lista[self.estado].valor) + " "
        if self.lista[self.estado].clase == 'Fin de linea': self.codigoLeido += '\n'
        self.estado += 1

    def siguienteLinea(self):
        while self.simbolo() != 'Fin de linea':
            if self.simbolo() == 'Fin de Secuencia': return
            self.estado += 1
        self.estado += 1
        self.ntS()

    # No terminal <S>
    def ntS(self):
        if self.simbolo() == 'Tipo':
            self.lea()
            self.ntT()
            if self.simbolo() == 'Fin de linea':
                self.lea()
                self.ntS()
            else:
                if self.simbolo() != 'Fin de Secuencia':
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Se esperaba un punto y coma, pero se recibió [{self.simbolo()}]-\n"
                self.siguienteLinea()
        elif self.simbolo() == 'Variable':
            self.lea()
            self.ntV()
            if self.simbolo() == 'Fin de linea':
                self.lea()
                self.ntS()
            else:
                if self.simbolo() != 'Fin de Secuencia':
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Se esperaba un punto y coma, pero se recibió [{self.simbolo()}]-\n"
                self.siguienteLinea()
        elif self.simbolo() == 'Condicion':
            self.lea()
            if self.simbolo() == 'Abre Parentesis':
                self.lea()
                self.ntExpresion()
                if self.simbolo() == 'Cierra Parentesis':
                    self.lea()
                    if self.simbolo() == 'Abre Llave':
                        self.lea()
                        self.ntS()
                        if self.simbolo() == 'Cierra Llave':
                            self.lea()
                            self.ntElse()
                            if self.simbolo() == 'Fin de linea':
                                self.lea()
                                self.ntS()
                            else:
                                if self.simbolo() != 'Fin de Secuencia':
                                    self.codigoLeido += str(self.lista[self.estado].valor)
                                    self.codigoLeido += f" \n-ERROR: Se esperaba un punto y coma, pero se recibió [{self.simbolo()}]-\n"
                                self.siguienteLinea()
                        else:
                            self.codigoLeido += str(self.lista[self.estado].valor)
                            self.codigoLeido += f" \n-ERROR: Se esperaba una llave que cierra, pero se recibió [{self.simbolo()}]-\n"
                            self.siguienteLinea()
                    else:
                        self.codigoLeido += str(self.lista[self.estado].valor)
                        self.codigoLeido += f" \n-ERROR: Se esperaba una llave que abre, pero se recibió [{self.simbolo()}]-\n"
                        self.siguienteLinea()
                else:
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Se esperaba un cierra de parentesis, pero se recibió [{self.simbolo()}]-\n"
                    self.siguienteLinea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-ERROR: Se esperaba un parentesis que abre, pero se recibió [{self.simbolo()}]-\n"
                self.siguienteLinea()
        elif self.simbolo() == 'Fin de Secuencia' or self.simbolo() == 'Cierra Llave':
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un Tipo, Variable o Estructura condicional, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <T>
    def ntT(self):
        if self.simbolo() == 'Variable':
            self.lea()
            self.ntTV()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <V>
    def ntV(self):
        if self.simbolo() == 'Asignacion':
            self.lea()
            self.ntVIgual()
        elif self.simbolo() == 'Modificador':
            self.lea()
            self.ntVIgual()
        elif self.simbolo() == 'Suma/Resta 1':
            self.lea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una asignacion o un modificador de valor, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <TV>
    def ntTV(self):
        if self.simbolo() == 'Separador':
            self.lea()
            self.ntTVComa()
        elif self.simbolo() == 'Asignacion':
            self.lea()
            self.ntTVIgual()
        elif self.simbolo() == 'Cierra Parentesis' or self.simbolo() == 'Fin de linea':
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una coma o una asignacion de valor, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <V=>
    def ntVIgual(self):
        if self.simbolo() == 'Variable':
            self.lea()
            self.ntVIgualV()
        elif self.simbolo() in ['int','float','double','boolean','String']:
            self.lea()
            self.ntVIgualD()
        elif self.simbolo() == 'Comillas':
            self.lea()
            estadoAux = self.estado
            codigoAux = self.codigoLeido
            while self.simbolo() != 'Comillas':
                self.lea()
                if self.simbolo() == 'Fin de Secuencia':
                    self.estado = estadoAux
                    self.codigoLeido = codigoAux
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Nunca se cierran las comillas\n"
                    self.siguienteLinea()
                    return
            self.lea()
            self.ntVIgualD()
        elif self.simbolo() == 'Abre Parentesis':
            self.lea()
            self.ntVIgual()
            if self.simbolo() == 'Cierra Parentesis':
                self.lea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-ERROR: Parentesis Desbalanceados-\n"
                self.siguienteLinea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, una Constante Numerica" \
                                f" o una cadena de caracteres, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <TV,>
    def ntTVComa(self):
        if self.simbolo() == 'Variable':
            self.lea()
            self.ntTV()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <TV=>
    def ntTVIgual(self):
        if self.simbolo() == 'Variable':
            self.lea()
            self.ntTVIgualV()
        elif self.simbolo() in ['int','float','double','boolean','String']:
            self.lea()
            self.ntTVIgualD()
        elif self.simbolo() == 'Comillas':
            self.lea()
            estadoAux = self.estado
            codigoAux = self.codigoLeido
            while self.simbolo() != 'Comillas':
                self.lea()
                if self.simbolo() == 'Fin de Secuencia':
                    self.estado = estadoAux
                    self.codigoLeido = codigoAux
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Nunca se cierran las comillas\n"
                    self.siguienteLinea()
                    return
            self.lea()
            self.ntTVIgualD()
        elif self.simbolo() == 'Abre Parentesis':
            self.lea()
            self.ntTVIgual()
            if self.simbolo() == 'Cierra Parentesis':
                self.lea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-ERROR: Parentesis Desbalanceados-\n"
                self.siguienteLinea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, una constante numerica " \
                                f"o una cadena de caracteres pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <V=V>
    def ntVIgualV(self):
        if self.simbolo() in ['Operador Aritmetico', 'Operador Logico']:
            self.lea()
            self.ntVIgualVOp()
        elif self.simbolo() == 'Suma/Resta 1':
            self.lea()
        elif self.simbolo() in ['Cierra Parentesis', 'Fin de linea']:
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un operador aritmetico o logico " \
                                f"o un punto y coma, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <V=d>
    def ntVIgualD(self):
        if self.simbolo() in ['Operador Aritmetico', 'Operador Logico']:
            self.lea()
            self.ntVIgualVOp()
        elif self.simbolo() in ['Cierra Parentesis', 'Fin de linea']:
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un operador aritmetico o logico, " \
                                f"o un punto y coma, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    def ntTVIgualV(self):
        if self.simbolo() == 'Separador':
            self.lea()
            self.ntTVComa()
        elif self.simbolo() in ['Operador Aritmetico', 'Operador Logico']:
            self.lea()
            self.ntTVIgualVOp()
        elif self.simbolo() == 'Suma/Resta 1':
            self.lea()
        elif self.simbolo() in ['Cierra Parentesis', 'Fin de linea']:
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un operador aritmetico o logico, " \
                                f"una coma o un punto y coma, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <TV=d>
    def ntTVIgualD(self):
        if self.simbolo() == 'Separador':
            self.lea()
            self.ntTVComa()
        elif self.simbolo() in ['Operador Aritmetico', 'Operador Logico']:
            self.lea()
            self.ntTVIgualVOp()
        elif self.simbolo() in ['Cierra Parentesis', 'Fin de linea']:
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un punto y coma, una coma, operador aritmetico o logico" \
                                f", pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <V=VOp>
    def ntVIgualVOp(self):
        if self.simbolo() in ['Variable','int','float','double','boolean','String']:
            self.lea()
            self.ntVIgualV()
        elif self.simbolo() == 'Comillas':
            self.lea()
            estadoAux = self.estado
            codigoAux = self.codigoLeido
            while self.simbolo() != 'Comillas':
                self.lea()
                if self.simbolo() == 'Fin de Secuencia':
                    self.estado = estadoAux
                    self.codigoLeido = codigoAux
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Nunca se cierran las comillas\n"
                    self.siguienteLinea()
                    return
            self.lea()
            self.ntVIgualV()
        elif self.simbolo() == 'Abre Parentesis':
            self.lea()
            self.ntVIgualVOp()
            if self.simbolo() == 'Cierra Parentesis':
                self.lea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-Parentesis desbalanceados-\n"
                self.siguienteLinea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, constante numerica o " \
                                f"o cadena de caracteres, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <TV=VOp>
    def ntTVIgualVOp(self):
        if self.simbolo() in ['Variable', 'int', 'float', 'double', 'boolean', 'String']:
            self.lea()
            self.ntTVIgualV()
        elif self.simbolo() == 'Comillas':
            self.lea()
            estadoAux = self.estado
            codigoAux = self.codigoLeido
            while self.simbolo() != 'Comillas':
                self.lea()
                if self.simbolo() == 'Fin de Secuencia':
                    self.estado = estadoAux
                    self.codigoLeido = codigoAux
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Nunca se cierran las comillas\n"
                    self.siguienteLinea()
                    return
            self.lea()
            self.ntVIgualV()
        elif self.simbolo() == 'Abre Parentesis':
            self.lea()
            self.ntTVIgualVOp()
            if self.simbolo() == 'Cierra Parentesis':
                self.lea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-Parentesis desbalanceados-\n"
                self.siguienteLinea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable, constante numerica o " \
                                f"cadena de caracteres, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <Expresion>
    def ntExpresion(self):
        if self.simbolo() == 'Variable':
            self.lea()
            self.ntRestoExpresion()
        elif self.simbolo() == 'boolean':
            self.lea()
        elif self.simbolo() == "Abre Parentesis":
            self.lea()
            self.ntExpresion()
            if self.simbolo() == "Cierra Parentesis":
                self.lea()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-Parentesis desbalanceados-\n"
                self.siguienteLinea()
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba una Variable o un valor booleano, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    # No terminal <RestoExpresion>
    def ntRestoExpresion(self):
        if self.simbolo() == 'Operador Logico':
            self.lea()
            self.ntExpresion()
        elif self.simbolo() == 'Cierra Parentesis':
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un operador logico o un cierre parentesis, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()

    def ntElse(self):
        if self.simbolo() == 'Else':
            self.lea()
            if self.simbolo() == 'Abre Llave':
                self.lea()
                self.ntS()
            else:
                self.codigoLeido += str(self.lista[self.estado].valor)
                self.codigoLeido += f" \n-ERROR: Se esperaba una apertura de llave, pero se recibió [{self.simbolo()}]-\n"
                self.siguienteLinea()
                if self.simbolo() == 'Cierra Llave':
                    self.lea()
                else:
                    self.codigoLeido += str(self.lista[self.estado].valor)
                    self.codigoLeido += f" \n-ERROR: Se esperaba un cierre de llaves, pero se recibió [{self.simbolo()}]-\n"
                    self.siguienteLinea()
        elif self.simbolo() == 'Fin de linea':
            return
        else:
            self.codigoLeido += str(self.lista[self.estado].valor)
            self.codigoLeido += f" \n-ERROR: Se esperaba un else o un punto y coma, pero se recibió [{self.simbolo()}]-\n"
            self.siguienteLinea()
    