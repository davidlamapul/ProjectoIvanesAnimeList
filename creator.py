import pymysql
from pymysql.cursors import DictCursor

def main():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='esplai22',
                                   cursorclass=DictCursor)
        with conexion.cursor() as cursor:
            cursor.execute('use sakila; select * from actor;')
            a=cursor.fetchall()
        print(a)
        conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
        
with open('dbcreator.sql', 'r') as file:
    print(file.read().replace('\n','').split(';').remove(''))
