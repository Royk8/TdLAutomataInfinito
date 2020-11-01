from tkinter import *
from tkinter import filedialog


def browseFile():
    filename = filedialog.askopenfilename(
        initialdir="./Windows", title="Seleccione un archivo", filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    global text
    texto1.configure(text="Archivo Seleccionado: "+filename)
    text = list(open(filename, 'r'))
    text = [i[:-1] for i in text]
    for i in range(len(text)):
        lbox.insert(i+1, text[i])


def analizador():
    print(text)
    None


# Ventana
ventana = Tk()
ventana.title('Automatador')
ventana.config(background="gray")

# Entrada de texto
texto1 = Label(ventana, text="Escoja un archivo o abrase", fg="blue")
texto1.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones
boton_archivo = Button(ventana, text='Escojer un archivo',
                       width=15, height=2, command=browseFile)
boton_salida = Button(ventana, text='Salir', width=15, height=2, command=exit)
boton_proceso = Button(ventana, text='Iniciar automata',
                       width=15, height=2, command=analizador)


boton_archivo.grid(row=1, column=0, padx=7, pady=5)
boton_salida.grid(row=3, column=0, padx=5, pady=5)
boton_proceso.grid(row=2, column=0, padx=5, pady=5)

# Cajor que muestra
lbox = Listbox(ventana)
lbox.grid(row=4, column=0)

ventana.mainloop()
