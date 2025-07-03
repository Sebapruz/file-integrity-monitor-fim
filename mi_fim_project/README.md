🛡️ Sistema Básico de Monitoreo de Integridad de Archivos (FIM)
📝 Descripción del Proyecto
Este proyecto es una implementación básica de un Sistema de Monitoreo de Integridad de Archivos (File Integrity Monitoring - FIM), una herramienta fundamental en las operaciones de Blue Team para la detección de amenazas y la seguridad proactiva. Su objetivo principal es monitorear un directorio específico en busca de cambios no autorizados en los archivos, como modificaciones, adiciones o eliminaciones.

En un entorno real, los ataques pueden incluir la alteración de archivos de configuración, la inyección de código malicioso en scripts existentes o la creación de nuevos archivos para establecer persistencia. Este FIM detecta estas anomalías calculando y comparando las firmas hash de los archivos con una línea base ("baseline") previamente establecida.

Este proyecto ha sido desarrollado como un primer paso para entender y aplicar principios de seguridad defensiva, ofreciendo una base para futuras expansiones hacia soluciones FIM más robustas.

🌟 Características
Monitoreo de Integridad: Detecta cambios en el contenido de los archivos mediante la comparación de hashes.

Detección de Nuevos Archivos: Identifica y reporta archivos que han sido añadidos al directorio monitoreado.

Detección de Archivos Eliminados: Alerta sobre la ausencia de archivos que anteriormente formaban parte de la línea base.

Registro de Eventos (Logging): Registra todas las detecciones y actividades en un archivo de log con marcas de tiempo.

Baseline Persistente: Almacena la línea base de los hashes de los archivos en un archivo JSON para comparaciones futuras.

Configuración Sencilla: Fácil de configurar especificando el directorio a monitorear.

🛠️ Tecnologías Utilizadas
Python 3.x: Lenguaje principal de desarrollo.

os: Módulo para interactuar con el sistema operativo (rutas de archivos, directorios).

hashlib: Módulo para generar hashes criptográficos (SHA256).

json: Módulo para leer y escribir datos en formato JSON (para el baseline).

datetime: Módulo para manejar fechas y horas en los logs.

🚀 Cómo Empezar
Prerequisitos

Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Puedes descargarlo desde python.org.

Instalación

Clona el Repositorio:

Bash
git clone https://github.com/Sebapruz/file-integrity-monitor-fim.git
cd file-integrity-monitor-fim
(Reemplaza tu_usuario con tu nombre de usuario de GitHub)

Configura el Directorio a Monitorear:

Dentro de la carpeta del proyecto, crea una carpeta de prueba que quieras monitorear. Por ejemplo, mi_carpeta_segura.

Abre el archivo fim_monitor.py y modifica la variable TARGET_DIRECTORY a la ruta de tu carpeta de prueba:

Python
TARGET_DIRECTORY = "mi_carpeta_segura" # ¡Asegúrate de que esta carpeta exista!
(Opcional) Coloca algunos archivos dentro de mi_carpeta_segura para empezar a monitorear (ej. config.txt, mis_datos.csv).

Uso

El script opera en dos fases principales: inicialización del baseline y monitoreo/detección de cambios.

Primera Ejecución (Inicializar el Baseline):
Ejecuta el script por primera vez. Esto calculará los hashes de todos los archivos en TARGET_DIRECTORY y los guardará en baseline.json.

Bash
python fim_monitor.py
Verás mensajes en la consola y se crearán los archivos baseline.json y fim_log.txt.

Simular Cambios:
Para probar el sistema, realiza algunos cambios en los archivos dentro de mi_carpeta_segura:

Modifica el contenido de un archivo existente.

Crea un nuevo archivo.

Elimina un archivo existente.

Segunda y Posteriores Ejecuciones (Detectar Cambios):
Vuelve a ejecutar el script. Ahora comparará el estado actual de los archivos con el baseline guardado y reportará cualquier cambio detectado.

Bash
python fim_monitor.py
Los cambios detectados se mostrarán en la consola y se registrarán en fim_log.txt.

🧠 Conceptos de Ciberseguridad Aprendidos
Al desarrollar este proyecto, he profundizado en los siguientes conceptos clave de ciberseguridad relacionados con el Blue Team:

Monitoreo de Integridad de Archivos (FIM): Comprender su rol crucial en la detección temprana de intrusiones, alteraciones de configuración y actividad maliciosa.

Hashing Criptográfico: Implementar y entender cómo funciones hash como SHA256 crean "huellas digitales" únicas e inalterables de los archivos, esenciales para verificar su integridad.

Detección Basada en Anomalías: Aprender a establecer una línea base de "normalidad" y cómo cualquier desviación de esta línea base puede indicar un incidente de seguridad.

Registro y Auditoría (Logging): La importancia de registrar eventos de seguridad con marcas de tiempo para análisis forenses y la cadena de custodia de la información.

Automatización de Tareas de Seguridad: Escribir scripts para automatizar procesos de monitoreo, liberando recursos para tareas más complejas.

Defensa en Profundidad: Este FIM es una capa más en una estrategia de defensa en profundidad, proporcionando visibilidad a nivel de sistema de archivos.

💡 Futuras Mejoras y Expansiones
Este proyecto es un punto de partida. Aquí hay algunas ideas para extender sus funcionalidades y aprender más:

Programación de Tareas: Integrar con cron (Linux) o el Programador de Tareas (Windows) para ejecutar el monitoreo automáticamente a intervalos regulares.

Notificaciones Avanzadas: Enviar alertas por correo electrónico, Slack, Discord o integrar con un sistema de gestión de eventos e información de seguridad (SIEM) básico.

Base de Datos Persistente: Utilizar una base de datos más robusta como SQLite para almacenar el baseline, especialmente útil para monitorear un gran número de archivos.

Exclusiones: Permitir la configuración de archivos o directorios a ignorar (por ejemplo, archivos de log que cambian constantemente).

Monitoreo en Tiempo Real: Implementar una solución que reaccione instantáneamente a los cambios en el sistema de archivos utilizando librerías como watchdog en Python.

Validación de Permisos: Añadir verificación de permisos de archivo para detectar cambios en los atributos de seguridad.