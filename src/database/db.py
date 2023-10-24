import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ.get("USER")
host = os.environ.get("HOST")
password = os.environ.get("PASSWORD")
database = os.environ.get("DATABASE")
port = os.environ.get("PORT")

connection = None
cursor = None

def init():
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, psycopg2.Error) as error:
        raise("Error while connecting to PostgreSQL", error)

def query(query, params=None):
    try:
        print("Query: ", query)
        print("Params: ", params)
        cursor.execute(query, params or ())
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        raise("Error while executing query", error)
    
def callProc(name_sp, params=None):
    try:
        print("Procedure: ", name_sp)
        print("Params: ", params)
        cursor.callproc(name_sp, params or ())
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        raise("Error while executing procedure", error)
    
def commit():
    try:
        cursor.commit()
    except (Exception, psycopg2.Error) as error:
        raise("Error while commiting", error)
    
def rollback():
    try:
        cursor.rollback()
    except (Exception, psycopg2.Error) as error:
        raise("Error while rollbacking", error)
    
def close():
    try:
        cursor.close()
    except (Exception, psycopg2.Error) as error:
        raise("Error while closing cursor", error)
    finally:
        try:
            connection.close()
        except (Exception, psycopg2.Error) as error:
            raise("Error while closing connection", error)