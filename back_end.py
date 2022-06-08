import connection


def initialise_database():
    if not connection.checkdb():
        connection.createdb()


def get_anime_id(anime_name: str):
    sql = f"SELECT IdAnime FROM anime WHERE Nombre = '{anime_name}';"
    return connection.executeall(sql)[0]['IdAnime']


def create_user(email: str, password: str, username: str):
    sql = f"INSERT INTO USUARIO(Username, EMail, Pass) VALUES ('{username}', '{email}', '{password}');"
    connection.executeall(sql)

    sql2 = f"SELECT IdUser FROM USUARIO WHERE EMail = '{email}';"
    return connection.executeall(sql2)[0]['IdUser']


def get_user_id(email: str, password: str):
    # todo check password
    sql = f"SELECT * FROM USUARIO WHERE EMail = '{email}';"

    return connection.executeall(sql)[0]['IdUser']


def create_anime(name_anime: str, ep_total: int, year: int, id_sequel='null'):
    sql = f"INSERT INTO ANIME(Nombre, Estreno, EpTotal, RIdSecuela) VALUES ('{name_anime}', {year}, {ep_total}, {id_sequel});"
    connection.executeall(sql)


# todo status por defecto en viendo
def add(user_id: int, name_anime: str, status: str = 'Viendo', ep_watched: int = 0):
    anime_id = get_anime_id(name_anime)

    sql2 = f"INSERT INTO usuario_anime VALUES({user_id}, {anime_id}, {ep_watched}, '{status}');"
    connection.executeall(sql2)


def remove(user_id: int, name_anime: str):
    anime_id = get_anime_id(name_anime)

    sql = f"DELETE FROM usuario_anime WHERE RIdUser = {user_id} AND RIdAnime = {anime_id};"
    connection.executeall(sql)


# status y ep_watched son opcionales
def update(user_id: int, name_anime: str, status: str = None, ep_watched: int = None):
    anime_id = get_anime_id(name_anime)

    if status is not None:
        sql = f"update usuario_anime set Estado = '{status}' where RIdUser = {user_id} AND RIdAnime = {anime_id};"
        connection.executeall(sql)

    if ep_watched is not None:
        sql2 = f"update usuario_anime set EpVistos = {ep_watched} where RIdUser = {user_id} AND RIdAnime = {anime_id};"
        connection.executeall(sql2)


def get_all_animes(user_id: int = None):
    if user_id is None:
        sql = f"select * from anime;"
        return connection.executeall(sql)
    else:
        sql2 = f"select * from anime a, usuario_anime ua where a.IdAnime = ua.RIdAnime AND ua.RIdUser = {user_id};"
        return connection.executeall(sql2)

def export(id_user):
    sql=f'''select a.Nombre, a.Estreno, a.EpTotal, ua.EpVistos, ua.Estado from anime a
    inner join usuario_anime ua
    on ua.ridAnime=a.idanime
    inner join usuario u
    on u.iduser=ua.riduser
    where iduser = {id_user};'''
    sql2=f'select username from usuario where iduser = {id_user};'
    lista=connection.executeall(sql)
    username=connection.executeall(sql2)[0]['username']
    with open(f'{username}_animelist.txt','w') as f:
        f.write(f"{'Nombre':<20} {'Estreno':<8} {'EpTotal':<8} {'EpVistos':<8} {'Estado':<12}\n")
        for l in lista:
            line=f"{l['Nombre']:<20} {l['Estreno']:<8} {l['EpTotal']:<8} {l['EpVistos']:<8} {l['Estado']:<12}"
            if l!=lista[-1]:
                line=line+'\n'
            f.write(line)