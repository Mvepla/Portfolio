📚 Contexto

Proyecto de detección de especies de tiburón mediante Deep Learning, el objetivo es poder identificar las diferentes especies de tiburon mediante una imagen para despues, una vez el modelo tenga una buena accuracy, evolucionar el proyecto hacia un modelo de reconocimiento de especies de tiburón a través de video en tiempo real, tomando todos los frames como imagenes para pasarselo al modelo, identificarlo y poder hacer un seguimiento en tiempo real.

📝 Contenido

Para el modelo de reconocimiento de especies de tiburon se han utilizado 1904 imagenes, obtenidas de un repositorio en linea y realizando web scraping para intentar aumentas el numero de imagenes.

Se ha utilizado un modelo secuencial con capas convolucionales y densas propio, despues se utilizo el modelo Resnetv2 ya preentrenado para comprobar si mejoraba el accuracy, por ultimo para intentar mejorar el accuracy se ha utilizado Open CV para filtrar las imagenes y definir mejor el contorno de los animales para que el modelo pueda capturar mejor la forma, como se ha explicado se han realizado multitud de pruebas obteniendo los siguientes resultados:

| Diseño modelo | Accuracy modelo |
|--------------|--------------|
| 3 capas Conv 64, dense 180,100  | 0,1645    |
| Resnetv2, dense 180 y 100    | 0.0574    |
| Conv 64, Conv 32, dense 100, lr=0.00001   | 0.1410    |
| Conv 32, 2 capas Conv 64, dense 100, lr=0.00001, filtro Canny    | 0.1875    |
| 3 capas Conv 64, dense 100 y 180, lr=0.00001, filtro Canny     | 0.2422    |


El camino es prometedor, ya que se ha ido mejorando el accuracy del modelo, pero se necesitan mas imagenes para poder entrenar el modelo y llegar a un accuracy aceptable para poder implementar el reconocimiento en el modelo de seguimiento de indiciduos en tiempo real.