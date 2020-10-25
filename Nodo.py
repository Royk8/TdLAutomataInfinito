class Nodo:
    def __init__(self, clase, valor):
        self.clase = clase
        self.valor = valor
        self.liga = None

    def setLiga(self, liga):
        self.liga = liga

