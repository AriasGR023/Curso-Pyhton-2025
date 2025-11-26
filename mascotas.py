# Factory Method para crear diferentes tipos de mascotas
# Patrón Factory para crear mascotas
class FabricaMascotas:
    @staticmethod
    def crear_mascota(tipo, nombre, edad, raza="Desconocida"):
        if tipo.lower() == "perro":
            return Perro(nombre, edad, raza)
        elif tipo.lower() == "gato":
            return Gato(nombre, edad, raza)
        elif tipo.lower() == "ave":
            return Ave(nombre, edad, raza)
        else:
            return Mascota(nombre, edad, tipo)

class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.vacunada = False
        self.enfermedades = []
    
    def vacunar(self):
        self.vacunada = True
        return f"{self.nombre} ha sido vacunado"
    
    def agregar_enfermedad(self, enfermedad):
        self.enfermedades.append(enfermedad)
        return f"Enfermedad {enfermedad} agregada a {self.nombre}"
    
    def mostrar_info(self):
        vacuna = "Sí" if self.vacunada else "No"
        return f"{self.nombre} ({self.tipo}) - {self.edad} años - Vacunado: {vacuna}"

class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Perro")
        self.raza = raza
    
    def ladrar(self):
        return "¡Guau guau!"
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Raza: {self.raza}"

class Gato(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Gato")
        self.raza = raza
    
    def maullar(self):
        return "¡Miau miau!"
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Raza: {self.raza}"

class Ave(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad, "Ave")
        self.raza = raza
    
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} - Raza: {self.raza}"