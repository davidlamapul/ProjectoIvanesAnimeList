import connection


def initialise_database():
    if not connection.checkdb():
        connection.createdb()


def create_user(email: str, password: str, username: str):
    sql = f"INSERT INTO USUARIO(Username, EMail, Pass) VALUES ('{username}', '{email}', '{password}');"

    connection.executeall(sql)

    sql = f"SELECT IdUser FROM USUARIO WHERE EMail = '{email}';"

    return connection.executeall(sql)[0]['IdUser']


def get_user_id(email: str, password: str):
    # todo check password
    sql = f"SELECT * FROM USUARIO WHERE EMail = {email};"

    return connection.executeall(sql)[0]['IdUser']


def create_anime(name_anime: str, ep_total: int, year: int, id_sequel='null'):
    sql = f"INSERT INTO ANIME(Nombre, Estreno, EpTotal, RIdSecuela) VALUES ('{name_anime}', {year}, {ep_total}, {id_sequel});"
    connection.executeall(sql)


# todo status por defecto en viendo
def add(user_id: int, name_anime: str, status: str = None, ep_watched: int = 0):
    sql = f"INSERT INTO usuario_anime"
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
