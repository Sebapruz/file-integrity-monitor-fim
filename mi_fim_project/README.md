# 🛡️ Sistema Básico de Monitoreo de Integridad de Archivos (FIM)

## 📝 Descripción del Proyecto

Este proyecto es una implementación básica de un **Sistema de Monitoreo de Integridad de Archivos (File Integrity Monitoring - FIM)**, una herramienta fundamental en operaciones de **Blue Team** para la detección de amenazas y la seguridad proactiva.

El objetivo principal es **monitorear un directorio específico** en busca de cambios no autorizados como:
- Modificaciones en archivos existentes.
- Creación de archivos nuevos.
- Eliminación de archivos.

Detecta estas anomalías **calculando y comparando los hashes SHA256** de los archivos contra una **línea base (baseline)** previamente establecida.

---

## 🌟 Características

- ✅ **Monitoreo de Integridad**: Detecta cambios en el contenido de los archivos.
- ➕ **Detección de Nuevos Archivos**.
- ❌ **Detección de Archivos Eliminados**.
- 🗂️ **Registro de Eventos (Logging)** con marcas de tiempo.
- 💾 **Baseline Persistente** en un archivo `.json`.
- ⚙️ **Configuración Sencilla**: Solo se especifica el directorio objetivo.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- `os`: Interacción con el sistema operativo.
- `hashlib`: Generación de hashes SHA256.
- `json`: Lectura/escritura de la línea base.
- `datetime`: Marcas de tiempo en los logs.

---

## 🚀 Cómo Empezar

### 📋 Prerrequisitos

- Tener instalado **Python 3.8 o superior**.
- Puedes descargarlo desde [python.org](https://www.python.org/).

### 💻 Instalación

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/file-integrity-monitor-fim.git
cd file-integrity-monitor-fim
Configura el directorio a monitorear:
Crea una carpeta de prueba, por ejemplo:

mkdir mi_carpeta_segura
Edita el archivo fim_monitor.py y modifica la línea:

TARGET_DIRECTORY = "mi_carpeta_segura"  # ¡Asegúrate de que esta carpeta exista!
Agrega archivos de prueba como config.txt, mis_datos.csv, etc.
⚙️ Uso

🟢 Primera Ejecución (Inicialización del Baseline)
python fim_monitor.py
Esto calculará los hashes de los archivos y los almacenará en baseline.json. También se creará el archivo de log fim_log.txt.

🧪 Simular Cambios
Modifica archivos, agrega nuevos o elimina alguno dentro de mi_carpeta_segura.

🔁 Segunda Ejecución (Detección de Cambios)
Ejecuta nuevamente el script:

python fim_monitor.py
Verás en la consola y en fim_log.txt cualquier cambio detectado.

🧠 Conceptos de Ciberseguridad Aprendidos

Monitoreo de Integridad (FIM).
Hashing Criptográfico (SHA256).
Detección basada en anomalías.
Registro y auditoría de eventos.
Automatización de tareas de seguridad.
Defensa en profundidad.
💡 Futuras Mejoras

📅 Programación con cron (Linux) o el Programador de Tareas (Windows).
📩 Alertas vía email, Discord, Slack o integración con un SIEM.
🗃️ Reemplazar JSON por SQLite para mayor escalabilidad.
🚫 Exclusiones configurables para ignorar ciertos archivos.
⚡ Monitoreo en tiempo real con la librería watchdog.
🔐 Validación de permisos y atributos de seguridad.
📎 Licencia

Este proyecto se publica con fines educativos y de aprendizaje.

Desarrollado con 💻 por Sebapruz
