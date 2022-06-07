# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import back_end.py as back

def main():
    while True:
        user = input('¿Tienes una cuenta? (Si/No)')
        if user.upper() = "NO":
            nombre = input('Introduce tu nombre')
            correo = input('Introduce tu correo')
            contrasenia = input('Introduce tu contraseña')
            main_menu( back.create_user(correo, contrasenia, nombre) )
        elif user.upper() = "SI":
            correo = input('Introduce tu correo')
            contrasenia = input('Introduce tu contraseña')
            main_menu( back.get_user_id(correo, contrasenia) )
        else:
            print('Por favor introduce una opcion correcta')




def menu():
    print('''Introduce un numero segun la opcion que quieras usar
1- Para ver toda la lista de animes disponibles
2- Para añadir un anime que no este en la aplicacion
3- Para ver mi lista de animes vistos o en pendiente
4- Para añadir a mi lista de animes vistos o en pendiente
5- Para modificar el estado de un anime
6- Para borrar un anime de mi lista
7- Para salir de la aplicacion
Aviso: si introduces una opcion incorrecta se volvera a mostrar
el mensaje hasta que introduzcas una opcion correcta''')
    opcion = input("\n")
    return opcion

def main_menu():
    while True:
        opcion = menu()
        if opcion == "1":
            read_file()
        elif opcion == "2":
            cliente = input("Nombre del cliente a consultar ")
            read_one_file(cliente)

        elif opcion == "3":
            cliente = input("Nombre del cliente para añadir ")
            telefono = input("Teléfono del cliente para añadir ")
            add_file(cliente, telefono)

        elif opcion == "4":
            cliente = input("Nombre del cliente a borrar ")
            delete_file(cliente)

        else:
            break

main()



