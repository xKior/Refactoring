class UserData:

    def __init__(self, edad: int, nombre: str):
        self.edad = edad
        self.nombre = nombre

    def es_valido(self) -> bool:

        return 0 < self.edad < 150 and bool(self.nombre.strip())


def parse_input(entrada: str) -> UserData:
    try:
        partes = entrada.split(",")
        if len(partes) != 2:
            raise ValueError("La entrada de datos debe tener formato: edad,nombre")

        edad = int(partes[0].strip())
        nombre = partes[1].strip()

        return UserData(edad, nombre)

    except ValueError as e:
        raise ValueError(f"Datos de entrada invalidos: {e}")


def main():
    datos = input("Ingrese sus datos (edad,nombre): ")

    try:
        usuario = parse_input(datos)

        if usuario.es_valido():
            print("El usuario si es valido")
        else:
            print("Error en la validacion del usuario")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
