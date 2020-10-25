def reconocerTipo(palabra):
    if tipos.__contains__(palabra):
        return True
    return False

linea = "int perico = cafe + leche"
separados = linea.split(' ')
print(separados)
tipos = ['int', 'double', 'string', 'float', 'boolean']
print(reconocerTipo(separados[0]))





"""
int
double
string
float
boolean
"""