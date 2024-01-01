
# Portfolio de Data Science

¡Bienvenido a mi portfolio de Data Science! Aquí encontrarás una variedad de proyectos de Exploratory Data Analysis, Webscrapping, Machine Learning tradicional y Deep Learning

## Data Analysis
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Exploratory Data Analysis

### Proyecto 1: Análisis exploratorio de datos en alquiler vacacional vs tradicional

Debido al gran auge de los pisos turísticos, se quiere comprobar si de verdad son mas rentables frente al alquiler tradicional, con la idea de invertir en el parque inmobiliario de la ciudad de Valencia y sacar la mayor rentabilidad posible a la inversión. Bibliotecas utilizadas: Pandas, Numpy, Matplotlib, Seaborn, Folium

![Informe en PDF](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/Exploratory_Data_Analysis/Alquiler_vacacional_vs_tradicional/EDA.pdf "Informe en PDF")

## Power BI

### Proyecto 1: Operaciones inmobiliarias

Dashboard interactivo sobre operaciones inmobiliarias en diferentes ciudades de Europa, con una serie de filtros integrados para que faciliten la visualización.

![Operaciones inmobiliarias](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/operaciones%20inmobiliarias.gif)

### Proyecto 2: Distribución de conservas de frutas por Argentina

Dashboard minimalista para una empresa de conservas de fruta argentina (FruitFresco), ayudando a la toma de decisiones para ubicar su nuevo punto de distribucion para todo el pais de manera que se pueda realizar una distribución mas efectiva y disminuyendo los costes de distribución, ademas de presentar las ventas por mes y por producto.

![Distribución geográfica](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/Distribucion%20de%20conservas%20de%20fruta%20FruitFresco.PNG)

### Proyecto 3: Análisis ventas cadena supermercados en diferentes regiones

Dashboard con dos perspectivas, una atendiendo al desempeño de cada zona y sucursal y la segunda analizando el desempeño de cada producto en funcion de las ventas. Se ha creado  una jerarquia nueva para poder explorar mejor las regiones con sus correspondientes sucursales y añadido un boton de navegación entre perspectivas.

![Cadena supermercados](https://github.com/Mvepla/Portfolio/blob/main/Data%20Analysis/PowerBI/productos%20y%20sucursales.gif)

### Proyecto 4: Ventas comercio minorista ElectroMas

Dasboard con dos perspectivas y con gama cromatica corporativa de la empresa ElectroMas. La primera perspectiva muestra ventas totales y su tendencia a lo largo del tiempo, así como su distribución en los canales de venta (tiendas físicas u online) y un mapa para conocer geográficamente dónde se concentran sus clientes. En la segunda perspectiva, se muestra como se comparan las diferentes categorías de productos entre sí, respecto a la cantidad de unidades vendidas.

![Cadena supermercados]()

## Machine Learning
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Proyecto 1: Detector de agua potable

El acceso al agua potable es esencial para la salud, un derecho humano básico y un componente de una política eficaz de protección de la salud. Es importante como cuestión de salud y desarrollo a nivel nacional, regional y local. En algunas regiones, se ha demostrado que las inversiones en abastecimiento de agua y saneamiento pueden reportar un beneficio económico neto, ya que la reducción de los efectos adversos para la salud y de los costes de atención sanitaria supera los costes de realizar las intervenciones. En este proyecto se han utilizado técnicas de Machine Learning tradicional del tipo de clasificación, probando cual era la mejor opción realizando una serie de pipes para optimizar cada modelo propuesto, una vez cada modelo optimizado se ha comprobado cual es el mejor y por ultimo un voting, siempre buscando la forma de obtener la mejor accuracy. El modelo esta implementado en una app de Flask para introducir los datos y realizar predicciones, también se realizará un registro de las predicciones, con la fecha y hora que se ha realizado la predicción y se guardara en una base de datos tipo Postgress alojada en el mismo servicio. Para realizar predicciones y poder revisar la base de datos haz click en el siguiente link: https://app-water-dev-kpgs.2.ie-1.fl0.io/


### Proyecto 2: Detección de especies de tiburón mediante Deep Learning

Proyecto de detección de especies de tiburón mediante Deep Learning, utilizando métodos de computer vision con un modelo secuencial con varias capas convolucionales y densas, con la idea de evolucionar el proyecto hacia un modelo de reconocimiento de especies de tiburón a través de video en tiempo real, para realizar las predicciones, al no tener que acceder ni registrar nada en una base de datos se ha abierto una app en streamlit para subir las imágenes y realizar la prediccion. https://identificador-tiburones.streamlit.app/

![Informe en PDF](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Identificador_tiburones_Deep_Learning/ML_ppt.pdf "Informe en PDF")

## Tecnologías Utilizadas

- Python
- Bibliotecas: NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn, Tensorflow,  etc.
- Jupyter Notebooks
- Power BI
- Web scrapping
- Streamlit

## Contacto

¡Gracias por explorar mi portfolio! Si tienes alguna pregunta o comentario, no dudes en contactarme:

- Correo Electrónico: miguel.vela.planas@gmail.com
- LinkedIn: [Perfil de LinkedIn](https://www.linkedin.com/in/miguel-vela/)