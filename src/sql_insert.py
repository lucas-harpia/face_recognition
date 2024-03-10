import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()


def conectar_db():
    try:
        conexao = pymysql.connect(
            host=os.getenv("db_host"),
            user=os.getenv("db_user"),
            port=int(os.getenv("db_port")),
            password=os.getenv("db_password"),
            database=os.getenv("db_database")
        )
        return conexao
    except pymysql.Error as erro:
        print("Erro ao conectar ao MySQL:", erro)
        return None


def insert_entidades(matriz):
    conn = conectar_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute(
                f'''INSERT INTO {os.getenv("tb_recognition")} (login) VALUES (%s)''', (matriz,))
            conn.commit()
        except pymysql.MySQLError as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
