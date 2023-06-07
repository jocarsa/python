class Gato:
    def __init__(self):
        self.edad = 0
        self.nombre = ""
        self.color = ""
    def maulla(self):
        print("el gato está maullando")
micifu = Gato()
print(micifu.edad)
micifu.edad += 1
print(micifu.edad)
micifu.maulla()
