FROM python:3.11

WORKDIR /app
COPY . .

# Configuración del entorno virtual dentro del contenedor
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

# Instalación de dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Comando de ejecución (modo producción, solo backend)
CMD reflex run --env prod --backend-only