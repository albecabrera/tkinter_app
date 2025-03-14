class Vehiculo():

    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud = longitud_metros
        self.ruedas = ruedas
        self.pais_origen = "Alemania"

    def arrancar(self):
        print("El vehículo ha arrancado.")

    def detener(self):
        print("El vehículo está detenido.")
    

# Instancia de dos objetos de la clase vehiculo
vehiculo_1 = Vehiculo("rojo", 4, 4)
vehiculo_2 = Vehiculo("negro", 4.10, 8)

print(vehiculo_1.pais_origen)
print(vehiculo_2.pais_origen)