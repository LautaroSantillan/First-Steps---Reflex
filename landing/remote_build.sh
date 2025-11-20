# Navega al directorio de la aplicación
cd landing
# 1. Crea y activa el entorno virtual (Aseguramos la compatibilidad)
python3 -m venv .venv
source .venv/bin/activate
# 2. Actualiza pip e instala dependencias
pip install --upgrade pip
pip install -r requirements.txt

# --- Proceso de Exportación de Reflex ---

# 3. Limpia la carpeta 'public' antigua si existe
rm -rf public
# 4. Inicializa Reflex (Asegura que el proyecto esté listo)
reflex init
# 5. Exporta el frontend (genera frontend.zip)
reflex export --frontend-only
# 6. Descomprime los archivos estáticos en la carpeta 'public'
unzip frontend.zip -d public
# 7. Limpia los archivos temporales de exportación
rm -f frontend.zip
# 8. Desactiva el entorno virtual
deactivate