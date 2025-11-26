import unittest
from mascotas import FabricaMascotas, Mascota, Perro, Gato, Ave
from clientes import GestionClientes
from servicios import *

class TestVeterinaria(unittest.TestCase):
    
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.fabrica = FabricaMascotas()
        self.gestion = GestionClientes()
    
    def test_1_fabrica_crea_perro_correctamente(self):
        """Prueba 1: Factory Method crea perro correctamente"""
        print("🧪 Probando Factory Method para perros...")
        perro = self.fabrica.crear_mascota("perro", "Max", 3, "Labrador")
        
        self.assertIsInstance(perro, Perro)
        self.assertEqual(perro.nombre, "Max")
        self.assertEqual(perro.edad, 3)
        self.assertEqual(perro.raza, "Labrador")
        self.assertEqual(perro.ladrar(), "¡Guau guau!")
        print("✅ Prueba 1 PASADA: Factory crea perros correctamente")
    
    def test_2_fabrica_crea_gato_correctamente(self):
        """Prueba 2: Factory Method crea gato correctamente"""
        print("🧪 Probando Factory Method para gatos...")
        gato = self.fabrica.crear_mascota("gato", "Luna", 2, "Siamés")
        
        self.assertIsInstance(gato, Gato)
        self.assertEqual(gato.nombre, "Luna")
        self.assertEqual(gato.tipo, "Gato")
        self.assertEqual(gato.maullar(), "¡Miau miau!")
        print("✅ Prueba 2 PASADA: Factory crea gatos correctamente")
    
    def test_3_singleton_funciona_correctamente(self):
        """Prueba 3: Singleton retorna la misma instancia"""
        print("🧪 Probando patrón Singleton...")
        gestion1 = GestionClientes()
        gestion2 = GestionClientes()
        
        self.assertIs(gestion1, gestion2)
        
        # Verificar que comparten el mismo estado
        gestion1.agregar_cliente("Test", "123", "test@test.com")
        self.assertEqual(len(gestion2.listar_clientes()), 1)
        print("✅ Prueba 3 PASADA: Singleton funciona correctamente")
    
    def test_4_gestion_clientes_agrega_y_busca(self):
        """Prueba 4: Se pueden agregar y buscar clientes"""
        print("🧪 Probando gestión de clientes...")
        cliente = self.gestion.agregar_cliente("María García", "555-1234", "maria@email.com")
        
        self.assertEqual(cliente['nombre'], "María García")
        self.assertEqual(cliente['telefono'], "555-1234")
        
        # Buscar por ID
        cliente_encontrado = self.gestion.buscar_cliente(1)
        self.assertEqual(cliente_encontrado['nombre'], "María García")
        
        # Buscar por nombre
        cliente_por_nombre = self.gestion.buscar_cliente_por_nombre("María García")
        self.assertEqual(cliente_por_nombre['email'], "maria@email.com")
        print("✅ Prueba 4 PASADA: Clientes se agregan y buscan correctamente")
    
    def test_5_strategy_vacunacion_funciona(self):
        """Prueba 5: Strategy pattern para vacunación funciona"""
        print("🧪 Probando Strategy pattern para vacunación...")
        mascota = Mascota("Rocky", 4, "Perro")
        estrategia = EstrategiaVacunacion()
        contexto = ContextoServicio(estrategia)
        
        # Verificar que no está vacunada inicialmente
        self.assertFalse(mascota.vacunada)
        
        # Ejecutar estrategia
        resultado = contexto.ejecutar_servicio(mascota)
        
        # Verificar que ahora está vacunada
        self.assertTrue(mascota.vacunada)
        self.assertIn("vacunado", resultado)
        print("✅ Prueba 5 PASADA: Strategy de vacunación funciona correctamente")
    
    def test_6_observer_notificaciones_funciona(self):
        """Prueba 6: Observer pattern para notificaciones funciona"""
        print("🧪 Probando Observer pattern para notificaciones...")
        sistema = SistemaNotificaciones()
        email_observer = NotificacionEmail()
        sms_observer = NotificacionSMS()
        
        # Agregar observadores
        sistema.agregar_observador(email_observer)
        sistema.agregar_observador(sms_observer)
        
        # Notificar a todos
        mensaje = "Mensaje de prueba del sistema"
        resultados = sistema.notificar_todos(mensaje)
        
        # Verificar que ambos observadores recibieron el mensaje
        self.assertEqual(len(resultados), 2)
        self.assertIn("EMAIL", resultados[0])
        self.assertIn("SMS", resultados[1])
        self.assertIn(mensaje, resultados[0])
        self.assertIn(mensaje, resultados[1])
        print("✅ Prueba 6 PASADA: Observer envía notificaciones correctamente")
    
    def test_7_agregar_mascota_a_cliente(self):
        """Prueba adicional: Agregar mascota a cliente"""
        print("🧪 Probando agregar mascota a cliente...")
        cliente = self.gestion.agregar_cliente("Juan Pérez", "555-5678", "juan@email.com")
        perro = self.fabrica.crear_mascota("perro", "Buddy", 2, "Golden Retriever")
        
        resultado = self.gestion.agregar_mascota_cliente(cliente['id'], perro)
        
        self.assertTrue(resultado)
        cliente_actualizado = self.gestion.buscar_cliente(cliente['id'])
        self.assertEqual(len(cliente_actualizado['mascotas']), 1)
        self.assertEqual(cliente_actualizado['mascotas'][0].nombre, "Buddy")
        print("✅ Prueba 7 PASADA: Mascota se agrega a cliente correctamente")

def ejecutar_pruebas():
    """Función para ejecutar todas las pruebas"""
    print("🚀 INICIANDO PRUEBAS UNITARIAS")
    print("=" * 50)
    
    # Crear test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVeterinaria)
    
    # Ejecutar pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    print("=" * 50)
    print("📊 RESUMEN DE PRUEBAS:")
    print(f"Pruebas ejecutadas: {resultado.testsRun}")
    print(f"Pruebas exitosas: {resultado.testsRun - len(resultado.failures) - len(resultado.errors)}")
    print(f"Pruebas fallidas: {len(resultado.failures)}")
    print(f"Errores: {len(resultado.errors)}")
    
    if resultado.wasSuccessful():
        print("🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
    else:
        print("❌ Algunas pruebas fallaron")

if __name__ == '__main__':
    ejecutar_pruebas()