# Consulta de Deuda Previsional

Esta aplicación recibe una lista de RUTs, ingresa a https://www.spensiones.cl/apps/certificados/formConsultaDeuda.php, pasa el captcha de google usando [2capcha](https://2captcha.com/) y envía un POST con cada rut, descargando el html con la deuda previsional de cada uno, luego deberá guardar los datos parseados en un archivo o una base de datos.

## Requisitos

- Python 3.7

## Instalación

Para instalar las dependencias necesarias, ejecutar los siguientes comandos:

- `pip install -r requirements.txt`
- `cp keys_example.py keys.py`

Y luego agregar los datos necesarios en `keys.py`

## Uso

Luego de ingresar los datos necesarios en `keys.py`, ejecutar el comando `python start.py`

---

[2capcha](https://2captcha.com/) es un servicio de pago, el cual entrega una API_KEY, la cual debe agregarse en el archivo `keys.py`.

