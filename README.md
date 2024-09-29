<div align="center">
<table>
    <thead>
        <tr>
            <td rowspan="3">
                <img alt="TurnoFácil" height="200px" src="https://raw.githubusercontent.com/mariaisabelcd/Trabajo-Final/refs/heads/main/images/logo%20turnof%C3%A1cil.png" hspace="10px" vspace="0px">
            </td>
            <td align="center">
                <h1><b>Software TurnoFácil</b></h1>
            </td>
        </tr>
        <tr>
            <td align="center">
                <h2><b>Optimizando la gestión de turnos en EPS PailaSalud</b></h2>
            </td>
        </tr>
    </thead>
</table>
</div>


<div align="right">
<h2> <b> Por: María Isabel Cañas Duque </b> </h2>
<p> Estudiante de quinto semestre de Ingeniería Industrial. Soy una persona comprometida y proactiva, con una fuerte orientación hacia la mejora continua y la eficiencia en todo lo que hago. Además, soy adaptable y siempre busco aprender y crecer en cada desafío que enfrento, lo que me permite aportar soluciones innovadoras y trabajar de manera colaborativa en equipo. </p>
<a href="mailto:maria.canasd@udea.edu.co"> ✉ María Isabel Cañas Duque </a>

<h2> <b> Por: Juan Manuel Ospina Hincapié </b> </h2>
<p> Estudiante de Séptimo semestre de Ingeniería Industrial con habilidades destacadas en creatividad e iniciativa, liderazgo y conocimientos tecnológicos, además con fortalezas en capacidad analítica, adaptable a diferentes situaciones y objetivo en la toma de decisiones. </p>
<a href="mailto:juan.ospina27@udea.edu.co"> ✉ Juan Manuel Ospina Hincapié </a>

<h2> <b> Por: Sandra Julieth Sandoval López </b> </h2>
<p> Estudiante de cuarto semestre de ingeniería industrial. Dentro de mis fortalezas destaco la resolución de problemas y la creatividad a la hora de buscar soluciones; y destaco habilidades como mi capacidad de aprendizaje y trabajo en equipo. </p>
<a href="mailto:julieth.sandoval@udea.edu.co"> ✉ Sandra Julieth Sandoval López </a>

</div>

<br>

# **Detalles del proyecto**
El software TurnoFácil es una solución diseñada para la EPS PailaSalud con el fin de optimizar la gestión de turnos y la atención de pacientes, superando las limitaciones del proceso manual actual. El sistema organiza y gestiona la llegada de los pacientes, basándose en las citas programadas previamente por el sistema de la EPS, asegurando una atención más fluida y priorizada.

TurnoFácil mejora el rendimiento del servicio, disminuyendo tiempos de espera innecesarios y garantizando un seguimiento claro del recorrido de cada paciente a través de la atención médica. Los datos se registran de manera eficiente en un archivo CSV, utilizando Python para su procesamiento, lo que facilita la gestión, archivo y exportación de información relevante.

Este programa será un recurso fundamental para optimizar la experiencia del usuario, tanto para los pacientes como para el personal de la EPS, reduciendo la carga administrativa y aumentando la satisfacción en la atención.

<div align="center">
    <img alt="Imagen representativa del proyecto" height="300px" src="https://raw.githubusercontent.com/mariaisabelcd/Trabajo-Final/refs/heads/main/images/atenci%C3%B3n%20turnof%C3%A1cil.jpg" hspace="10px" vspace="0px">
</div>

# **Licencia del software**
<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><span property="dct:title">Software TurnoFácil</span> by <span property="cc:attributionName">María Cañas, Juan Ospina & Julieth Sandoval</span> is licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" alt=""><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" alt=""></a></p>

# **Reporte de visión**

## *Objetivos*
- Automatizar el proceso de asignación y seguimiento de turnos.
- Asegurar un flujo adecuado en la atención, priorizando citas programadas.
- Disminuir el tiempo que los pacientes pasan esperando ser atendidos.
- Minimizar la carga administrativa del personal de la EPS.
- Utilizar un sistema para el registro y archivo de información de pacientes.
- Generar informes sobre la gestión de turnos y la atención al paciente.
- Mejorar la experiencia de pacientes y personal a través de un sistema más fluido.

## *Beneficios*
- Optimización en el uso de recursos y tiempo.
- Facilitar la comunicación entre pacientes y personal médico.
- Minimizar errores en la asignación de turnos y la gestión de citas.
- Acceso rápido y organizado a los datos de los pacientes.
- Mejora en la percepción del servicio por parte de los usuarios.
- Posibilidad de ajustar y modificar turnos en tiempo real según necesidades.


