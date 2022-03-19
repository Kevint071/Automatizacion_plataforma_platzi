import pyautogui as pyt

print("\nPresiona Ctrl + C para quitar...")

try:
    while True:
        x, y = pyt.position()
        posicion = f"X: {str(x).rjust(4)} Y: {str(y).rjust(4)}"
        print(posicion, end = "")
        print("\b" * len(posicion), end = "")
except KeyboardInterrupt:
    print("\nProceso finalizado")