import requests
from time import sleep, time
import keys
import session

class Captura(object):

    # print(self.rut)
    def captura_datos(rut):

        start_time = time()
        print("EL RUT A CONSULTAR ES: " + rut)
        captcha_key = keys.captcha_api_key
        google_key = "6LefRUMUAAAAAGtRLa7E4jdPmjq6smsHNzwZZN7P"
        page_url = "https://www.spensiones.cl/apps/certificados/formConsultaDeuda.php"
        method = "userrecaptcha"

        url="http://2captcha.com/in.php?key=" + captcha_key + "&method=" + method + "&googlekey=" + google_key + "&pageurl=" + page_url
        resp = requests.get(url) 
        print(resp.text)
        if resp.text[0:2] != 'OK':
            quit('Error. Captcha is not received')
        captcha_id = resp.text[3:]

        fetch_url = "http://2captcha.com/res.php?key=" + captcha_key + "&action=get&id=" + captcha_id
        for i in range(1, 20):	
            sleep(5) # wait 5 sec.
            resp = requests.get(fetch_url)
            if resp.text[0:2] == 'OK':
                break
                
        print("g-recaptcha-response: " + resp.text[3:])

        if(resp.text[3:] == "CAPCHA_NOT_READY"):
            print("Intentaremos de nuevo en 5 segundos...")
            sleep(5)
            pass
        if(resp.text[3:] == "ERROR_ZERO_BALANCE"):
            print("No queda debito en 2captcha.")
            raise Exception

        print('Time to solve: ', time() - start_time) 


        submit_url = "https://www.spensiones.cl/apps/certificados/consultaDeudaPrevisional.php"
        session_id = session.get_session_id()
        print("SessionId: " + session_id)

        headers = {
            'Host': 'www.spensiones.cl',
            'Connection': 'keep-alive',
            'Content-Length': '381',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://www.spensiones.cl',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.spensiones.cl/apps/certificados/formConsultaDeuda.php',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'es-US,es;q=0.9,es-419;q=0.8,en;q=0.7'
        } 

        payload = {
            'sessionid': session_id, 
            'rut': rut, 
            'g-recaptcha-response': resp.text[3:]
            }

        resp = requests.post(submit_url, headers=headers, data=payload)
        # print(resp.text)
        return resp.text

