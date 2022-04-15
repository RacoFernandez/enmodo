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

# Fuentes

### Bogotá

### Buenos Aires

### Ciudad de México

### Montevideo

### Santiago de Chile

### Sao Paulo

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
