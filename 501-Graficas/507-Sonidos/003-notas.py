#pip install playsound
from playsound import playsound
import os
directorio = 'mp3/'
notas = []
for archivo in os.listdir("mp3"):
    # check if current path is a file
    if os.path.isfile(os.path.join(directorio, archivo)):
        print("es archivo")
        notas.append(directorio+archivo)
for nota in notas:
    playsound(nota)
print('playing sound using  playsound')
