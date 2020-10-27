def singleton(cls):

    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args,**kwargs)

        return instances[cls]

    return wrap

@singleton
class Simbols():
    def __init__(self):
        self.alfanumerico = 'abcdefghijklmnopqrstuvwxyz_1234567890'
        self.numericos = '0123456789'
        self.asignacion = ['=']
        self.modificadores = ['+=', '-=', '*=', '/=', '%=']
        self.aritmeticos = ['+', '-', '*', '/', '%']
        self.logicos = ['==', '!=', '<=', '>=', '|', '||', '&', '&&']

    def getAlfanumericos(self):
        return self.alfanumerico

    def getNumericos(self):
        return self.numericos

    def getAsignacion(self):
        return self.asignacion

    def getAritmeticos(self):
        return self.aritmeticos

    def getModificadores(self):
        return self.modificadores

    def getLogicos(self):
        return self.logicos

    def getSimbolos(self, tipo):
        if tipo == 'alfanumericos':
            return self.getAlfanumericos()
        elif tipo == 'asignacion':
            return self.getAsignacion()
        elif tipo == 'operadores':
            return self.getOperadores()
        elif tipo == 'modificadores':
            return self.getModificadores()