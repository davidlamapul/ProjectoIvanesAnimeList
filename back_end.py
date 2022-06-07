def initialise_database():
    print()


def create_user(email: str, password: str, username: str):
    user_id: int
    sql = f"INSERT INTO USUARIO(Username, EMail, Pass) VALUES ({username}, {email}, {password});"

    print(sql)

    return user_id


def get_user_id(email: str, password: str):
    user_id: int

    sql = f"SELECT * FROM USUARIO WHERE EMail = {email}"

    return user_id


def create_anime(name_anime: str, ep_total: int, year: int, id_sequel: int = None):

    if id_sequel is None:
        id_sequel = 'null'

    sql = f"INSERT INTO ANIME(Nombre, Estreno, EpTotal, RIdSecuela) VALUES ({name_anime}, {year}, {ep_total}, {id_sequel});"

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
