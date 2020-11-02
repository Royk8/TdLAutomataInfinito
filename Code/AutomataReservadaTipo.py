from Code.AutomataReservada import AutomataReservada


# Variacion del automata de palabras reservads que reconoce String, int, float, etc.
class AutomataReservadaTipo(AutomataReservada):

    def getClase(self):
        return "Tipo"