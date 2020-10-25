class Simbolos:
    class __Singleton:
        def __init__(self):
            self.alfanumerico = 'abcdefghijklmnopqrstuvwxyz_1234567890'
            self.asignacion = ['=']
            self.cambiador = ['+=','-=','*=','/=','%=']
            self.operadores = ['+','-','*','/','%','==','!=','<=','>=','|','||','&','&&']

        def getAlfanumericos(self):
            return self.alfanumerico

        def getAsignacion(self):
            return self.asignacion

        def getOperadores(self):
            return self.operadores

    instance = None

    def __init__(self):
        if not Simbolos.instance:
            Simbolos.instance = Simbolos.__Singleton()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def getSimbolos(self, tipo):
        if tipo == 'alfanumericos':
            return self.instance.getAlfanumericos()
        elif tipo == 'asignacion':
            return self.instance.getAsignacion()
        elif tipo == 'operadores':
            return self.instance.getOperadores()