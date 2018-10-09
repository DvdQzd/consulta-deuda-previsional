import bs4 as bs
import urllib.request
from time import sleep

class Scraper:

    def data_parser(source):
        sauce = source
        soup = bs.BeautifulSoup(sauce, "html.parser")
        msg = soup.find("div").text.strip()
        if(msg == "Debe comprobar que Ud. no es un robot"):
            print("El sitio cree que soy un robot...")
            print("Intentaremos de nuevo en 5 segundos...")
            sleep(5)
            return False
        elif 'no registra Cotizaciones Impagas' in msg:
            print("El RUT no registra Cotizaciones Impagas.")
            return True
        else:
            try:
                deudas = soup.find("div").table.find_all("tr")
                deudas.pop(0) # Eliminamos la fila con los titulos de la tabla
                response = []
                data = []
                for row in deudas: 
                    columns = row.find_all("td")
                    lista = []
                    for column in columns:
                        if(column.string.strip() != ""):
                            lista.append(column.string.strip())
                    response.append(lista)     

                return response
            except:
                print("La pagina no se encuentra disponible...")
                print("Intentaremos de nuevo en 5 segundos...")
                sleep(5)
                return False
            