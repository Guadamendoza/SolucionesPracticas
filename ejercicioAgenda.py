def mostrar_menu():
    print("\n--- Menú de la Agenda Telefónica ---")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar todos en la agenda")
    print("5. Salir")

def agregar_persona(agenda):
    dni = input("DNI: ").strip()
    agenda[dni] = {
        "apellido": input("Apellido: ").strip(),
        "nombre": input("Nombre: ").strip(),
        "email": input("Email: ").strip(),
        "telefono": input("Número de teléfono: ").strip()
    }
    print("Persona agregada con éxito.")

def modificar_persona(agenda):
    dni = input("DNI de la persona a modificar: ").strip()
    print("Deja en blanco el campo que no quieras modificar.")
    persona = agenda[dni]
    persona['apellido'] = input(f"Apellido ({persona['apellido']}): ").strip() or persona['apellido']
    persona['nombre'] = input(f"Nombre ({persona['nombre']}): ").strip() or persona['nombre']
    persona['email'] = input(f"Email ({persona['email']}): ").strip() or persona['email']
    persona['telefono'] = input(f"Teléfono ({persona['telefono']}): ").strip() or persona['telefono']
    print("Persona modificada con éxito.")

def eliminar_persona(agenda):
    dni = input("DNI de la persona a eliminar: ").strip()
    if dni in agenda:
        del agenda[dni]
        print("Persona eliminada con éxito.")
    else:
        print("No se encontró una persona con ese DNI.")

def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        for dni, datos in agenda.items():
            print(f"DNI: {dni}, Apellido: {datos['apellido']}, Nombre: {datos['nombre']}, Email: {datos['email']}, Teléfono: {datos['telefono']}")

def main():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()
        if opcion == "1":
            agregar_persona(agenda)
        elif opcion == "2":
            modificar_persona(agenda)
        elif opcion == "3":
            eliminar_persona(agenda)
        elif opcion == "4":
            mostrar_agenda(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda telefónica.")
            break
        else:
            print("Opción no válida, por favor elige una opción del 1 al 5.")

if __name__ == "__main__":
    main()
