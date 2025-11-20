# 1. Navega al directorio de la aplicación (donde están los archivos .py y el .venv)
cd first_steps
# 2. Crea el entorno virtual (si no existe)
python -m venv .venv
# 3. Activa el entorno virtual (Usando la ruta estándar)
source .venv/bin/activate
# 4. Actualiza pip e instala dependencias
pip install --upgrade pip
pip install -r requirements.txt

# --- Proceso de Exportación de Reflex ---

# 5. Limpia la carpeta 'public' antigua si existe
rm -rf public
# 6. Inicializa Reflex (Asegura que el proyecto esté listo)
reflex init
# 7. Exporta el frontend (genera frontend.zip)
API_URL=demos-data-riders.vercel.app reflex export --frontend-only
# 8. Descomprime los archivos estáticos en la carpeta 'public'
unzip frontend.zip -d public
# 9. Limpia los archivos temporales de exportación
rm -f frontend.zip
# 10. Desactiva el entorno virtual
deactivate