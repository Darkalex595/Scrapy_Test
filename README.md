# Scrapy_Test

## Nota de desarrollador
### 1. Para la correcta ejecución del programa se necesitan cambiar las direcciones de archivos en la línea 67 del archivo Spider.py por la locación donde se va a guardar el archivo JSON y la línea 5 en ConvertJson.py que es el link donde esta guardado el archivo JSON ya que ambos links estan hechos basados en las carpetas dentro de mi computadora personal.
### 2. Para la conexión a postgres se necesitara postgres local o alguno remoto ya que el programa esta codeado para trabajar con localhost, es decir una BD dentro de mi propia computadora. Es necesario tener postgres dentro de la computadora o servidor.

## Descripcion
#### La solución implementada consiste en 3 pasos:
#### - Paso 1: Se creó el spider en el archivo Spider.py. El spider de nombre books contiene 2 funciones parse, la primera (parse) es encargada de navegar entre lás páginas que muestran los libros de manera superficial sin detalles. Esta función saca el link de los detalles de cada libro individual. Usando este link, manda a llamar a la otra función parse (parse_detalles) y entra a cada libro a extraer la información pertinente de cada libro usando el css para encontrar la información. El css se analizó desde la página para poder saber como extraer la información. Una vez termina de extraer los datos de cada libro en la página de productos que se encuentra el spider, este busca el link del boton de next y se manda a llamar de manera recursiva para acceder a la siguiente página de productos y asi hasta terminar con todas las páginas y todos los libros dentro de la página web. Luego de terminar de recoger la información, el script crea un archivo JSON llamado books.json usando el output del spider.

#### - Paso 2: Luego de creado el spider se desarrolló una función de conexión con el programa de base de datos postgresql. Se descargó postgres y se usó el localhost para hostear la base de datos. Se creó el programa DB.py. Usando la libreria psycopg2, que es un middleware que conecta python con postgres, se crea la conexión ingresando las credenciales correspondientes. Luego de asegurar la conexión, se manda a llamar a un script nuevo llamado ConvertJson que lo que hace es usar el archivo books.json para sacarle el arreglo de jsons para ingresarlo en un statement de SQL de insert para prepararlo para ejecutarlo y subir la información a la base de datos. Una vez se crea el insert, se ejecuta el comando y se hace el commit, si este es exitoso termina el programa y cierra la conexión, si hay un error, este manda un mensaje de error y cierra la conexión.

#### - Paso 3: El paso final para el desarrollo de la solución fue unir los pasos anteriores dentro de un script. Ambos pasos funcionaban por si solos ejecutandolos dentro la linea de comandos pero queria una solución un poco mas completa por lo que busque como ejecutar los spiders desde un script y econtré que era con la función crawl y habia que configurar para crear el archivo json. Una vez se pudo ejecutar el spider desde el script main.py, se manda a llamar la función de conexión para poder mandar la información a la base de datos dentro de postgres y de esta manera todo el programa se ejecuta usando solo el script de main.py.

## Lista de Commits

### Primer Commit
#### Se creo el spider para extraer la información de la página web http://books.toscrape.com/.
#### Se crea la tabla en postgresql basado en las variables extraidas de la página.

### Segundo Commit
#### Se crea el programa para realizar la conexión con la base de datos de postgres.

### Tercer Commit
#### Se crea una fachada para correr todos los programas [spider(Spider.py) y la conexión(DB.py)] usando un solo script (main.py)
#### Se añaden comentarios para mejor comprensión del programa
