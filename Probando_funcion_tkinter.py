import tkinter as tk


root = tk.Tk()
root.title('Ejemplo ventana: Ocultar y mostrar widgets')
root.geometry('600x80')


# Agregar los widgets....

labelExample = tk.Label(root, text="Este es un ejemplo de un widget (en este caso un label)")


def ShowLabel(event=None): # Mostrar los widgets por medio de esta función al hacer clic
    labelExample.place(x=13, y=15)

def HideLabel(event=None): # Ocultar los widgets por medio de esta función al hacer clic
    labelExample.place_forget() 

HideLabelButton = tk.Button(root, text="Ocultar el label", command=HideLabel)
ShowLabelButton = tk.Button(root, text="Mostrar el label", command=ShowLabel)

HideLabelButton.place(x=485, y=12)
ShowLabelButton.place(x=359, y=12)

root.mainloop() # Fin ciclo de eventos