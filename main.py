from bookSpider.books.spiders.Spider import execute
from DB import realizarConexion


print("Corriendo la spider bookSpider para sacar la información de la página http://books.toscrape.com/")
print("\n")
print("\n")

#La siguiente función se encarga de ejecutar desde el script la spider para que empieze a recolectar información y almacenarla dentro de un archivo json
execute()

print("\n")
print("\n")
print("Información guardada en el archivo books.json.")
print("Se empieza a estabecer la conexión con la base de datos")
print("\n")
print("\n")

#La siguiente función se conecta a la base de datos y crea el statement para guardar información en esta y luego le da commit para guardarla en la base de datos
realizarConexion()

