from consulta import Captura
from format_rut import Rut
from scraper import *


ruts = ["96806980-2", "90635000-9", "96799250-K"]

for rut in ruts:
    rut = Rut.formatter(rut)

    robot = False

    while(robot == False):
        source = Captura.captura_datos(rut)
        robot = Scraper.data_parser(source)



