# Informatorio-Data-ProyectoFinal-1-2023

Nivel inicial:


1. Obtener el archivo de la fuente que escojamos archivos de fuente utilizando Google Colab y la librería requests, por último debe almacenarse en forma local en formato CSV:

Librerias necesarias:

from datetime import datetime
import requests
import pandas as pd
from pandas import json_normalize
import json

### API de datos abiertos del clima:

Descripción: Algunas APIs públicas proporcionan datos históricos o en tiempo real sobre el clima, incluidas temperaturas, precipitaciones, vientos, etc.
API: [https://openweathermap.org/api](https://openweathermap.org/api)

2. Solicitud: Debes hacer una solicitud HTTP a la API para obtener los datos en formato JSON y luego convertirlos a CSV utilizando Python.

BASE_URL = "[https://api.openweathermap.org/data/2.5/weather](https://api.openweathermap.org/data/2.5/weather)[&#34;](https://api.openweathermap.org/data/2.5/onecall/timemachine?%22)


3. Organizar los archivos en rutas siguiendo la siguiente estructura:
   “data_analytics\openweather\tiempodiario_yyyymmdd.csv”
   La fecha de la nomenclatura es la fecha del tiempo tomado.

4. buscar estas ciudades:

cityList = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
coordList = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]

5. Realizar los comentarios correspondientes para una correcta comprensión del código. (#)
