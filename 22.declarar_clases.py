# Se declara la clase vehículo
class Vehiculo():
    # Atributos
    color = None
    longitud_metros = None
    ruedas = 4

    # Métodos
    def arrancar (self):
        print("El vehículo ha arrancado")   
    
    def detener (self):
        print("El vehículo se ha detenido")  

vehiculo_1 = Vehiculo()
vehiculo_2  = Vehiculo()

# Llamadas a métodos
vehiculo_1.arrancar()
vehiculo_1.detener()

vehiculo_2.material_aleron = "Fibra de carbono"

print(vehiculo_2.material_aleron )
 