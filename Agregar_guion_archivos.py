import os
from pyautogui import prompt


def directorio_simple(curso):
    videos = os.listdir(curso)

    for nombre in videos:
        num = nombre[:2].replace(".", "")

        if num.count("_"):
            return None

        elif int(num) > 9:

            nombre_nuevo = "_" + nombre
            print(nombre_nuevo)
            os.rename(nombre, nombre_nuevo)


def directorio_complejo(directorio_principal):

    cursos = os.listdir(directorio_principal)

    for curso in cursos:
        curso_individual = os.chdir(f"{directorio_principal}/{curso}")
        curso_individual = os.getcwd()
        
        directorio_simple(curso_individual)


def run():
    directorio = prompt(text='Digite el directorio al que desea cambiarle los nombres de los archivos', title="Obtener directorio")

    print(directorio)

    directorio_principal = os.chdir(directorio)
    directorio_principal = os.getcwd()
    print(directorio_principal)

    # Ver lo que está dentro de esta carpeta

    directorio_interior = os.listdir(directorio_principal)

    if directorio_interior[0].count("mp4") >= 1:
        directorio_simple(directorio_principal)
    else:
        directorio_complejo(directorio_principal)

if __name__ == "__main__":
    run()


