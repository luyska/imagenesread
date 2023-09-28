.. ImgCompressCRPython documentation master file, created by
   sphinx-quickstart on Mon Sep 25 20:07:10 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

====================
ImgCompressCRPython.
====================

Bievenidos a documentación de la biblioteca 

***********
Instalación
***********

.. code-block:: python

   python -m venv venv
   env\Scripts\activate
   pip install -r python -m venv venv

Para utilizarlo solo debe importar las funciones al inicio de su módulo


.. code-block:: python

   from ImgCompressCRPython.compress import compress_image 
   from ImgCompressCRPython.compress import resize_image


****
Usos
****

Esta biblioteca cuenta cond dos funciones:

1. compress_image
2. resize_image

Para comprimir una imagen en la ruta /images/prueba.jpg se debería llamar a al función de la siguiente forma:

.. code-block:: python

   from ImgCompressCRPython.compress import compress_image
   path = "/images/prueba.jpg"
   dest_path = "/images/prueba-compressed.jpg"
   compress_image(path, dest, uquality=60, uoptimize=True)

************************
Referencias a sitios web
************************

Para ver el código fuente vaya a nuestro repositorio de `GitHub`_.

.. _`Github`: https://github.com/luyska/image_compress


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
