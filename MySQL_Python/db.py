import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='MaNu$$1015',
    database='prueba'
)

cursor = midb.cursor()

# Listar datos y limitar la cantidad de datos
#cursor.execute('select * from Usuario') # Muestra lo que hay en la base de datos
#resultado = cursor.fetchall() # fetchall es palabra reservada para hacer la busqueda, en este caso a todos
#print(resultado)

cursor.execute('select * from Usuario limit 1') 
resultado = cursor.fetchall() 
print(resultado)
#----------------------------------------------------------------------
# Ver definiciones de tablas
#cursor.execute('show create table Usuario') # Muestra como se creo la tabla
#------------------------------------------------------------------------------
# insertar datos
#sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
#values = ('manumenox@gmail.com', 'Manuel 2', '25')
#cursor = midb.cursor() # Nos permite interacuar con la base de datos
#cursor.execute(sql,values) # esto permite realizar la escritura, más no almacena en la base de datos
#midb.commit() # Esto permite escribir y guardar
#print(cursor.rowcount)
#------------------------------------------------------------------------------------------
# Actualizar datos
#sql = 'update Usuario set email = %s where id = %s'
#values=('mendoza.meza.manuel.20.1@gmail.com',4)

#cursor.execute(sql,values)
#midb.commit()
#-------------------------------------------------------------------------------------
# Eliminar datos
#sql = 'delete from Usuario where id = %s'
#values=(4, ) # Es necesario el ,_ porque si no manda un error

#cursor.execute(sql,values)
#midb.commit()
#-------------------------------------------------------------------------------------
