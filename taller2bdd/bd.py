import pymysql 

connector = pymysql.connect(
    user="root",
    password="1234",
    host="127.0.0.1",
    port=3307,
    database="bd_clase"
)

with connector.cursor() as cursor:
        #
        cursor.execute("""
            CREATE TABLE usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL
            );
        """)
        print("-> Tabla 'usuarios' creada correctamente.")

        # 
        cursor.execute("""
            CREATE TABLE juzgado (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                ubicacion VARCHAR(150)
            );
        """)
        print("-> Tabla 'juzgado' creada correctamente.")
        
        #
        connector.commit()


with connector.cursor() as cursor:
        # 
        cursor.execute("""
            CREATE TABLE hora_de_servicios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                horario TIME NOT NULL,
                descripcion VARCHAR(100)
            );
        """)
        print("-> Tabla 'hora_de_servicios' creada correctamente.")

        #
        cursor.execute("""
            CREATE TABLE estados_citas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre_estado VARCHAR(50) NOT NULL
            );
        """)
        print("-> Tabla 'estados_citas' creada correctamente.")

        #
        cursor.execute("""
            CREATE TABLE aseguradoras (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                telefono VARCHAR(20)
            );
        """)
        print("-> Tabla 'aseguradoras' creada correctamente.")
        
        connector.commit()