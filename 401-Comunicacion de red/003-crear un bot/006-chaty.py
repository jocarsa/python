#pip install pyautogui
import pyautogui
import time 
def buscar(texto):
    delay1 = 1
    delay2 = 30
    print(pyautogui.position())
    #nuevo chat
    pyautogui.moveTo(100,100)
    pyautogui.click()
    time.sleep(delay1)
    #click en casilla de pregunta
    pyautogui.moveTo(900,950)
    pyautogui.click()
    time.sleep(delay1)
    #escribir pregunta
    pyautogui.write(texto)
    pyautogui.press('enter')
    time.sleep(delay2)
    #subir scroll
    pyautogui.moveTo(1918,83)
    pyautogui.click()
    time.sleep(delay1)
    #copiar texto
    pyautogui.moveTo(1428,185)
    pyautogui.click()
    time.sleep(delay1)
    #segunda pestaña
    pyautogui.moveTo(348,12)
    pyautogui.click()
    time.sleep(delay1)
    # estilos
    pyautogui.moveTo(341,156)
    pyautogui.click()
    time.sleep(delay1)
    # estilo 1
    pyautogui.moveTo(378,425)
    pyautogui.click()
    time.sleep(delay1)
    # final de pagina
    pyautogui.moveTo(1857,1010)
    pyautogui.click()
    time.sleep(delay1)
    # escribir
    pyautogui.write(texto)
    pyautogui.press('enter')
    #estilos
    pyautogui.moveTo(341,156)
    pyautogui.click()
    time.sleep(delay1)
    #parrafo
    pyautogui.moveTo(378,207)
    pyautogui.click()
    time.sleep(delay1)
    # menu editar
    pyautogui.moveTo(147,117)
    pyautogui.click()
    time.sleep(delay1)
    # menu pegar
    pyautogui.moveTo(171,297)
    pyautogui.click()
    time.sleep(delay1)
    pyautogui.press('enter')
    time.sleep(delay1)
    # pestaña 1
    pyautogui.moveTo(125,14)
    pyautogui.click()
    time.sleep(delay1)
    
    

busqueda = ['lenguajes de marcas','programacion de aplicaciones','bases de datos','sistemas informáticos','entornos de desarrollo']

for busca in busqueda:
    buscar(busca)
    


