def initialise_database():
    print()


def create_user(email: str, password: str, username: str):
    user_id: int
    sql = f"INSERT INTO USUARIO(Username, EMail, Pass) VALUES ({username}, {email}, {password})"

    print(sql)

    return user_id


def get_user_id(email: str, password: str):
    user_id: int

    return user_id


# todo poner todos los campos
def create_anime(name_anime: str, ep_total: int, year: int, id_sequel: int = None):
    print()


# todo status por defecto en viendo
def add(user_id: int, name_anime: str, status: str = None, ep_watched: int = 0):
    print()


def remove(user_id: int, id_anime: int):
    print()


# status y ep_watched son opcionales
def update(user_id: int, name_anime: str, status: str = None, ep_watched: int = None):
    if status is not None:
        print()

    if ep_watched is not None:
        print()


def get_all(user_id: int = None):
    if user_id is not None:
        print()
    else:
        print()

    return []
