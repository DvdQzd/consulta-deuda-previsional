from consulta import Captura
from format_rut import Rut
from scraper import *
import connect as con
from time import sleep


ruts = con.get_ruts()

for rut in ruts:
    data = False
    rut = Rut.formatter(rut)
    tries = 0
    while(data == False and tries < 3):
        source = Captura.captura_datos(rut)
        data = Scraper.data_parser(source)
        tries += 1
        sleep(5)
    if(tries = 3):
        print("Ya fueron 3 intentos. Ahorraremos Captchas para despues.")
    if(data):
        con.insert_data(data)




