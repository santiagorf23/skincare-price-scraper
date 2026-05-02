import requests # le dices a Python que vas a usar esa librería.
import openpyxl
from datetime import datetime
from bs4 import BeautifulSoup

def obtener_pagina(url): #  defines una función que recibe una URL como parámetro. Así puedes reutilizarla con cualquier página, no solo una.
    respuesta = requests.get(url) # aquí Python sale a internet, llama a esa URL y guarda todo lo que el servidor responde.
    respuesta.encoding = respuesta.apparent_encoding # apparent_encoding le dice a requests que detecte automáticamente la codificación correcta del texto en lugar de asumir una.

    if respuesta.status_code == 200: # antes de seguir, verificas que la solicitud funcionó. Si el servidor devolvió algo distinto a 200, no tiene sentido intentar extraer datos de una respuesta vacía o de error.
        return respuesta.text # devuelves el HTML como texto para que otras funciones lo puedan usar después.
    else:
        print(f"Error al acceder a la pagina: {respuesta.status_code}")
        return None

def extraer_productos(html):
    soup = BeautifulSoup(html, "html.parser") # convierte el texto HTML crudo en un objeto navegable. A partir de aquí puedes hacer preguntas sobre la estructura.
    productos = []

    articulos = soup.find_all("article", class_= "product_pod") #  le preguntas: "encuéntrame todos los elementos article que tengan la clase product_pod". Cada uno de esos es un producto en la página.

    for articulo in articulos: # recorres cada producto uno por uno.
        nombre = articulo.find("h3").find("a")["title"] # dentro del artículo, buscas el h3, luego el a que está dentro, y lees su atributo title. Ahí está el nombre completo del producto.
        precio = articulo.find("p", class_= "price_color").text.strip() # buscas el párrafo con clase price_color y lees su texto. .strip() elimina espacios o saltos de línea sobrantes.

        productos.append({ # cada producto lo guardas como un diccionario con nombre y precio, y lo agregas a la lista.
            "nombre": nombre,
            "precio": precio
        })

    return productos

def guardar_excel(productos):
    wb = openpyxl.Workbook() # crea un archivo Excel nuevo en memoria, todavía no en disco.
    hoja = wb.active # accede a la primera hoja que todo Excel trae por defecto.
    hoja.title = "Productos"
    
    hoja.append(["Nombre", "Precio", "Fecha de extraccion"]) # agrega una fila. La primera llamada crea los encabezados, las siguientes agregan un producto por fila.
    
    for producto in productos:
        hoja.append([
            producto['nombre'],
            producto['precio'],
            datetime.now().strftime("%Y-%m-%d %H:%M") # agrega la fecha y hora exacta en que se extrajo el dato. Esto es clave para el proyecto real: cuando monitorees precios de skincare a lo largo del tiempo, necesitas saber cuándo se registró cada precio.
        ])
        
    nombre_archivo = f"data/productos_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx" # el nombre del archivo incluye la fecha y hora, así cada vez que ejecutes el scraper genera un archivo nuevo sin sobreescribir el anterior.
    wb.save(nombre_archivo)
    print(f"Archivo guardado: {nombre_archivo}")

'''
if __name__ == "__main__": — esto es una buena práctica importante. 
Significa: "este bloque solo se ejecuta cuando corres este archivo directamente". 
Si en el futuro importas este archivo desde otro script, este bloque no se ejecuta accidentalmente.
'''

if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    html = obtener_pagina(url)
    
    if html:
        productos = extraer_productos(html)
        print(f"Productos encontrados: {len(productos)}")
        guardar_excel(productos)