print("Clases V2 Cesariin")
print("\n")
#Zona de clase
class Datos:
    #El constructor
    def __init__(self, estatura,peso):
        self.estatura=estatura
        self.peso=peso 
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts, Peso: {self.peso} Kg")
        print("\n")
    def mi_lista(self):
        Carros=["doge charger hellcat v8 srt pack","Dodge Challenger SRT Scat Pack","Ford Mustang Boss 302"]
        print(Carros)
        for carritos in Carros:
            print(carritos)
        print("\n")
    def mi_tupla(self):
        Frutas=("manzana","zanahoria","naranja")
        print(Frutas)
        for fruit in Frutas:
            print(fruit)
        print("\n")
    def mi_set(self):
        Animales={"perro","mono","elefante"}
        print(Animales)
        for Animal in Animales:
            print(Animal)
        print("\n")
    def mi_dic(self):
        Diccionario = {
            "Marca:": "wolsvagen",
            "Modelo:": "chevi",
            "Año:": 2007,
            "Color:": "gris"
            }
        for dick, di in Diccionario.items():
            print(dick,di)

#creacion de objeto info
info=Datos(1.75,70)

#utilizando el obj.
info.mostrar_datos()
print("Lista de mis carritos")
info.mi_lista()
print("Tupla de Verduras")
info.mi_tupla()
print("Sets de animales")
info.mi_set()
print("Diccionario de un camaro")
info.mi_dic()