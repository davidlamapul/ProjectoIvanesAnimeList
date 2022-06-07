import back_end as back

def main():
    while True:
        user = input('¿Tienes una cuenta? (Si/No) ')
        if user.upper() == "NO":
            nombre = input('Introduce tu nombre ')
            correo = input('Introduce tu correo ')
            contrasenia = input('Introduce tu contraseña ')
            main_menu( back.create_user(correo, contrasenia, nombre) )
            break
        elif user.upper() == "SI":
            correo = input('Introduce tu correo ')
            contrasenia = input('Introduce tu contraseña ')
            try:
                back.get_user_id(correo, contrasenia)  
            except:
                print('Usuario no encontrado.')
                main()
            main_menu( back.get_user_id(correo, contrasenia) )
            break
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

def main_menu(id_user):
    while True:
        opcion = menu()
        if opcion == "1":
            back.get_all_animes()
        elif opcion == "2":
            nombre = input("Nombre del anime ")
            anio = input('Año de estreno ')
            cap = input('Capitulos totales ')
            back.create_anime(nombre, cap, anio)

        elif opcion == "3":
            back.get_all_animes(id_user)

        elif opcion == "4":
            nombre = input("Nombre del anime ")
            estado = input('Estado (finalizado/comenzado) ')
            cap = input('Capitulos totales')
            back.add(id_user, nombre, estado, cap)

        elif opcion == "5":
            nombre = input("Nombre del anime ")
            estado = input('Estado (finalizado/comenzado) ')
            cap = input('Capitulos totales ')
            back.update(id_user, nombre, estado, cap)
        elif opcion == "6":
            nombre = input("Nombre del anime ")
            back.remove(id_user, nombre)
        elif opcion == "7":
            break

back.initialise_database()
main()



