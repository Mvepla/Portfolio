
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=33&pause=1000&color=000000&center=true&vCenter=true&multiline=true&repeat=false&random=false&width=435&lines=Portfolio+Data+Science" alt="Typing SVG" /></a>

¡Bienvenid@ a mi portfolio de Data Science! Aquí encontrarás una variedad de proyectos de Exploratory Data Analysis, Webscrapping, Machine Learning tradicional y Deep Learning


# Data Analysis.


## Exploratory Data Analysis.


### Proyecto 1: Análisis exploratorio de datos en alquiler vacacional vs tradicional.

Debido al gran auge de los pisos turísticos, se quiere comprobar si de verdad son mas rentables frente al alquiler tradicional, con la idea de invertir en el parque inmobiliario de la ciudad de Valencia y sacar la mayor rentabilidad posible a la inversión. Bibliotecas utilizadas: Pandas, Numpy, Matplotlib, Seaborn, Folium.

[![PDF](https://img.shields.io/badge/PDF-Download-red?style=for-the-badge&logo=AdobeAcrobatReader)](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/Exploratory_Data_Analysis/Alquiler_vacacional_vs_tradicional/EDA.pdf)


## Power BI.


### Proyecto 1: Operaciones inmobiliarias.

Dashboard interactivo sobre operaciones inmobiliarias en diferentes ciudades de Europa, con una serie de filtros integrados para que faciliten la visualización.

![Operaciones inmobiliarias](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/operaciones%20inmobiliarias.gif)


### Proyecto 2: Distribución de conservas de frutas por Argentina.

Dashboard minimalista para una empresa de conservas de fruta argentina (FruitFresco), ayudando a la toma de decisiones para ubicar su nuevo punto de distribucion para todo el pais de manera que se pueda realizar una distribución mas efectiva y disminuyendo los costes de distribución, ademas de presentar las ventas por mes y por producto.

![Distribución geográfica](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/Distribucion%20de%20conservas%20de%20fruta%20FruitFresco.PNG)


### Proyecto 3: Análisis ventas cadena supermercados en diferentes regiones.

Dashboard con dos perspectivas, una atendiendo al desempeño de cada zona y sucursal y la segunda analizando el desempeño de cada producto en funcion de las ventas. Se ha creado  una jerarquia nueva para poder explorar mejor las regiones con sus correspondientes sucursales y añadido un boton de navegación entre perspectivas.

![Cadena supermercados](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/productos%20y%20sucursales.gif)


### Proyecto 4: Ventas comercio minorista ElectroMas.

Dasboard con dos perspectivas y utilizando la gama cromatica corporativa de la empresa ElectroMas. La primera perspectiva muestra informacion detallada en tarjetas, asi como un grafico de las cantidades vendidas y su tendencia a lo largo del tiempo, así como su distribución en los canales de venta (tiendas físicas u online) y un mapa para conocer geográficamente dónde se concentran sus clientes, se puede filtrar por cudad o fecha/hora. En la segunda perspectiva, se comparan las diferentes categorías de productos entre sí, respecto a la cantidad de unidades vendidas y el tipo de venta, además de una tabla detallada de cantidades por cada categoria y subcategoria con un filtro para entrar en detalle de las categorias mas vendidas en cada ciudad.

![ElectroMas](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/ElectroMas.gif)


# Machine learning.


### Proyecto 1: Detector de agua potable.

El acceso al agua potable es esencial para la salud, un derecho humano básico y un componente de una política eficaz de protección de la salud. Es importante como cuestión de salud y desarrollo a nivel nacional, regional y local. En algunas regiones, se ha demostrado que las inversiones en abastecimiento de agua y saneamiento pueden reportar un beneficio económico neto, ya que la reducción de los efectos adversos para la salud y de los costes de atención sanitaria supera los costes de realizar las intervenciones. En este proyecto se han utilizado técnicas de Machine Learning tradicional del tipo de clasificación, probando cual era la mejor opción realizando una serie de pipes para optimizar cada modelo propuesto, una vez cada modelo optimizado se ha comprobado cual es el mejor y por ultimo un voting, siempre buscando la forma de obtener la mejor accuracy. El modelo esta implementado en una app de Flask desplegada en el servicio fl0 para introducir los datos y realizar predicciones, también se realizará un registro de las predicciones, con la fecha y hora que se ha realizado la predicción y se guardara en una base de datos tipo Postgress alojada en el mismo servicio.


### Proyecto 2: Detección de especies de tiburón mediante Deep Learning.

Proyecto de detección de especies de tiburón mediante Deep Learning, utilizando métodos de computer vision con un modelo secuencial con varias capas convolucionales y densas, con la idea de evolucionar el proyecto hacia un modelo de reconocimiento de especies de tiburón a través de video en tiempo real, para realizar las predicciones, al no tener que acceder ni registrar nada en una base de datos se ha abierto una app en streamlit para subir las imágenes y realizar la prediccion. https://identificador-tiburones.streamlit.app/

[![PDF](https://img.shields.io/badge/PDF-Download-red?style=for-the-badge&logo=AdobeAcrobatReader)](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Identificador_tiburones_Deep_Learning/ML_ppt.pdf)

### Proyecto 3: Cálculo del área de un nódulo en mamografía.

Proyecto de detección y cálculo de área de manchas de una mamografía, el usuario define el contorno de la mancha mediante un polígono seleccionado mediante clicks de ratón.

![mamografia](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Deteccion_manchas_mamografia/mamografia.PNG)

![mamografia_con_area](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Deteccion_manchas_mamografia/mamografia_con_poligono.jpg)


### Proyecto 3: Seguimiento de tibrones en video.

Proyecto de seguimiento de animales, en este caso tiburones, mediante la libreria OpenCV. Al ser el video excesivamente pesado a continuación se muestra el resultado del modelo.

![Gif tiburones](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Seguimiento%20tiburones%20en%20video/demo.gif)


### Proyecto 4: Desafío tripulaciones.

El desafío de tripulaciones es la práctica integrada en la que trabajan los estudiantes de todas las disciplinas a través de un proyecto real. El proyecto sobre el que trabajamos las tres verticales es una web-app para el Colegio de Administradores de Fincas Valencia-Castellón. El enfoque del proyecto es mejorar la forma de trabajo de los administradores para poder ser mas eficientes en su trabajo, el proyecto se lleva a cabo junto a las otras 2 verticales, UX/UI y Fullstack. 

La parte de proyecto del grupo de Data Science se centra en realizar una API-REST para realizar un tratamiento de las actas de las reuniones de comunidad. Para ello se ha creado una api con flask que recibe como entrada un acta en formato pdf, este acta se transforma en texto y pasa a un modelo de Huggingface (facebook/bart-large.cnn) el cual hace un resumen. Una vez obtenido el resumen, para transcribirlo a audio pasa por un modelo Google Text-to-Speech (gTTs) que devuelve el contenido del resumen en un archivo mp3. Una vez tenemos el pdf, resumen y modelo se suben a la BBDD, para la BBD se usa MongoDB Atlas, que es un servicio de Cloud Database (o Base de Datos en la Nube)

# Talleres Bootcamp

### Taller Visualizaciones: ¿Nos mienten con los datos?

Taller para los alumnos de Data Science y UX/UI donde vemos como se puede manipular la percepción de un dato dependiendo de la visualizacion elegida.

### Taller PowerBI & Looker:

Taller para los alumnos de Data Science donde verremos dos programas para poder visualizar datos, uno es PowerBI y el otro es Looker, además verremos las diferentes maneras que tenemos para nutrir de datos ambos programas como excell y webscrapping para PowerBI y Bigquery de Google Cloud Plattform para Looker.

# Tecnologías Utilizadas.

- Python
- Bibliotecas: NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn, Tensorflow,  etc.
- Jupyter Notebooks
- Power BI
- Web scrapping
- Flask
- Streamlit
- Fl0
- AWS
- MongoDB

# Contacto.

¡Gracias por explorar mi portfolio! Si tienes alguna pregunta o comentario, no dudes en contactarme:

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:miguel.vela.panas@gmail.com)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-vela/)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Mvepla)
