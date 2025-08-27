Este repositorio contiene un ejemplo de **estructura básica de un entorno virtual en python**, incluyendo:

1.Entorno Virtual
- Uso de **entorno virtual (`venv`)**
- Separación de dependencias (`requirements.txt` y `requirements-dev.txt`)
- Configuración por variables de entorno (`.env.example`)
- Organización en carpetas (`src`, `tests`)
  
2.Ejemplo de actividades
- Ejemplos de buenas prácticas con **Refactoring** y **Principios SOLID**

refactoring.py → ejemplo de mejora de código aplicando buenas prácticas (nombres descriptivos, validación robusta, manejo de errores, separación de responsabilidades).

solid.py → implementación de un sistema básico de notificaciones aplicando los principios:
SRP: cada clase se encarga de un tipo de notificación

OCP: se pueden agregar nuevos tipos sin modificar los existentes

DIP: se usa una abstracción (NotificationSender) en lugar de depender de clases concretas
