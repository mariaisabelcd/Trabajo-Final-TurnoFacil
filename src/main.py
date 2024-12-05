from eps.sistema import PailaSalud
from eps.usuarios import llenar_datos

# Se instancia la clase PailaSalud y se le da la contraseña de Administrador
paila_salud = PailaSalud(contrasena_admin="paila123")

# Llenar mas usuarios de forma aleatorea
llenar_datos(paila_salud, 100, 100)

# Agregar usuarios manuales
paila_salud.agregar_usuario(110023, "Antonio Osorio", 50, "Alta")
paila_salud.agregar_usuario(110023, "Ana Murillo", 23, "Baja")

# Agregar citas manuales
paila_salud.agregar_cita(110023, "2024-12-05", "10:30 AM", "Consulta General", "Dr. Ramírez")
paila_salud.agregar_cita(110023, "2024-12-06", "2:00 PM", "Pediatría", "Dra. Gómez")


# Ejecutar menú principal
paila_salud.menu_principal()
