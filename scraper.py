import bs4 as bs
import urllib.request

class Scraper:

    def data_parser(source):
        # sauce = open('test.html').read()
        sauce = source
        soup = bs.BeautifulSoup(sauce, "html.parser")
        msg = soup.find("div").text.strip()
        print("Respuesta " + msg)
        if(msg == "Debe comprobar que Ud. no es un robot"):
            print("Lo intentaremos de nuevo...")
            return False
        print("Pasemos al siguiente...")
        return True