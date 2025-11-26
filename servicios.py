# Patrón Observer para notificaciones
class Observador:
    def actualizar(self, mensaje):
        pass

class SistemaNotificaciones:
    def __init__(self):
        self.observadores = []
    
    def agregar_observador(self, observador):
        self.observadores.append(observador)
    
    def eliminar_observador(self, observador):
        self.observadores.remove(observador)
    
    def notificar_todos(self, mensaje):
        resultados = []
        for observador in self.observadores:
            resultados.append(observador.actualizar(mensaje))
        return resultados

class NotificacionEmail(Observador):
    def actualizar(self, mensaje):
        return f"EMAIL ENVIADO: {mensaje}"

class NotificacionSMS(Observador):
    def actualizar(self, mensaje):
        return f"SMS ENVIADO: {mensaje}"

class NotificacionApp(Observador):
    def actualizar(self, mensaje):
        return f"APP NOTIFICATION: {mensaje}"

# Patrón Strategy para servicios veterinarios
class EstrategiaServicio:
    def ejecutar(self, mascota):
        pass

class EstrategiaVacunacion(EstrategiaServicio):
    def ejecutar(self, mascota):
        return mascota.vacunar()

class EstrategiaConsultaGeneral(EstrategiaServicio):
    def ejecutar(self, mascota):
        return f"Consulta general realizada a {mascota.nombre}"

class EstrategiaDesparasitacion(EstrategiaServicio):
    def ejecutar(self, mascota):
        return f"{mascota.nombre} ha sido desparasitado"

class EstrategiaCirugia(EstrategiaServicio):
    def ejecutar(self, mascota):
        return f"Cirugía programada para {mascota.nombre}"

class EstrategiaLimpiezaDental(EstrategiaServicio):
    def ejecutar(self, mascota):
        return f"Limpieza dental realizada a {mascota.nombre}"

class ContextoServicio:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia
    
    def establecer_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def ejecutar_servicio(self, mascota):
        if self.estrategia:
            return self.estrategia.ejecutar(mascota)
        else:
            return "No se ha establecido una estrategia de servicio"