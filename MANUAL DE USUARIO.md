### **Manual de Usuario: Sistema de Gestión de Citas - Paila Salud**

Bienvenido al sistema de gestión de citas de *Paila Salud*. Este software permite gestionar citas de manera ágil y eficiente para los usuarios de la EPS, asegurando un proceso organizado y sin complicaciones.

---

### **1. Instalación**
Antes de comenzar, asegúrese de que su entorno cumple con los requisitos necesarios. 

1. **Requisitos previos:**
   - Tener Python instalado en su equipo.
   - Instalar la biblioteca `pandas`.

2. **Comandos de instalación:**
   - Abra la terminal y ejecute:
     ```bash
     pip install pandas
     python .\EPS\main.py
     ```

Una vez instaladas las dependencias y ejecutado el programa, estará listo para utilizar el sistema.

---

### **2. Contenido del Sistema**
Al ejecutar el programa, accederá al menú principal de *Paila Salud*. Este menú le permitirá realizar las siguientes acciones:

#### **Menú Principal**
1. **Consultar cita por cédula:**  
   Ingrese la cédula del usuario para verificar si tiene una cita registrada.

2. **Confirmar cita por cédula:**  
   Ingrese la cédula del usuario para confirmar una cita previamente registrada.

3. **Crear usuario:**  
   Registre un nuevo usuario proporcionando:
   - Cédula.
   - Nombre.
   - Edad.
   - Prioridad de la cita (*Alta, Media, Baja*).  
   Esto permitirá realizar consultas y confirmaciones de citas para el usuario.

4. **Crear cita para usuario:**  
   Registre una nueva cita para un usuario ya existente proporcionando:
   - Cédula.
   - Fecha y hora de la cita.
   - Tipo de cita.
   - Nombre del médico.  
   Las citas registradas podrán ser consultadas y confirmadas mediante las opciones 1 y 2 del menú principal.

5. **Ingresar al menú administrador:**  
   Ingrese como administrador utilizando la contraseña predeterminada `paila123`. Desde este menú podrá:
   - **Imprimir reporte de datos:** Generar un informe detallado de los usuarios y sus citas, incluyendo:
     - Datos personales.
     - Información de citas (fecha, hora, tipo de cita, médico asignado y estado de confirmación).
   - **Salir al menú anterior:** Regresar al menú principal.
   - **Salir completamente y generar reportes:** Cerrar el programa y generar un reporte final.

6. **Salir:**  
   Finalice la sesión del programa.

---

### **3. Descripción de Funcionalidades**
#### **Consultar cita por cédula**
- Introduzca el número de cédula para verificar si hay citas registradas para el usuario. 

#### **Confirmar cita por cédula**
- Introduzca el número de cédula para confirmar una cita existente en el sistema.

#### **Crear usuario**
- Proporcione los datos básicos del paciente:
  - Cédula.
  - Nombre.
  - Edad.
  - Prioridad (*Alta, Media o Baja*).
- Una vez registrado, el usuario podrá programar citas.

#### **Crear cita para usuario**
- Registre una cita ingresando:
  - Cédula del usuario.
  - Fecha y hora deseadas.
  - Tipo de cita.
  - Médico asignado.  
  Asegúrese de que el usuario esté registrado previamente.

#### **Menú Administrador**
El acceso a este menú está protegido por contraseña (`paila123`). Desde aquí podrá:
1. **Imprimir reporte de datos:**  
   Obtenga un informe detallado de todas las citas registradas, incluyendo información como:
   - Cédula del usuario.
   - Fecha, hora, tipo de cita, médico asignado.
   - Estado de la cita (confirmada o no).

2. **Salir al menú anterior:**  
   Regrese al menú principal sin cerrar el programa.

3. **Salir completamente y generar reportes:**  
   Cierre el programa y genere un informe final de usuarios y citas.

---

### **4. Uso del Sistema**
El sistema ha sido diseñado para ser intuitivo, ofreciendo una gestión eficiente de citas para la EPS. Siga los pasos descritos en cada opción del menú para garantizar una experiencia sin complicaciones.

**Nota:**  
La contraseña del administrador es *paila123*. Manténgala en un lugar seguro para evitar accesos no autorizados.

---

### **5. Beneficios del Sistema**
- Gestión centralizada de citas.
- Confirmaciones rápidas y sencillas.
- Reportes detallados para seguimiento.
- Optimización de procesos administrativos en la EPS.

---

Para más información, contacte con los desarrolladores o soporte técnico. ¡Gracias por usar *Paila Salud*!

## Autores

- Juan Manuel Ospina Hincapié
- Maria Isabel Cañas Duque
