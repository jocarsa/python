#pip install pyautogui
import pyautogui
import time 
def buscar(texto):
    print(pyautogui.position())
    pyautogui.moveTo(319,126)
    pyautogui.tripleClick()
    pyautogui.write(texto)
    pyautogui.press('enter')

busqueda = ['manzanas','peras','limones','uva','platano']

for busca in busqueda:
    buscar(busca)
    #y aquí hago cosas
    time.sleep(4)


