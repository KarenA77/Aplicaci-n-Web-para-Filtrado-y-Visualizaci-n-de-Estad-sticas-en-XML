Este proyecto presenta un sistema web para la visualización y gestión de estadísticas en formato XML. Utiliza Django y Flask para implementar un sistema en arquitectura Cliente-Servidor, donde Django maneja el backend y Flask facilita el manejo de solicitudes ligeras en el frontend. El sistema permite la organización, filtrado y presentación de datos en archivos XML, con visualización lado a lado del archivo original y del archivo modificado para mejorar la accesibilidad de la información.

Requerimientos Mínimos

* Python 3.x: Lenguaje principal de desarrollo.
* Frameworks Web:
- Django para el backend, empleando un patrón Modelo-Vista-Controlador (MVC).
- Flask para el frontend, facilitando las interacciones específicas y ligeras con el servidor.
* Biblioteca XML (xml.etree.ElementTree): Para el manejo de datos en formato XML.
* Graphviz: Para la creación de diagramas en forma de árbol, que representan visualmente las consultas.
  
Ejecución
Iniciar el servidor Flask: python app.py
Iniciar el servidor Django: python manage.py runserver

