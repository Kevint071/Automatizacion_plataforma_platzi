from tkinter import *
import tkinter.font as tf

lista_paginas_texto = []
numero_videos = []
pagina_inicial = []
link = []
video_inicial = []

def obtener_paginas_texto():
    root = Tk()
    root.title("Páginas de texto")
    
    canvas = Canvas(root, height=550, width=650)
    canvas.pack()

    fontStyle = tf.Font(family="Lucida Grande", size = 13)
    titleStyle = tf.Font(family="Comic Sans Ms", size = 18)

    label_error = Label(root, text="Números no válidos")
    label_good = Label(root, text="✔")

    def guardar_paginas(paginas):
        try:
            lista = paginas.split(",")
            for i in lista:
                i = int(i)
                lista_paginas_texto.append(i)

            label_error.place_forget()
            label_good.place(x=520, y=87+10)
        except ValueError:
            label_good.place_forget()
            label_error.place(x=395, y=110+10)
    
    label_error2 = Label(text="Número no válido")
    label_good2 = Label(text="✔")

    def cantidad_videos(num_videos):
        try:
            num_videos = int(num_videos)
            numero_videos.append(num_videos)

            label_error2.place_forget()
            label_good2.place(x=520, y=148+10)
        except ValueError:
            label_good2.place_forget()
            label_error2.place(x=395, y=168+10)
    
    label_error3 = Label(text="Número no válido")
    label_good3 = Label(text="✔")

    def iniciar_automatizacion(pag_inicial):
        try:
            pag_inicial = int(pag_inicial)
            pagina_inicial.append(pag_inicial)
            label_error3.place_forget()
            label_good3.place(x=520, y=210+10)
        except ValueError:
            label_good3.place_forget()
            label_error3.place(x=395, y=235+10)

    label_error4 = Label(text="Link no válido")
    label_good4 = Label(text="✔")
    
    def obtener_link(link_platzi):
        if len(link_platzi) != 0 and link_platzi.count(".") >= 1:
            link.append(link_platzi)
            label_error4.place_forget()
            label_good4.place(x=520, y=280)
        else:
            label_good4.place_forget()
            label_error4.place(x=410, y=305)

    label_error5 = Label(text="Número no válido")
    label_good5 = Label(text="✔")
    
    def vid_inicial(vid_ini):
        try:
            vid_ini = int(vid_ini)
            video_inicial.append(vid_ini)
            label_error5.place_forget()
            label_good5.place(x=520, y=340)
        except ValueError:
            label_good5.place_forget()
            label_error5.place(x=397, y=360)

    def cerrar_ventana():
        root.destroy()

    label = Label(text="Obtención de datos", font=titleStyle)
    label.place(x=237, y=30)

    label = Label(text="Agrega las páginas que contienen texto: ", font=fontStyle)
    label.place(x=70, y=87+10)

    entry_paginas = Entry()
    entry_paginas.place(x=390, y=88+10)

    button_pag_text = Button(text="Guardar", command=lambda: guardar_paginas(entry_paginas.get()))
    button_pag_text.place(x= 550, y=84+10)

    label = Label(text="Digite cuantas páginas de videos hay: ", font=fontStyle)
    label.place(x=85, y=147+10)

    entry_videos = Entry()
    entry_videos.place(x=390, y=148+10)

    button_num_videos = Button(text="Guardar", command=lambda: cantidad_videos(entry_videos.get()))
    button_num_videos.place(x= 550, y=144+10)

    label = Label(text="¿Por qué página desea comenzar?: ", font=fontStyle)
    label.place(x=100, y=210+10)

    entry_comenzar = Entry()
    entry_comenzar.place(x=390, y=211+10)

    button_comenzar = Button(text="Guardar", command=lambda: iniciar_automatizacion(entry_comenzar.get()))
    button_comenzar.place(x= 550, y=209+10)

    label = Label(text="Digite el link: ", font=fontStyle)
    label.place(x=269, y=280)

    entry_link = Entry()
    entry_link.place(x=390, y=281)

    button_link = Button(text="Guardar", command=lambda: obtener_link(entry_link.get()))
    button_link.place(x= 550, y=279)

    label = Label(text="Digite la primera página que contiene video: ", font=fontStyle)
    label.place(x=40, y=340)

    entry_vid_ini = Entry()
    entry_vid_ini.place(x=390, y=341)

    button_vid_ini = Button(text="Guardar", command=lambda: vid_inicial(entry_vid_ini.get()))
    button_vid_ini.place(x= 550, y=339)

    button_cerrar = Button(text="Cerrar", command=lambda: cerrar_ventana(), font=titleStyle)
    button_cerrar.place(x=295, y=420)
    
    root.mainloop()
obtener_paginas_texto()
