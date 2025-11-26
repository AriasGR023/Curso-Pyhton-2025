# Patrón Singleton para gestionar clientes
class GestionClientes:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.clientes = []
            cls._instancia.contador_id = 1
        return cls._instancia
    
    def agregar_cliente(self, nombre, telefono, email):
        cliente = {
            'id': self.contador_id,
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'mascotas': []
        }
        self.clientes.append(cliente)
        self.contador_id += 1
        return cliente
    
    def buscar_cliente(self, id_cliente):
        for cliente in self.clientes:
            if cliente['id'] == id_cliente:
                return cliente
        return None
    
    def buscar_cliente_por_nombre(self, nombre):
        for cliente in self.clientes:
            if cliente['nombre'].lower() == nombre.lower():
                return cliente
        return None
    
    def listar_clientes(self):
        return self.clientes.copy()
    
    def agregar_mascota_cliente(self, id_cliente, mascota):
        cliente = self.buscar_cliente(id_cliente)
        if cliente:
            cliente['mascotas'].append(mascota)
            return True
        return False
    
    def obtener_total_clientes(self):
        return len(self.clientes)