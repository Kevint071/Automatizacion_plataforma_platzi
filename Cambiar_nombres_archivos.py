import pyautogui as pyto
from time import sleep


numero_videos = int(input("Digite la cantidad de videos a convertir: "))
distancia_1_10 = int(input("Digite la cantidad de videos que hay desde el 1 hasta el 10: "))

pyto.alert(text='Presione el boton "Ok" cuando esté en la carpeta del explorador de archivos y los archivos esten en tamaño detalles, organizacion de nombre ascendente', button="Ok", title="Anticipante de cambio de nombres")

# Ciclo para editar nombres

y = 327

def repetir_down(num):
    for i in range(num):
        pyto.press("down")

pyto.click(1230, 260)
sleep(0.5)
for i in range(6):
    sleep(0.1)
    pyto.press("tab")

for i in range(4):
    sleep(0.1)
    pyto.press("right")

sleep(0.7)
pyto.press("enter")

repetir_down(distancia_1_10 - 1)

for i in range(numero_videos):

    pyto.press("f2")
    sleep(1)
    pyto.press("left")
    sleep(0.5)
    pyto.press("_")
    sleep(1)
    pyto.press("enter")
    sleep(1)
    repetir_down(distancia_1_10)