# crear una clase llamada motocicleta
class Motocicleta():
    
    # Atributos de clase
    estado = "nuevo"
    motor = False
  
    # Métodos
    def __init__(self, color="rojo", matricula="ABC123", combustible_litros=5, numero_ruedas=4, marca="Honda", modelo=250, fecha_fabricacion=2010, velocidad_punta=200, peso=150):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        
    def arrancar(self):
        if self.motor:
            print(f'Se escucha un molesto sonido al girar la llave. El motor ya estaba arrancado. ')
        else: 
            print(f'Se ha arrancado el motor. El motor ruge como un león')
    
    def detener(self):
        if self.motor:
            print(f'Se detiene el motor.')
        else: 
            print(f'No puedes apagar el motor porque ya está apagado')    
            
    motocicleta_yamaha1 = Motocicleta("Roja y blanca", "BNAC315", 10, 2, "Yamaha ") 
        
    
        
 