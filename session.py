import bs4 as bs
import urllib.request


def get_session_id():
    sauce = urllib.request.urlopen('https://www.spensiones.cl/apps/certificados/formConsultaDeuda.php')
    soup = bs.BeautifulSoup(sauce, 'html.parser')

    session_id = soup.find('input', {'name': 'sessionid'})['value']

    return session_id
