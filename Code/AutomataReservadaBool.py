from Code.AutomataReservada import AutomataReservada


# Variacion de el automata de palabras reservadas que reconoce false y true
class AutomataReservadaBool(AutomataReservada):

    def getClase(self):
        return "boolean"