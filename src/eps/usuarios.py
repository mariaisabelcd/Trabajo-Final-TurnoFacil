import random

def generar_usuario():
    """Genera un usuario con datos aleatorios."""
    nombres = [
        "Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Manuel", "Carmen", "Johan", "Nora",
        "Jorge", "Mayra", "Francisco", "Elena", "Raúl", "Isabella", "Miguel", "Leidy", "Fernando",
    ]
    apellidos = [
        "Perez", "Lopez", "Ospina", "Hernandez", "Cañas", "Garcia", "Duque", "Sanchez", "Ramirez", "Torres",
        "Aristizabal", "Morales", "Rivera", "Jiménez", "Rojas", "Vargas", "Castro", "Ortiz"
    ]
    edades = range(18, 70)
    prioridades = ["Alta", "Media", "Baja"]

    cedula = random.randint(100000, 999999)
    nombre_completo = f"{random.choice(nombres)} {random.choice(apellidos)}"
    edad = random.choice(edades)
    prioridad = random.choice(prioridades)

    return cedula, nombre_completo, edad, prioridad

def generar_cita(cedula):
    """Genera una cita aleatoria para un usuario existente."""

    fechas = ["2024-12-05", "2024-12-06", "2024-12-07", "2024-12-08", "2024-12-09", "2024-12-10"]
    horas = ["10:30 AM", "2:00 PM", "4:00 PM", "8:30 AM", "9:00 AM"]
    tipos_cita = ["Consulta General", "Pediatría", "Odontología", "Cardiología"]
    medicos = ["Dr. Ospina", "Dra. Cañas", "Dr. Hincapie", "Dra. Duque"]

    fecha = random.choice(fechas)
    hora = random.choice(horas)
    tipo_cita = random.choice(tipos_cita)
    medico = random.choice(medicos)

    return cedula, fecha, hora, tipo_cita, medico

def llenar_datos(paila_salud, numero_usuarios, numero_citas):
    """Llena el sistema con datos aleatorios."""

    usuarios = []
    for _ in range(numero_usuarios):
        cedula, nombre, edad, prioridad = generar_usuario()
        usuarios.append(cedula)
        paila_salud.agregar_usuario(cedula, nombre, edad, prioridad)

    for _ in range(min(numero_citas, len(usuarios))):  # Evitar más citas que usuarios disponibles
        cedula = random.choice(usuarios)
        _, fecha, hora, tipo_cita, medico = generar_cita(cedula)
        paila_salud.agregar_cita(cedula, fecha, hora, tipo_cita, medico)
        usuarios.remove(cedula)
