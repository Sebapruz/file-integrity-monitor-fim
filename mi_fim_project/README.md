# 🛡️ Sistema Básico de Monitoreo de Integridad de Archivos (FIM)

## 📝 Descripción del Proyecto

Este proyecto implementa un Sistema de Monitoreo de Integridad de Archivos (FIM), una herramienta fundamental para las operaciones de Blue Team. Su objetivo es fortalecer la seguridad proactiva y la detección de amenazas monitoreando un directorio específico en busca de cambios no autorizados.

El FIM detecta anomalías como:

- Modificaciones en archivos existentes.
- Creación de archivos nuevos.
- Eliminación de archivos.

Para lograrlo, el sistema calcula y compara los hashes SHA256 de los archivos con una línea base (baseline) previamente establecida. Esto permite identificar rápidamente si algún archivo ha sido comprometido o alterado por actividad maliciosa.

---

## 🌟 Características

- ✅ **Monitoreo de Integridad:** Detecta cualquier cambio en el contenido de los archivos.
- ➕ **Detección de Archivos Nuevos:** Identifica la aparición de archivos no registrados en la línea base.
- ❌ **Detección de Archivos Eliminados:** Alerta sobre la desaparición de archivos existentes en la línea base.
- 🗂️ **Registro de Eventos (Logging):** Todos los eventos y detecciones se registran con marcas de tiempo para auditoría.
- 💾 **Baseline Persistente:** La línea base de hashes se almacena de forma segura en un archivo `.json`.
- ⚙️ **Configuración Sencilla:** Requiere solo la especificación del directorio a monitorear.

---

## 🛠️ Tecnologías Utilizadas

El proyecto está desarrollado en **Python 3.x** y utiliza las siguientes librerías estándar:

- `os`: Para la interacción con el sistema operativo y la gestión de rutas de archivos.
- `hashlib`: Para la generación de hashes criptográficos (SHA256).
- `json`: Para la lectura y escritura de la línea base en formato JSON.
- `datetime`: Para añadir marcas de tiempo precisas a los registros de eventos.

---

## 🚀 Cómo Empezar

### 📋 Prerrequisitos

- Asegúrate de tener Python **3.8 o superior** instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

### 💻 Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/tu_usuario/file-integrity-monitor-fim.git
cd file-integrity-monitor-fim
```
Configura el directorio a monitorear:

Crea una carpeta de prueba que desees monitorear, por ejemplo:
```bash
mkdir mi_carpeta_segura
```
Edita el archivo fim_monitor.py y actualiza la variable TARGET_DIRECTORY para apuntar a tu carpeta:
```bash
TARGET_DIRECTORY = "mi_carpeta_segura"  # ¡Asegúrate de que esta carpeta exista!
```
Agrega algunos archivos de prueba dentro de mi_carpeta_segura (ej. config.txt, mis_datos.csv) para comenzar el monitoreo.

### ⚙️ Uso

El script opera en dos fases clave: la inicialización de la línea base y el monitoreo/detección de cambios.

### 🟢 Primera Ejecución (Inicialización del Baseline)
Ejecuta el script por primera vez. Esto calculará los hashes de todos los archivos en el TARGET_DIRECTORY y los almacenará en baseline.json. También se creará el archivo de log fim_log.txt.
```bash
python fim_monitor.py
```

### 🧪 Simular Cambios
Modifica archivos, agrega nuevos o elimina alguno dentro de mi_carpeta_segura.

### 🔁 Segunda y Posteriores Ejecuciones (Detección de Cambios)
Ejecuta el script nuevamente. Ahora comparará el estado actual de los archivos con la línea base guardada y reportará cualquier cambio detectado.
```bash
python fim_monitor.py
```
Verás en la consola y en fim_log.txt cualquier cambio detectado.

### 🧠 Conceptos de Ciberseguridad Aprendidos

- Monitoreo de Integridad de Archivos (FIM).
- Hashing Criptográfico (SHA256).
- Detección basada en anomalías.
- Registro y auditoría de eventos.
- Automatización de tareas de seguridad.
- Defensa en profundidad.

### 💡 Futuras Mejoras

Este proyecto es un excelente punto de partida para seguir explorando y mejorando. Algunas ideas para futuras expansiones incluyen:

- 📅 Programación de Tareas: Integrar con cron (Linux) o el Programador de Tareas (Windows).
- 📩 Alertas Mejoradas: Notificaciones por correo, Discord, Slack o integración con SIEM.
- 🗃️ Base de Datos Escalable: Usar SQLite en lugar de JSON para mayor robustez.
- 🚫 Exclusiones Configurables: Ignorar archivos como logs que cambian frecuentemente.
- ⚡ Monitoreo en Tiempo Real: Usar watchdog en Python para detección instantánea.
- 🔐 Validación de Permisos: Monitorear cambios en permisos o atributos de seguridad.
  
📄 Licencia

Este proyecto se publica con fines educativos y de aprendizaje.

Desarrollado con 💻 por Sebapruz
