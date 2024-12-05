import os
import pandas as pd

pd.set_option('display.max_rows', None)  # Muestra todas las filas
pd.set_option('display.max_columns', None)  # Muestra todas las columnas

class PailaSalud:
    def __init__(self, contrasena_admin):
        self.usuarios = {}                          # Almacena informacion de los usuarios
        self.citas = {}                             # Almacena las citas programadas
        self.atenciones = []                        # Lista para registrar atenciones
        self.procesos = []                          # Lista para registrar procesos
        self.contrasena_admin = contrasena_admin

    def limpiar_consola(self):
        """
            Funcion para limpiar la consola, se valida usando (os) si el sistema es windows o linux.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def agregar_usuario(self, cedula, nombre, edad, prioridad):
        """
            Funcion para agregar los usuarios al sistema, dentro del self.usuarios que es un atributo de
            la clase PailaSalud, servira como una base de datos.

            Estructura:
                {
                    "cedula_1": {
                        "nombre": "nombre_1",
                        "edad": "edad_1",
                        "prioridad": "prioridad_1"
                    },
                    "cedula_2": {
                        "nombre": "nombre_2",
                        "edad": "edad_2",
                        "prioridad": "prioridad_2"
                    }                
                }
        """
        if cedula in self.usuarios:
            print(f"\nEl usuario con cedula: {cedula} -> Ya esta registrado.")
        else:
            self.usuarios[cedula] = {
                "nombre": nombre,
                "edad": edad,
                "prioridad": prioridad,
            }
            print(f"\nUsuario {nombre} con Cedula {cedula} agregado correctamente al sistema.")

    def agregar_cita(self, cedula, fecha, hora, tipo_cita, medico):
        """
            Funcion para agregar los citas al sistema, dentro del self.citas que es un atributo de
            la clase PailaSalud, servira como una base de datos.

            Estructura:
                {
                    "cedula_1": {
                        "fecha": fecha,
                        "hora": hora,
                        "tipo_cita": tipo_cita,
                        "medico": medico,
                        "confirmada": False,
                    },
                    "cedula_2": {
                        "fecha": fecha,
                        "hora": hora,
                        "tipo_cita": tipo_cita,
                        "medico": medico,
                        "confirmada": False,
                    }                
                }
        """
        if cedula not in self.usuarios:
            print(f"\nNo se puede agregar cita: El usuario con cedula {cedula} no esta registrado en la EPS Paila Salud.")
            return

        if cedula in self.citas:
            print(f"\nEl usuario con cedula {cedula} ya tiene una cita programada.")
        else:
            self.citas[cedula] = {
                "fecha": fecha,
                "hora": hora,
                "tipo_cita": tipo_cita,
                "medico": medico,
                "confirmada": False,
            }
            print(f"\nCita agregada correctamente para el usuario {self.usuarios[cedula]["nombre"]} con cedula: {cedula}.")

    def confirmar_cita(self, cedula):
        """
            Funcion confirmar una cita, dentro del self.citas se busca la cita usando la cedula
            Luego de encontrarla se actualiza el atributo booleano (confirmada) a True.

            Estructura:
                {
                    "cedula_1": {
                        "fecha": fecha,
                        "hora": hora,
                        "tipo_cita": tipo_cita,
                        "medico": medico,
                        "confirmada": False,   <--- Cambia este atributo a True
                    }              
                }
        """

        if cedula not in self.citas:
            print(f"\nNo se puede confirmar: El usuario con cedula {cedula} no tiene citas programadas.")
        else:
            self.citas[cedula]["confirmada"] = True
            print(f"\nLa cita del usuario {self.usuarios[cedula]["nombre"]} y cedula {cedula} ha sido confirmada.")

    def consultar_cita(self, cedula):
        """ 
            Funcion consultar una cita por cedula del usuario.
            Cuando se consulta se agrega el proceso de atencion, como consulta de cita.
        """

        if cedula in self.citas:
            cita = self.citas[cedula]
            usuario = self.usuarios[cedula]
            print(f"Datos de la cita para {usuario["nombre"]}:")
            print(
                f"* Fecha: {cita["fecha"]} | Hora: {cita["hora"]} | Tipo: {cita["tipo_cita"]} | Medico: {cita["medico"]} | Estado: {cita["confirmada"]}"
            )
            self.atenciones.append({"cedula": cedula, "proceso": "Consulta de cita"})
        else:
            print(f"No hay cita registrada para el usuario con cedula: {cedula}.")

    def administrador(self):
        """
        Funcion para construir el menu de administrador, en esta se usan las funciones de limpiar consolar
        y se genera un ciclo infinito para que se permanezca en el menu hasta que el usuario decida salir
        de este.
        """
        self.limpiar_consola()
        constrasena = input("Ingrese la contraseña de administrador: ")
        if constrasena != self.contrasena_admin:
            print("Contraseña incorrecta.")
            return

        while True:
            self.limpiar_consola()
            print("\n--- MENU ADMINISTRADOR ---")
            print("1. Imprimir reporte de datos")
            print("2. Salir al menu anterior")
            print("3. Salir completamente y generar reportes")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.generar_reporte()
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                break
            elif opcion == "3":
                self.generar_reporte()
                print("Saliendo del sistema...")
                exit()
            else:
                print("Opcion no valida.")
                input("\nPresione Enter para continuar...")

    def generar_reporte(self):
        """
            Funcion para generar reportes, en esta se usan dataFrames de Pandas
            para visualizar los datos de las atenciones y las citas.
            Se guarda la accion de generar reporte como un proceso.
        """
        citas_data = []
        atenciones_df = pd.DataFrame(self.atenciones)

        for cedula, cita in self.citas.items():
            cita_data = {"cedula": cedula, **cita}
            citas_data.append(cita_data)

        citas_df = pd.DataFrame(citas_data)

        print("\n--- Reporte de Atenciones ---")
        if not atenciones_df.empty:       # Los dataFrames tienen propiedades, una de ellas es empty, ayuda a saber si un DataFrame esta vacio.
            print(atenciones_df)
        else:
            print("No hay atenciones registradas.")
        
        print("\n--- Reporte de Citas ---")
        if not citas_df.empty:    
            print(citas_df)
        else:
            print("No hay citas registradas.")
        
        self.procesos.append("Generar reporte")

    def menu_principal(self):
        """
        Funcion para crear el menu principal, con opciones adicionales para crear usuarios y crear citas.
        """
        while True:
            self.limpiar_consola()
            print("\n---- BIENVENIDO A PAILA SALUD ----")
            print("\n1. Consultar cita por cedula")
            print("2. Confirmar cita por cedula")
            print("3. Crear usuario")
            print("4. Crear cita para usuario")
            print("5. Ingresar al menu administrador")
            print("6. Salir")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.limpiar_consola()
                try:
                    cedula = int(input("Ingrese su cedula: "))
                    self.consultar_cita(cedula)
                except ValueError:
                    print("La cedula debe ser un numero.")
                input("\nPresione Enter para continuar ...")

            elif opcion == "2":
                self.limpiar_consola()
                try:
                    cedula = int(input("Ingrese su cedula: "))
                    self.confirmar_cita(cedula)
                except ValueError:
                    print("La cedula debe ser un numero.")
                input("\nPresione Enter para continuar ...")

            elif opcion == "3":
                self.limpiar_consola()
                try:
                    cedula = int(input("Ingrese la cedula del usuario: "))
                    nombre = input("Ingrese el nombre del usuario: ").strip()
                    edad = int(input("Ingrese la edad del usuario: "))
                    prioridad = input("Ingrese la prioridad del usuario (Alta, Media, Baja): ").strip().capitalize()
                    if prioridad not in ["Alta", "Media", "Baja"]:
                        print("Prioridad no válida. Intente nuevamente.")
                    else:
                        self.agregar_usuario(cedula, nombre, edad, prioridad)
                except ValueError:
                    print("Los valores ingresados son incorrectos. Intente nuevamente.")
                input("\nPresione Enter para continuar ...")

            elif opcion == "4":
                self.limpiar_consola()
                try:
                    cedula = int(input("Ingrese la cedula del usuario para la cita: "))
                    if cedula not in self.usuarios:
                        print(f"El usuario con cedula {cedula} no está registrado. Primero debe crear el usuario.")
                    else:
                        fecha = input("Ingrese la fecha de la cita (YYYY-MM-DD): ").strip()
                        hora = input("Ingrese la hora de la cita (HH:MM AM/PM): ").strip()
                        tipo_cita = input("Ingrese el tipo de cita (Ej. Consulta General, Odontologia): ").strip()
                        medico = input("Ingrese el nombre del medico: ").strip()
                        self.agregar_cita(cedula, fecha, hora, tipo_cita, medico)
                except ValueError:
                    print("Los valores ingresados son incorrectos. Intente nuevamente.")
                input("\nPresione Enter para continuar ...")

            elif opcion == "5":
                self.administrador()

            elif opcion == "6":
                print("Saliendo del sistema ... ¡Hasta pronto!")
                break

            else:
                print("Opcion no válida.")
                input("\nPresione Enter para continuar ...")
