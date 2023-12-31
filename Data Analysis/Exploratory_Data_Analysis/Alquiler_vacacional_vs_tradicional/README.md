📚 Contexto

Debido al gran auge de los pisos turisticos, se quiere comprobar si de verdad son mas rentables frente al alquiler tradicional, con la idea de invertir en el parque inmobiliario de la ciudad de Valencia y sacar la mayor rentabilidad posible a la inversion.

📝 Contenido

### **Obtención de los datos**

- Datos alquileres Airbnb csv obtenidos de http://insideairbnb.com/get-the-data/ y https://datahippo.org/es/region/599232358a46554f807aef06/

- precios alquiler y venta webscraping El idealista

- Geojson de barrios obtenido del ayuntamiento de Valencia

- Geojson de distritos obtenido de https://code.montera34.com/airbnb/valencia/tree/master/data/original/shapes

- Datos superficie media por distrito obtenidos de https://www.abc.es/espana/comunidad-valenciana/abci-superficie-media-vivienda-distritos-valencia-200112030300-63541_noticia.html

- Datos de ocupacion media Airbnb obtenidos de https://pegv.gva.es/es/temas/servicios/turismo/encuestadeocupaciondealojamientosturisticos

### **Limpieza de los datos**

Se decide partir el trabajo en una coleccion de notebooks para que sea mas facil acceder y tratar los datos:

   - insideairbnb: notebook prinipal donde se van a tratar los datos de Airbnb
   - metros_cuadrados: notebook donde guardamos la informacion obtenida del articulo del ABC
   - precios_alquileres: notebook donde guardamos la informacion de precios de alquiler del ayuntamiento de Valencia
   - datos_idealista: notebook donde guardamos y procesamos la informacion obtenida de la pagina del idealista
   - final: Notebook donde se cargan los csv despues de limpiarlos por separado para trabajar con los datos juntos y obtener medias y valores para realizar la comparación
   - mapa_barrios: notebook donde creamos el mapa de distritos y al ser tantos barrios, se decide trabajar con distritos
   - mapa_distritos: notebook donde creamos el mapa de distritos y limpiamos los datos para quedarnos con los distritos que nos interesan
   - mapa choropleth: notebook, donde una vez tratados los datos se crean los mapas finales.

Una vez hecha la division, comienza el procesado de los datos:

- **insideairbnb**: cargamos el csv descargado y lo visualizmos, al visualizarlo vemos que hay varias columnas que no nos van a servir, por lo que con un drop las quitamos, despues les cambiamos el nombre al castellano y hacemos un primer histograma para visualizar la distribucion de los datos. Una vez visualizados empezamos a filtrar los datos, ya que para hacer la comparativa nos interesan solo los alojamientos con un numero de noches minimas no superior a 30 para comparar en igualdad de condiciones con el alquiler tradicional, ademas se ponen las columnas donde despues vamos a agrupar y comparar en minuscula. Despues se añade una nueva columna con el precio final del alojamiento teniendo en cuenta el precio por noche y numero minimo de noches. A continuacion se eliminan 3 distritos para quedarnos con el mismo numero de distritos que tenemos en los datos del idealista. A continuacion separamos el csv en 16 csv diferentes para buscar valores anomalos con diagramas de cajas, y scatterplot descubriendo varios outlayers en los distritos de ciutat vella y l'eixample, eliminandolos al considerarlos errores que debieron cometer los propietarios al introducir el precio/noche, el resto de distritos pese a presentar valores que podrian considerarse outlayers, no se alejan tanto y se deciden dejar ya que podria ser simplemente que el propietario ha decidido poner un precio alto debido a las comodidades que ofrece.

- **metros_cuadrados**: se intenta scrapear la web, pero debido a las faltas de redacción que imposibilitan la separacion de distritos y precios en listas separadas se decide tomar los datos de forma manual guardandolos en un csv para importarlo y trabajar con ellos.

- **datos_idealista**: debido a lo complicado del scrapeo ya que no se tienen todos los datos distribuidos de forma igual, algunos incluso faltantes (que se completan a posteriori con el csv obtenido de la pagina del ayuntamiento de valencia) y al de ser pocos datos se toman de forma manual guardandolos en un csv para importarlo y trabajar en ellos

### **Representación de gráficos**

Una vez ya todos los datos limpios procedemos a pulir algunos graficos ya generados mientras se hacia el tratamiento de los datos para ayudarnos con la limpieza visualizando los datos en graficas, igualando el estilo a los graficos generados con los datos limpios para poder hacer una comparacion del antes y despues. tambien pasamos a generar mapas choropleth para una representacion mas visual de los datos obtenidos, ademas de colorear y añadir leyendas al mapa de  distritos y se realiza un mapa de distritos con los aribnb que han quedado despues de la limpieza.