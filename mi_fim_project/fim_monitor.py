import os # Para interactuar con el sistema de archivos (directorios, rutas)
import hashlib # Para generar hashes de archivos (MD5, SHA256)
import json # Para guardar y cargar el baseline en formato JSON
import datetime # Para añadir marcas de tiempo a los logs

TARGET_DIRECTORY = "monitorear_este_directorio" # ¡CAMBIA ESTO! Define el directorio a monitorear.

BASELINE_FILE = "baseline.json"
LOG_FILE = "fim_log.txt"
HASH_ALGORITHM = "sha256" # Se puede usar "md5", "sha1", "sha256"

def calculate_file_hash(filepath, algorithm):
    """Calcula el hash de un archivo dado su ruta y algoritmo."""
    try:
        hasher = hashlib.new(algorithm)
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192): #Lee el archivo en bloques para archivos grandes
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        return None # Archivo no encontrado
    except Exception as e:
        log_event(f"Error al calcular hash de {filepath}: {e}")
        return None
    
def load_baseline(filename):
    """Carga el baseline desde un archivo JSON."""
    if os.path.exists(filename) and os.path.getsize(filename) > 0: # <-- ¡AÑADE ESTA CONDICIÓN!
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            # Si el archivo existe pero está vacío o mal formado, lo tratamos como vacío
            log_event(f"ADVERTENCIA: Archivo baseline '{filename}' vacío o corrupto. Se inicializará uno nuevo.")
            return {}
    return {} # Si no existe o está vacío desde el inicio, devuelve un diccionario vacío

def save_baseline(filename, data):
    """Guarda el baseline en un archivo JSON."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4) # indent=4 para una lectura más fácil

def log_event(message):
    """Registra un mensaje en el archivo de log con marca de tiempo."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}"
    print(log_entry) # Imprime también en consola
    with open(LOG_FILE, 'a') as f: # 'a' para añadir al final del archivo
        f.write(log_entry + "\n")

def run_fim_monitor():
    log_event("Iniciando monitoreo de integridad de archivos...")

    # 1. Cargar el baseline existente
    old_baseline = load_baseline(BASELINE_FILE)
    new_baseline = {}
    current_files = set() # Para llevar un registro de los archivos actuales

    # 2. Recorrer el directorio objetivo y calcular nuevos hashes
    for root, _, files in os.walk(TARGET_DIRECTORY):
        for filename in files:
            filepath = os.path.join(root, filename)
            # Asegúrate de que las rutas sean relativas o consistentes
            relative_filepath = os.path.relpath(filepath, TARGET_DIRECTORY)
            current_files.add(relative_filepath)
            
            current_hash = calculate_file_hash(filepath, HASH_ALGORITHM)
            if current_hash:
                new_baseline[relative_filepath] = current_hash

                if relative_filepath in old_baseline:
                    # Archivo existente: Comprobar si ha sido modificado
                    if old_baseline[relative_filepath] != current_hash:
                        log_event(f"MODIFICADO: {relative_filepath} (Hash anterior: {old_baseline[relative_filepath]}, Hash nuevo: {current_hash})")
                else:
                    # Archivo nuevo
                    log_event(f"NUEVO: {relative_filepath} (Hash: {current_hash})")
            else:
                log_event(f"ADVERTENCIA: No se pudo calcular el hash para {relative_filepath}. Ignorando.")

    # 3. Detectar archivos eliminados
    for filepath_in_old_baseline in old_baseline:
        if filepath_in_old_baseline not in current_files:
            log_event(f"ELIMINADO: {filepath_in_old_baseline}")

    # 4. Guardar el nuevo baseline
    save_baseline(BASELINE_FILE, new_baseline)
    log_event("Monitoreo de integridad de archivos completado. Baseline actualizado.")

if __name__ == "__main__":
    # Asegúrate de que el directorio objetivo exista antes de ejecutar
    if not os.path.isdir(TARGET_DIRECTORY):
        print(f"Error: El directorio objetivo '{TARGET_DIRECTORY}' no existe.")
        print("Por favor, crea la carpeta o actualiza la variable TARGET_DIRECTORY.")
    else:
        run_fim_monitor()