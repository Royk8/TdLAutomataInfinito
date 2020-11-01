from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Code.Controller import Controller


def browseFile():
    try:
        global filename
        filename = filedialog.askopenfilename(
            initialdir="./Windows", title="Seleccione un archivo", filetypes=(("Text files", "*.java*"), ("all files", "*.*")))
        global text
        mensaje.configure(text="Archivo Seleccionado: "+filename)
        text = list(open(filename, 'r'))
        text = [i.replace('\n', '')for i in text]
        lbox.delete(0, 'end')
        for i in range(len(text)):
            lbox.insert(i+1, str(i+1)+'  '+text[i])

    except:
        messagebox.showinfo("Error", "No selecciono ningun archivo")


def analizador():
    try:
        global text2
        text2 = ''
        for line in text:
            text2 += Controller.reconocedor(line)

        text2 = text2.split('\n')
        lbox2.delete(0, 'end')
        for i in range(len(text2)):
            lbox2.insert(i+1, str(i+1)+'  '+text2[i])
    except:
        messagebox.showinfo("Error", "No selecciono ningun archivo")


def getReg():
    try:
        print(filename)
    except:
        messagebox.showinfo("Error", "No ha iniciado automatador")


# Ventana
ventana = Tk()
ventana.title('Automatador')
ventana.config(background="#353535")
ventana.attributes('-zoomed', True)

# Entrada de texto
mensaje = Label(ventana, text="Escoja un archivo o abrase", fg="blue")

# posicion ENtrada de texto
mensaje.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones
boton_archivo = Button(ventana, text='Escojer un archivo',
                       width=15, height=2, command=browseFile)
boton_salida = Button(ventana, text='Salir', width=15, height=2, command=exit)
boton_proceso = Button(ventana, text='Iniciar automata',
                       width=15, height=2, command=analizador)
boton_reg = Button(ventana, text='Registro',
                   width=15, height=2, command=getReg)

# Posición de botones
boton_archivo.grid(row=1, column=0, padx=7, pady=5)
boton_salida.grid(row=1, column=2, padx=5, pady=5)
boton_proceso.grid(row=1, column=1, padx=5, pady=5)
boton_reg.grid(row=5, column=0, padx=5, pady=5)

# Cajor que muestra
lbox = Listbox(ventana, height=11, width=80)
lbox2 = Listbox(ventana, height=13, width=180)
lbox3 = Listbox(ventana, height=13, width=180)

# Posición de cajon
lbox.grid(row=2, column=0, columnspan=3)
lbox2.grid(row=3, column=0, columnspan=3)
lbox3.grid(row=4, column=0, columnspan=3)

ventana.mainloop()