# **Especificación de requisitos**

## *Requisitos funcionales*
•	El programa permitirá que los pacientes consulten el día, la hora, el médico asignado y el tipo de consulta.
•	Los pacientes deben poder usar la plataforma para confirmar su asistencia a la cita y el administrador del sistema podrá ver si la cita ha sido confirmada o no.
•	El sistema debe permitir al administrador generar reportes de citas confirmadas y no confirmadas en formato CSV. Y la información debe permitirse exportar en dicho formato.
•	El sistema deberá tener un menú al que solo los administradores podrán acceder a través de una contraseña, lo que les permitirá realizar acciones como consultar citas, reportar atenciones y administrar la base de datos de pacientes.
•	Cada operación que realiza el sistema debe registrarse en un log de eventos, que incluya el tiempo de ejecución y las acciones realizadas.
•	El programa debe permitir que los usuarios se identifiquen introduciendo su número de identificación.

## *Requisitos no funcionales*
•	El sistema debe poder manejar varias solicitudes de consulta y confirmación de citas al mismo tiempo sin disminuir el tiempo de respuesta.
•	Los datos de los pacientes, especialmente los datos personales y médicos, deben estar protegidos. Para esto, se deberá usar una contraseña para evitar el acceso a las funciones administrativas.
•	La interfaz debe ser fácil de usar para personas sin experiencia técnica, con menús simples y opciones para interactuar con el sistema.
•	El programa debe ser compatible con varios sistemas operativos, como Windows, Linux y MacOS.
•	El sistema debe garantizar una alta disponibilidad y precisión en el manejo de datos de citas, minimizando fallas o pérdidas de información.
•	Para facilitar futuras actualizaciones y correcciones de errores, el código debe estar bien documentado y estructurado.
•	el sistema debe poder manejar errores de manera eficiente, registrar problemas en los registros y garantizar la integridad de los datos en caso de fallos inesperados.

# **Plan de proyecto**

dict(Tarea="Reunión inicial y asignación de responsabilidades", FechaInicio='2024-09-29', FechaFin='2024-10-01', Responsable="Juan, María, Julieth"),
dict(Tarea="Definición de requisitos del software", FechaInicio='2024-10-02', FechaFin='2024-10-05', Responsable="María"),
dict(Tarea="Diseño de la arquitectura del software", FechaInicio='2024-10-06', FechaFin='2024-10-10', Responsable="Juan"),
dict(Tarea="Desarrollo del módulo de gestión de citas", FechaInicio='2024-10-11', FechaFin='2024-10-18', Responsable="Julieth"),
dict(Tarea="Desarrollo del módulo de atención de pacientes", FechaInicio='2024-10-19', FechaFin='2024-10-26', Responsable="María"),
dict(Tarea="Integración de módulos y pruebas iniciales", FechaInicio='2024-10-27', FechaFin='2024-11-02', Responsable="Juan, María, Julieth"),
dict(Tarea="Revisión del código y corrección de errores", FechaInicio='2024-11-03', FechaFin='2024-11-08', Responsable="Juan"),
dict(Tarea="Generación de reportes y exportación a CSV", FechaInicio='2024-11-09', FechaFin='2024-11-12', Responsable="Julieth"),
dict(Tarea="Pruebas finales y ajustes de software", FechaInicio='2024-11-13', FechaFin='2024-11-17', Responsable="María"),
dict(Tarea="Documentación (Manual de usuario y README)", FechaInicio='2024-11-18', FechaFin='2024-11-21', Responsable="Julieth"),
dict(Tarea="Entrega final del trabajo", FechaInicio='2024-11-22', FechaFin='2024-11-24', Responsable="Juan, María, Julieth")
])

## *Presupuesto*
*Numero de integrantes:* 3 (Juan Manuel, Maria Isabel, Julieth)
*Horas dedicas por integrante:* 80 horas c/u
*Total de horas del equipo:* 3*80= 240 Horas 
*Equivalencia al SMLV:* 8 horas/día * 30dias/mes= 240 horas/mes
El presupuesto de tiempo para este proyecto se mide en horas de trabajo y corresponde a 1 SMLV (240 horas). Esto refleja el esfuerzo conjunto de los tres integrantes, quienes dedicaremos un total de 240 horas (80 horas cada uno) a realizar el proyecto.
