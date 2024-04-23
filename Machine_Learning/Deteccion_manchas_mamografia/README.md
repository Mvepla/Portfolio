📚 Contexto.

Según los últimos datos recogidos por la Sociedad Española de Oncología Médica (SEOM), en 2024 se diagnosticarán 36.395 nuevos casos de cáncer de mama, siendo este tipo de tumor más frecuente entre las mujeres en nuestro país por delante del cáncer colorrectal, de pulmón, cuerpo uterino, tiroides y páncreas. En España, aproximadamente el 30% de los cánceres diagnosticados en mujeres se originan en la mama. El cáncer de mama es ya el tumor más diagnosticado del mundo, superando por primera vez al cáncer de pulmón, según datos publicados en 2021 por el Centro de Investigaciones sobre el cáncer (IARC, por sus siglas en inglés).

En cuanto a la tasa de incidencia, se estiman 132 casos por cada 100.000 habitantes. La probabilidad estimada de desarrollar cáncer de mama siendo mujer es de 1 de cada 8. Este tipo de tumor suele aparecer entre los 35 y los 80 años, aunque la franja de los 45-65 es la de mayor incidencia, al ser el momento en el que se producen los cambios hormonales en los períodos de peri y post menopausia, una curva de incidencia que continúa aumentando a medida que la mujer envejece.


📝 Descripción.

Las mamografías habituales son las mejores pruebas con que cuentan los médicos para detectar el cáncer de mama en sus etapas iniciales. Una mamografía es una imagen de la mama tomada con rayos X. Los médicos usan las mamografías para buscar signos de cáncer de mama en sus etapas iniciales, que se pueden ver en forma de manchas dentro de la imagen de la mama.

📝 Objetivo.

Este proyecto Tiene la idea de facilitar la detección de cáncer de mama mediante el calculo del área de una mancha vista en una mamografía. Para ello se utiliza la libreria OpenCV para realizar tratamiento de imágenes de RX en las cuales se ven los posibles nódulos cancerígenos en forma de manchas, por lo que interesa poder medir el área de las manchas para poder tener una idea del tamaño.

📝 Contenido.

La estructura de este trabajo es la siguiente:

    - detector.ipynb: notebook donde esta todo el código en una misma celda con comentarios sobre las partes y donde se puede ejecutar para comprobar su funcionamiento.
    - mamografia.png: mamografia donde queremos medir las manchas.
    - mamografia_con_poligono.jpg: mamografia procesada, donde se marcamos los posibles nódulos cancerígenos en forma de polígono y el área de las mancha delineada con el polígono.