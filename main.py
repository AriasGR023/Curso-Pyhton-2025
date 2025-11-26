from mascotas import FabricaMascotas
from clientes import GestionClientes
from servicios import *

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("       SISTEMA VETERINARIO CON PATRONES")
    print("="*50)
    print("1. 🧍 Agregar cliente")
    print("2. 🐕 Agregar mascota a cliente")
    print("3. 📋 Listar todos los clientes y mascotas")
    print("4. 🏥 Realizar servicio veterinario")
    print("5. 🔍 Buscar cliente por nombre")
    print("6. 📊 Mostrar estadísticas")
    print("7. 🚪 Salir")
    print("="*50)

def main():
    # Inicializar sistemas con patrones
    gestion_clientes = GestionClientes()
    sistema_notificaciones = SistemaNotificaciones()
    
    # Agregar observadores (Patrón Observer)
    sistema_notificaciones.agregar_observador(NotificacionEmail())
    sistema_notificaciones.agregar_observador(NotificacionSMS())
    sistema_notificaciones.agregar_observador(NotificacionApp())
    
    # Contexto para servicios (Patrón Strategy)
    contexto_servicio = ContextoServicio()
    
    print("¡Bienvenido al Sistema Veterinario!")
    print("Este sistema utiliza patrones de diseño:")
    print("- Factory Method para crear mascotas")
    print("- Singleton para gestionar clientes")
    print("- Observer para notificaciones")
    print("- Strategy para servicios veterinarios")
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            # Agregar cliente
            print("\n--- AGREGAR NUEVO CLIENTE ---")
            nombre = input("Nombre del cliente: ").strip()
            telefono = input("Teléfono: ").strip()
            email = input("Email: ").strip()
            
            if nombre and telefono and email:
                cliente = gestion_clientes.agregar_cliente(nombre, telefono, email)
                print(f"Cliente '{cliente['nombre']}' agregado exitosamente (ID: {cliente['id']})")
                
                # Notificar a todos los observadores
                mensaje = f"Nuevo cliente registrado: {nombre}"
                notificaciones = sistema_notificaciones.notificar_todos(mensaje)
                for notif in notificaciones:
                    print(f" {notif}")
            else:
                print("Error: Todos los campos son obligatorios")
                
        elif opcion == "2":
            # Agregar mascota
            print("\n--- AGREGAR MASCOTA A CLIENTE ---")
            
            if gestion_clientes.obtener_total_clientes() == 0:
                print("No hay clientes registrados. Primero agregue un cliente.")
                continue
            
            try:
                id_cliente = int(input("ID del cliente: ").strip())
                cliente = gestion_clientes.buscar_cliente(id_cliente)
                
                if not cliente:
                    print("Cliente no encontrado")
                    continue
                
                print(f"Cliente: {cliente['nombre']}")
                tipo = input("Tipo de mascota (perro/gato/ave): ").strip().lower()
                nombre_mascota = input("Nombre de la mascota: ").strip()
                edad = int(input("Edad en años: ").strip())
                raza = input("Raza (opcional): ").strip() or "Desconocida"
                
                # Usar Factory Method para crear mascota
                fabrica = FabricaMascotas()
                mascota = fabrica.crear_mascota(tipo, nombre_mascota, edad, raza)
                
                if gestion_clientes.agregar_mascota_cliente(id_cliente, mascota):
                    print(f"Mascota '{nombre_mascota}' agregada exitosamente a {cliente['nombre']}")
                else:
                    print("Error al agregar mascota")
                    
            except ValueError:
                print("Error: ID y edad deben ser números")
                
        elif opcion == "3":
            # Listar clientes y mascotas
            print("\n--- LISTA DE CLIENTES Y MASCOTAS ---")
            
            clientes = gestion_clientes.listar_clientes()
            if not clientes:
                print("📭 No hay clientes registrados")
            else:
                for cliente in clientes:
                    print(f"\n🧍 CLIENTE ID: {cliente['id']}")
                    print(f"   Nombre: {cliente['nombre']}")
                    print(f"   Teléfono: {cliente['telefono']}")
                    print(f"   Email: {cliente['email']}")
                    print(f"   Mascotas: {len(cliente['mascotas'])}")
                    
                    if cliente['mascotas']:
                        for i, mascota in enumerate(cliente['mascotas'], 1):
                            print(f"   {i}. {mascota.mostrar_info()}")
                    else:
                        print("   🐾 No tiene mascotas registradas")
        
        elif opcion == "4":
            # Realizar servicio veterinario
            print("\n--- SERVICIO VETERINARIO ---")
            
            if gestion_clientes.obtener_total_clientes() == 0:
                print("No hay clientes registrados")
                continue
            
            try:
                id_cliente = int(input("ID del cliente: ").strip())
                cliente = gestion_clientes.buscar_cliente(id_cliente)
                
                if not cliente or not cliente['mascotas']:
                    print("Cliente no encontrado o no tiene mascotas")
                    continue
                
                print(f"\nMascotas de {cliente['nombre']}:")
                for i, mascota in enumerate(cliente['mascotas'], 1):
                    print(f"{i}. {mascota.mostrar_info()}")
                
                idx_mascota = int(input("Seleccione el número de la mascota: ").strip()) - 1
                
                if 0 <= idx_mascota < len(cliente['mascotas']):
                    mascota = cliente['mascotas'][idx_mascota]
                    
                    print("\nServicios disponibles:")
                    print("1. Vacunación")
                    print("2. Consulta general")
                    print("3. Desparasitación")
                    print("4. Limpieza dental")
                    print("5. Cirugía")
                    
                    servicio_opcion = input("Seleccione el servicio (1-5): ").strip()
                    
                    # Configurar estrategia según selección
                    if servicio_opcion == "1":
                        contexto_servicio.establecer_estrategia(EstrategiaVacunacion())
                    elif servicio_opcion == "2":
                        contexto_servicio.establecer_estrategia(EstrategiaConsultaGeneral())
                    elif servicio_opcion == "3":
                        contexto_servicio.establecer_estrategia(EstrategiaDesparasitacion())
                    elif servicio_opcion == "4":
                        contexto_servicio.establecer_estrategia(EstrategiaLimpiezaDental())
                    elif servicio_opcion == "5":
                        contexto_servicio.establecer_estrategia(EstrategiaCirugia())
                    else:
                        print("Servicio no válido")
                        continue
                    
                    # Ejecutar servicio con Strategy pattern
                    resultado = contexto_servicio.ejecutar_servicio(mascota)
                    print(f" {resultado}")
                    
                    # Notificar
                    mensaje = f"Servicio realizado: {type(contexto_servicio.estrategia).__name__} para {mascota.nombre}"
                    sistema_notificaciones.notificar_todos(mensaje)
                    
                else:
                    print(" Número de mascota no válido")
                    
            except (ValueError, IndexError):
                print(" Error en la selección")
        
        elif opcion == "5":
            # Buscar cliente por nombre
            print("\n--- BUSCAR CLIENTE ---")
            nombre_buscar = input("Nombre del cliente a buscar: ").strip()
            cliente = gestion_clientes.buscar_cliente_por_nombre(nombre_buscar)
            
            if cliente:
                print(f"✅ Cliente encontrado:")
                print(f"   ID: {cliente['id']}")
                print(f"   Nombre: {cliente['nombre']}")
                print(f"   Teléfono: {cliente['telefono']}")
                print(f"   Email: {cliente['email']}")
                print(f"   Mascotas: {len(cliente['mascotas'])}")
            else:
                print(" Cliente no encontrado")
        
        elif opcion == "6":
            # Mostrar estadísticas
            print("\n--- ESTADÍSTICAS DEL SISTEMA ---")
            total_clientes = gestion_clientes.obtener_total_clientes()
            print(f"Total de clientes: {total_clientes}")
            
            if total_clientes > 0:
                total_mascotas = 0
                for cliente in gestion_clientes.listar_clientes():
                    total_mascotas += len(cliente['mascotas'])
                print(f"🐾 Total de mascotas: {total_mascotas}")
                print(f"Promedio de mascotas por cliente: {total_mascotas/total_clientes:.1f}")
        
        elif opcion == "7":
            print("\n¡Gracias por usar el Sistema Veterinario!")
            print("Hasta pronto! ")
            break
        
        else:
            print(" Opción no válida. Por favor, seleccione 1-7")

if __name__ == "__main__":
    main()