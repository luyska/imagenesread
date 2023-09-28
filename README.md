# ImgCompressCRPython

## Instalación
Esta sección muestra como instalar el paquete **ImgCompressCRPython**.
---
Para instalar el paquete es necesario crear un entorno virtual:
```terminal
python -m venv venv
env\Scripts\activate
pip install -r python -m venv venv
```
Para utilizarlo solo debe importar las funciones al inicio de su módulo

```python
from ImgCompressCRPython.compress import compress_image 
from ImgCompressCRPython.compress import resize_image
```

## Usos

Esta biblioteca cuenta cond dos funciones:

1. compress_image
2. resize_image

Para comprimir una imagen en la ruta /images/prueba.jpg se debería llamar a al función de la siguiente forma:
```python
from ImgCompressCRPython.compress import compress_image
path = "/images/prueba.jpg"
dest_path = "/images/prueba-compressed.jpg"
compress_image(path, dest, uquality=60, uoptimize=True)
```

## Referencias

Para ver el código fuente vaya a nuestro repositorio de [GitHub](https://github.com/luyska/image_compress).

## Imagenes de prueba
![Imagen de prueba](https://images.pexels.com/photos/18336090/pexels-photo-18336090/free-photo-of-ensayo-femenino.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

> "Veni, vidi, vici

