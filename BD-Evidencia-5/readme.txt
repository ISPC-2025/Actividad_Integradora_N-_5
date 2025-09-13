Ejecución del Primer Script

Para ejecutar el script que crea la estructura de la base de datos, lo que se debe hacer es copiar el contenido del archivo y pegarlo directamente en el editor DBMS en línea: 'OneCompiler' (https://onecompiler.com/).
Es crucial seleccionar el lenguaje MySQL en el menú de opciones para que el código se interprete correctamente.
Este script es el primer paso y debe ejecutarse antes que cualquier otro, ya que define todas las tablas y las relaciones necesarias (como las claves primarias y foráneas).
Al hacer clic en el botón de "Run", el sistema procesará todas las instrucciones CREATE TABLE, construyendo la base de datos vacía pero lista para recibir los datos.

Ejecución del Segundo Script

Una vez que las tablas han sido creadas con éxito, se puede proceder a ejecutar el segundo script.
Al igual que con el anterior, el proceso consiste en copiar el código y pegarlo en el mismo editor de MySQL.
Este script realiza dos tareas principales: primero, utiliza múltiples sentencias INSERT INTO para poblar las tablas con datos de ejemplo; luego, ejecuta varias consultas SELECT para recuperar y mostrar información específica.
Al pulsar "Run", el DBMS procesará primero todas las inserciones y, de forma secuencial, ejecutará las consultas SELECT, mostrando el resultado en la ventana de salida, lo que permite verificar que los datos se han insertado y consultado correctamente.