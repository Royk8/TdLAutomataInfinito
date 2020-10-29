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
        self.separadores = ","
        self.finLinea = ";"
        self.simbolosSimples = "=+-*/%!<>|&,();"
        self.parentesis = ["()"]

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

    def getSeparadores(self):
        return self.separadores

    def getSimbolosSimples(self):
        return self.simbolosSimples

    def getParentesis(self):
        return self.parentesis

    def getCaracteresEspeciales(self):
        caracteres = []
        caracteres.append(self.asignacion)
        caracteres.append(self.modificadores)
        caracteres.append(self.aritmeticos)
        caracteres.append(self.logicos)
        caracteres.append(self.separadores)
        return caracteres