class Gato:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.color = ""
    def maulla(self):
        return "el gato está maullando"
    def getEdad(self):
        return self.edad
    def setEdad(self,nuevaedad):
        self.edad = nuevaedad
micifu = Gato()
print(micifu.getEdad())
micifu.setEdad(1)
print(micifu.getEdad())
print(micifu.maulla())
