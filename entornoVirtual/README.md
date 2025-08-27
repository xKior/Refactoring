# Mi Entorno Virtual En Python

Estructura inicial de un proyecto en Python con:

- Entorno virtual
- Separación de dependencias
- Configuración por variables de entorno
- Carpeta `src` para código fuente
- Carpeta `tests` para pruebas

## Como iniciar

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements-dev.txt

# Ejecutar la app
python src/main.py
