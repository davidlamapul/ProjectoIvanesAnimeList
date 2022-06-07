import pymysql
from pymysql.cursors import DictCursor

def checkdb():
    '''Comprueba si la base de datos 'animelist 'existe.
    Si existe retorna True, si no, False.
    '''
    connexion = pymysql.connect(host='localhost',
                           user='root',
                           password='esplai22',
                           cursorclass=DictCursor)
    with connexion.cursor() as cursor:
         cursor.execute('show databases')
         dbs=cursor.fetchall()
    check=False
    for db in dbs:
        if db['Database']=='animelist':
            check=True
    connexion.commit()
    connexion.close()
    return check

def createdb():
    '''Crea la base de datos.
    No retorna nada.
    '''
    with open('dbcreator.sql', 'r') as file:
        script=file.read()
    commands=script.replace('\n',' ').split(';')
    try:
        commands.remove('')
    except:
        pass
    connexion = pymysql.connect(host='localhost',
                           user='root',
                           password='esplai22',
                           cursorclass=DictCursor)
    with connexion.cursor() as cursor:
        for command in commands:
            cursor.execute(command)
    connexion.commit()
    connexion.close()

def getscript(file):
    '''Obtiene la lista de comandos de un archivo sql.
    Retorna un string con el script. Separa los comandos por ';'.
    '''
    with open(file, 'r') as f:
        script=file.read()
    return script
    
def executeall(script):
    '''Ejecuta un script en forma de string. Acepta strings de línea múltiple
    (los de las triples comillas).
    Retorna el output del script.
    '''
    commands=script.replace('\n','').split(';')
    try:
        commands.remove('')
    except:
        pass
    connexion = pymysql.connect(host='localhost',
                           user='root',
                           password='esplai22',
                           cursorclass=DictCursor,
                           db='ANIMELIST')
    with connexion.cursor() as cursor:
        for command in commands:
            cursor.execute(command)
        a=cursor.fetchall()
    connexion.commit()
    connexion.close()
    return a
      
