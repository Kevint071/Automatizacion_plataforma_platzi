from time import *
from tkinter import *
import tkinter.font as tf
import pyautogui as pyto
import webbrowser

sleep(4)

lista_paginas_texto = []
numero_videos = []
pagina_inicial = []
link = []
video_inicial = []
lista_paginas_evaluacion = []

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
        lista_paginas_texto.clear()
        try:
            lista = paginas.split(", ")
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
        numero_videos.clear()
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
        pagina_inicial.clear()
        try:
            pag_inicial = int(pag_inicial)
            pagina_inicial.append(pag_inicial)
            label_error3.place_forget()
            label_good3.place(x=520, y=210+10)
        except ValueError:
            label_good3.place_forget()
            label_error3.place(x=395, y=245)

    label_error4 = Label(text="Link no válido")
    label_good4 = Label(text="✔")
    
    def obtener_link(link_platzi):
        link.clear()
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
        video_inicial.clear()
        try:
            vid_ini = int(vid_ini)
            video_inicial.append(vid_ini)
            label_error5.place_forget()
            label_good5.place(x=520, y=340)
        except ValueError:
            label_good5.place_forget()
            label_error5.place(x=397, y=360)
    
    label_error6 = Label(text="Número no válido")
    label_good6 = Label(text="✔")
    
    def paginas_evaluacion(paginas):
        lista_paginas_evaluacion.clear()
        try:
            lista = paginas.split(", ")
            for i in lista:
                i = int(i) + 1
                lista_paginas_evaluacion.append(i)

            label_error6.place_forget()
            label_good6.place(x=520, y=400)
        except ValueError:
            label_good6.place_forget()
            label_error6.place(x=400, y=420)

    def cerrar_ventana():
        root.destroy()

    label = Label(text="Obtención de datos", font=titleStyle)
    label.place(x=237, y=30)

    label = Label(text="Agrega las páginas que contienen texto: ", font=fontStyle)
    label.place(x=70, y=97)

    entry_paginas = Entry()
    entry_paginas.place(x=390, y=98)

    button_pag_text = Button(text="Guardar", command=lambda: guardar_paginas(entry_paginas.get()))
    button_pag_text.place(x= 550, y=94)

    label = Label(text="Digite cuantas páginas de videos hay: ", font=fontStyle)
    label.place(x=85, y=157)

    entry_videos = Entry()
    entry_videos.place(x=390, y=158)

    button_num_videos = Button(text="Guardar", command=lambda: cantidad_videos(entry_videos.get()))
    button_num_videos.place(x= 550, y=154)

    label = Label(text="¿Por qué página desea comenzar?: ", font=fontStyle)
    label.place(x=100, y=220)

    entry_comenzar = Entry()
    entry_comenzar.place(x=390, y=221)

    button_comenzar = Button(text="Guardar", command=lambda: iniciar_automatizacion(entry_comenzar.get()))
    button_comenzar.place(x= 550, y=219)

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
    button_cerrar.place(x=295, y=460)

    label = Label(text="Paginas antes de una evaluacion de prueba: ", font=fontStyle)
    label.place(x=40, y=400)

    entry_pag_eval = Entry()
    entry_pag_eval.place(x=390, y=401)

    button_pag_eval = Button(text="Guardar", command=lambda: paginas_evaluacion(entry_pag_eval.get()))
    button_pag_eval.place(x= 550, y=399)
    
    root.mainloop()
obtener_paginas_texto()

numero_videos = numero_videos[0]
pagina_inicial = pagina_inicial[0]
link = link[0]
video_inicial = video_inicial[0]

print(f"Paginas con texto: {lista_paginas_texto}")
print(f"Cantidad de páginas: {numero_videos}")

pyto.alert(text='Presione el boton "Ok" para continuar', button="Ok", title="Procediendo automatización")

webbrowser.open(link)

# Se crea una funcion repetitiva para todos los videos 

sleep(8)

lista_pausas = []

def descargar_todos_los_videos(videos):
    for j in range(pagina_inicial, videos+1):
        print(j)

        if j in lista_paginas_evaluacion:
            pyto.click(690, 560)
            sleep(8)
        
        valor_lista = videos

        if j == pagina_inicial:
            for x in range(int(videos/10)):
                valor_lista = valor_lista - 10
                lista_pausas.append(valor_lista)
                lista_pausas.sort()
            print(f"Paginas de pausa: {lista_pausas}")
        print(lista_pausas)
        
        if j in lista_pausas:
            pyto.click(250, 240)
            pyto.alert(text='Haremos una pausa, presiona el botón "OK" hasta que solo quede 1 video en la lista de descarga para que mas adelante, no hayan errores por ralentización', title="Pausa", button="Ok")
            pyto.click(250, 240)
            sleep(1)
            
        
        # Si la variable iteradora está en alguno de estos lugares da click para ver el siguiente video

        if j in lista_paginas_texto:
            pyto.click(720, 440)
            pyto.click(720, 420)
            pyto.click(720, 400)
            pyto.click(720, 380)
            pyto.click(720, 360)
            pyto.click(720, 340)
            pyto.click(720, 320)
            pyto.click(720, 300)
            sleep(8)
            continue
        
        if j == video_inicial:
            # Pausa el video

            pyto.click(250, 240)
            sleep(1)

            pyto.alert(text='Asegúrate de ya tener la carpeta para descargar los videos', title='Recomendacion', button='Listo')
            sleep(1)

            # Renadua el video

            pyto.click(250, 240)
            sleep(1)

        # Se pausa el video y se abre la extension livecat

        pyto.click(250, 240)
        sleep(1)

        pyto.moveTo(1180, 50)
        pyto.click()
        sleep(2)
        pyto.moveTo(1165, 180)
        pyto.click()
        sleep(8)

        #Se edita el titulo del video

        pyto.moveTo(820, 480)
        sleep(2)
        pyto.click()
        pyto.press("down")

        for i in range(29):
            pyto.press("backspace")

        pyto.press("up")
        pyto.write(f"{j}. ")

        # Se guarda el video
        
        if j == video_inicial:
            pyto.alert(text='Si este es el primer video guárdalo, presiona el boton de "Terminé" cuando lo hayas guardado en la carpeta que tenías destinada para este curso. Tómate tu tiempo', title="Ubicación de descargas", button="Terminé")
        else:
            pyto.click(745, 535)
            sleep(2)
            pyto.click(660, 645)
            sleep(3)
            pyto.click(800, 450)
            sleep(4)
        

        # Se asegura que se esté en la ventana de platzi 

        pyto.click(80, 10)
        sleep(1)

        # Se da click para ver el siguiente video

        pyto.click(871, 645)
        sleep(8)
descargar_todos_los_videos(numero_videos)