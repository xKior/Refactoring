from src.config import settings

def main():
    print("🚀 Proyecto inicial funcionando")
    print(f"Entorno: {settings.ENV}")
    print(f"Base de datos: {settings.DATABASE_URL}")

if __name__ == "__main__":
    main()
