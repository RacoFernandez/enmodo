# `enmodo`: Análisis y visualización de las Encuestas Origen Destino (EODs) de diferentes ciudades de Latinoamérica

# Estructura del repositorio

Existe una carpeta por ciudad. Si se incluyeron diferentes años de las ENMODO para 1 ciudad, va a haber una subcarpeta por cada año para la misma ciudad (ej. Bogotá).

### Source

Cada ciudad tiene subcarpetas llamadas `source-{file_extension}` que incluyen los datos que se publicaron como fuentes oficiales de las ENMODO. El `{file_extension}` varía dependiendo el tipo de archivo que haya utilizado la ciudad para publicar la ENMODO.

### Output

Cada ciudad tiene carpetas llamadas `output-{file_extension}` o sólo con nombre de extensión ej. `csv` donde hay un output por diferentes tipos de extensión con los datos procesados de la ENMODO, tanto en .shp, .geojson y .csv

### Procesamiento

En las carpetas `python` se encuentra 1 notebook por cada ciudad-año con el procesamiento de los indicadores, diferentes visualizaciones y la generación de los archivos de output. Este es el core del repositorio, donde esta el código que utiliza y genera los datos del mismo.

# Ejecución notebooks

Todas las notebooks consumen los datos publicados en este repositorio de Github, por lo cual las notebooks pueden correrse fácilmente luego de instalar las dependencias. Lo único que se debe reemplazar es el objeto `data_path` por el directorio donde se haya clonado el repositorio para luego poder importar el script `eod_analysis.py` con las siguientes celdas.

```python
# Si se está en google colab, reemplazar por path de Drive
data_path = 'C:/Users/Usuario/Documents/GitHub/enmodo/'
```

```python
import sys

# Si se está en google colab, reemplazar por path donde tiene la carpeta "scripts"
sys.path.insert(1, data_path +'scripts')

import eod_analysis as eod
```

### Google colab

En caso de utilizar google colab para ejecutar las notebooks, descomentar y ejecutar las 3 primeras celdas en cada notebook:

```python
# Instalamos dependencias necesarias para correr en Google colab
!pip3 uninstall matplotlib -y
!pip install -q condacolab
import condacolab
condacolab.install()
```

```python
#Esta celda clona el repositorio AVES que se utiliza para visualizaciones GIS
!git clone https://github.com/zorzalerrante/aves.git aves_git
!mamba env update --name base --file aves_git/environment-colab.yml
```

```python
# Montando datos desde Google Drive
from google.colab import drive
drive.mount('/content/drive')
```

Para posteriormente reemplazar `data_path` en vez del path del directorio local, por el path correspondiente de drive. [Referencia](https://neptune.ai/blog/google-colab-dealing-with-files)

> :warning: Las funcionalidades del paquete `AVES` solo pueden ejecutarse en Google Colab, por lo cual ciertas celdas que generan algunas de las visualizaciones de las notebooks pueden arrojar error al correrlas de manera local. Próximamente este issue quedará resuelto.

# Fuentes

### Bogotá

* [Alcaldía Mayor de Bogotá. Sistema integrado de información sobre Movilidad Urbana Regional. Encuesta de Movilidad Bogotá 2019.](https://www.simur.gov.co/encuestas-de-movilidad)

### Buenos Aires

* [Ministerio de Transporte - Programas y Proyectos Sectoriales y Especiales del Ministerio de Transporte - ENMODO](https://www.argentina.gob.ar/transporte/dgppse/publicaciones/encuestas)

### Ciudad de México

* [Ciudad de México:  Instituto Nacional de Estadística, Geografía e Informática (INEGI). Encuesta Origen Destino en Hogares de la Zona Metropolitana del Valle de México (EOD) 2017](https://www.inegi.org.mx/programas/eod/2017/)

### Montevideo

* [Intendencia de Montevideo, Observatorio de Movilidad. Encuesta de movilidad del área metropolitana de Montevideo 2016](https://montevideo.gub.uy/observatorio-de-movilidad)
* [Intendencia de Montevideo, Observatorio de Movilidad. Encuesta de movilidad del área metropolitana de Montevideo 2009](https://montevideo.gub.uy/observatorio-de-movilidad)

### Santiago de Chile

* [Subsecretaría de Transportes del Ministerio de Transportes y Telecomunicaciones (MTT), Programa de Vialidad y Transporte Urbano SECTRA. Encuesta Origen Destino Santiago 2012](http://www.sectra.gob.cl/encuestas_movilidad/encuestas_movilidad.htm)

### Sao Paulo

* [Companhia do Metropolitano de São Paulo - Metrô. Pesquisa Origem e Destino Região Metropolitana de São Paulo 2017](https://www.metro.sp.gov.br/pesquisa-od/index.aspx)

# Contribuidores

- Paula Vásquez-Henríquez
- Ariel López
- Genaro Cuadros
- Exequiel Gaete
- Alba Vásquez
- Juan Correa
- Ramiro Oliverio Fernández

# Agradecimientos

- El paquete [AVES](https://github.com/zorzalerrante/aves) elaborado por [@zorzalerrante](https://github.com/zorzalerrante) ha sido de gran ayuda para el desarrollo de las visualizaciones y análisis GIS.

- El repositorio de Sebastián Anapolsky con el análisis de la ENMODO de Buenos aires, disponible [aquí](https://github.com/sanapolsky/Analisis-Movilidad-AMBA)
