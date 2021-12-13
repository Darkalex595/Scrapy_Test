import psycopg2
from psycopg2 import Error
from ConvertJson import createInsert

#Funcion para crear la conexión y guardar la info en la base de datos.
def realizarConexion():
    try:
        conexion = psycopg2.connect(
            host="localhost",
            database="Libros",
            user="postgres",
            password="Nesmar$31"
        )
        cursor = conexion.cursor()
        print("PostgreSQL server information")
        print(conexion.get_dsn_parameters(), "\n")
        
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (conexion):
            sql_ins = createInsert()
            
            try:
                cursor.execute(sql_ins)
                conexion.commit()
                print ('\nfinished INSERT INTO execution')
            except (Exception, Error) as error2:
                print("\nexecute_sql() error:", error2)
                conexion.rollback()
            
            
            cursor.close()
            conexion.close()
            print("PostgreSQL connection is closed")
        