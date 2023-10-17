# Sistema de Recomendación

Este es un sistema de recomendación que utiliza tres métricas diferentes y dos métodos de predicción para predecir las valoraciones de los usuarios. El sistema está diseñado para ayudar a los usuarios a encontrar recomendaciones basadas en sus preferencias y datos de entrada.

## Descripción

Este programa es un sistema recomendador que utiliza métricas para predecir la valoración de un usuario. Toma un archivo de datos de entrada (archivo.txt) que contiene información sobre las valoraciones de los usuarios y utiliza varias métricas y métodos de predicción para ofrecer recomendaciones personalizadas.

## Requisitos

El sistema de recomendación requiere la instalación de las siguientes bibliotecas de Python:

- [tabulate](https://pypi.org/project/tabulate/): Para formatear y mostrar datos en forma de tabla.
- [termcolor](https://pypi.org/project/termcolor/): Para agregar color a la salida de la consola.

Puedes instalar estas bibliotecas utilizando pip:

```shell
pip install tabulate termcolor
```

## Ejecución

Para ejecutar el sistema de recomendación, sigue estos pasos:

1. Abre una terminal.

2. Ejecuta el programa recommender_system.py proporcionando el archivo de datos de entrada como argumento:

```shell
python recommender_system.py <nombre_archivo>.txt
```
1. El programa mostrará un menú para seleccionar una métrica y un método de predicción. Sigue las instrucciones en pantalla para hacer tus selecciones.

2. Después de realizar tus selecciones, el sistema generará recomendaciones basadas en las métricas y métodos de predicción elegidos.

3. La salida del sistema se mostrará en la consola y estará formateada como tablas con colores.

## Argumentos

```<nombre_archivo>.txt```: El archivo que contiene los datos de entrada para el sistema recomendador.

+ Este archivo tiene el siguiente aspecto: 

```txt
0.000
5.000
0.678 4.460 - - 2.512 - 0.266 4.778 - 0.457 
3.769 1.624 - - 3.983 4.776 1.687 2.473 1.052 1.049 
3.541 4.815 - 4.884 - 2.396 - 4.169 0.582 - 
3.778 1.152 - 2.424 1.202 - - - 3.940 2.451 
0.183 3.793 1.195 2.069 - 0.951 0.358 - - 2.351 
```

En las 2 primeras líneas tenemos los límites inferiores y superiores de las puntuaciones de los usuarios. En las líneas sucesivas podemos encontrar la matriz de valoraciones incompleta, ya que la idea es predecir los valores vacíos que se representan con "-"
