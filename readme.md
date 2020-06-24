# MLAlertas

Un sencillo programa en python para monitorear las ventas de un producto en MercadoLibre, cada vez que se incrementa el contador de vendidos envia un mensaje en Pushbullet.

## Instalacion

- Requests
```bash
pip3 install requests
```
- BeautifulSoup
```bash
pip3 install beautifulsoup4
```
- Pushbullet
```bash
pip3 install pushbullet.py
```

## Configuración

El programa solo utiliza un archivo json donde almacena los parametros de configuracion, y la cantidad de productos vendidos para
comparar.
Tiene la siguiente estructura:
```json
{
    "APIKEY": "API_KEY_PRODUCTOS", 
    "cantidad": 0, 
    "URL": "URL DEL PRODUCTO DE ML"
}
```

## Ejecución

Recomiendo configurar para que se ejecute por medio de cron cada hora o dos horas, dependiendo la frecuencia que se necesite. Aqui un ejemplo de como agregar a la linea para que se ejecute cada hora.
```
0 * * * * python3 /path/MLAlertas.py
```

En la siguiente web pueden encontrar más ejemplos de configuraciones de cron: [crontab guru](https://crontab.guru/examples.html)
