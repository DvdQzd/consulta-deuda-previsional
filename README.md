# Consulta de Deuda Previsional

Esta aplicación recibe una lista de RUTs, ingresa a https://www.spensiones.cl/apps/certificados/formConsultaDeuda.php, pasa el captcha de google usando [2capcha](https://2captcha.com/) y envía un POST con cada rut, descargando el html con la deuda previsional de cada uno, luego deberá guardar los datos parseados en un archivo o una base de datos.

[2capcha](https://2captcha.com/) es un servicio de pago, el cual entrega una API_KEY, la cual debe agregarse en el archivo `keys.py`. 
Luego de agregar la API_KEY, utilizar el comando `py start.py`

Este es un trabajo en proceso. Actualmente estoy trabajando en el scraper y en el manejo de excepciones.
