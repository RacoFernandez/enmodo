# `enmodo`: Análisis y visualización de las Encuestas Origen Destino (EODs) de diferentes ciudades de Latinoamérica

# Estructura del repositorio

Hay una carpeta por ciudad. Si se incluyeron diferentes años de las ENMODO para 1 ciudad, va a haber una subcarpeta por cada año para la misma ciudad (ej. Bogotá).

### Source

Cada ciudad tiene subcarpetas llamadas `source-{file_extension}` que varían dependiendo el tipo de archivo que haya publicado la ciudad con los datos de la ENMODO.

### Output

Cada ciudad tiene carpetas con nombre de extensión ej. `csv` donde hay un output por diferentes tipos de extensión.

### Procesamiento

En las carpetas `python` se encuentra 1 notebook por cada ciudad-año con el procesamiento de los indicadores, diferentes visualizaciones y la generación de los archivos de output.

# Ejecución notebooks

Para ejecutar las notebooks de manera local, luego de clonar el repositorio, en la notebook que se utilice reemplazar la líneas donde se define el objeto `data_path` por el path local

```python
# Reemplazar el string por el path local correspondiente
data_path = '/home/roliverio/Documentos/ADDI/enmodo/bogota/'
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

[Alcaldía Mayor de Bogotá. Sistema integrado de información sobre Movilidad Urbana Regional. Encuesta de Movilidad Bogotá 2019.](https://www.simur.gov.co/encuestas-de-movilidad)

### Buenos Aires

[Ministerio de Transporte - Programas y Proyectos Sectoriales y Especiales del Ministerio de Transporte - ENMODO](https://www.argentina.gob.ar/transporte/dgppse/publicaciones/encuestas)

### Ciudad de México

[Ciudad de México:  Instituto Nacional de Estadística, Geografía e Informática (INEGI). Encuesta Origen Destino en Hogares de la Zona Metropolitana del Valle de México (EOD) 2017](https://www.inegi.org.mx/programas/eod/2017/)

### Montevideo

* [Intendencia de Montevideo, Observatorio de Movilidad. Encuesta de movilidad del área metropolitana de Montevideo 2016](https://montevideo.gub.uy/observatorio-de-movilidad)
* [Intendencia de Montevideo, Observatorio de Movilidad. Encuesta de movilidad del área metropolitana de Montevideo 2009](https://montevideo.gub.uy/observatorio-de-movilidad)

### Santiago de Chile

[Subsecretaría de Transportes del Ministerio de Transportes y Telecomunicaciones (MTT), Programa de Vialidad y Transporte Urbano SECTRA. Encuesta Origen Destino Santiago 2012](http://www.sectra.gob.cl/encuestas_movilidad/encuestas_movilidad.htm)

### Sao Paulo

[Companhia do Metropolitano de São Paulo - Metrô. Pesquisa Origem e Destino Região Metropolitana de São Paulo 2017](https://www.metro.sp.gov.br/pesquisa-od/index.aspx)

# Contribuidores

- Paula Vásquez-Henríquez
- Ariel López
- Genaro Cuadros
- Exequiel Gaete
- Alba Vásquez
- Juan Correa
- Ramiro Oliverio Fernández

# Agradecimientos

El paquete [AVES](https://github.com/zorzalerrante/aves) ha sido de gran ayuda para el desarrollo de las visualizaciones y análisis de GIS.
