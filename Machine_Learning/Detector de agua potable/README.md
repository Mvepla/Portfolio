# Predicción de Acceso al Agua Potable con Machine Learning

El acceso al agua potable es esencial para la salud, un derecho humano básico y un componente crucial de una política eficaz de protección de la salud. En este proyecto, se utilizan técnicas de Machine Learning para predecir el acceso al agua potable en diferentes regiones, lo que puede ayudar en la planificación de políticas de salud y desarrollo a nivel nacional, regional y local.

## Objetivo

El objetivo principal de este proyecto es utilizar técnicas de Machine Learning para predecir el acceso al agua potable en diferentes regiones. Esto se logra a través de un proceso de clasificación donde se entrenan varios modelos de Machine Learning utilizando datos históricos y se selecciona el modelo con mejor rendimiento.

## Métodos Utilizados

1. **Preprocesamiento de Datos:** Se realizó una limpieza y preparación de los datos para su posterior procesamiento en los modelos de Machine Learning.

2. **Selección de Modelos:** Se probaron varios modelos de clasificación de Machine Learning, como Regresión Logística, Support Vector Machines, Random Forest, entre otros, utilizando técnicas de optimización como la búsqueda de hiperparámetros para mejorar su rendimiento.

3. **Implementación de la Aplicación Web:** El modelo seleccionado se implementó en una aplicación web utilizando Flask, lo que permite a los usuarios introducir datos y obtener predicciones sobre el acceso al agua potable en una región específica.

4. **Registro de Predicciones:** Se realizó un registro de las predicciones realizadas por los usuarios, incluyendo la fecha y hora de la predicción, que se guarda en una base de datos tipo Postgres alojada en el mismo servicio.

## Estructura del Repositorio

- `data/`: Carpeta que contiene los datos utilizados para entrenar y probar los modelos de Machine Learning.
- `models/`: Carpeta que contiene los modelos entrenados guardados en formato `.pkl`.
- `app/`: Carpeta que contiene los archivos necesarios para la implementación de la aplicación web Flask.
- `notebooks/`: Carpeta que contiene los cuadernos Jupyter utilizados para el análisis de datos, la construcción y evaluación de modelos.
- `README.md`: Este archivo README que proporciona una descripción general del proyecto y cómo ejecutarlo.

## Contenido

El archivo `water_potability.csv` contiene parámetros de calidad del agua para 3276 masas de agua diferentes.

- **Valor del PH:** El PH es un parámetro importante para evaluar el equilibrio ácido-base del agua. También es el indicador del estado ácido o alcalino del agua. La OMS ha recomendado un límite máximo permisible de pH de 6,5 a 8,5. Los rangos de la investigación actual fueron de 6,52-6,83, que están dentro del rango de las normas de la OMS.

- **Dureza:** La dureza está causada principalmente por sales de calcio y magnesio. Estas sales se disuelven a partir de depósitos geológicos a través de los cuales viaja el agua. El tiempo que el agua está en contacto con el material que produce la dureza ayuda a determinar cuánta dureza hay en el agua bruta. La dureza se definió originalmente como la capacidad del agua para precipitar jabón causada por el Calcio y el Magnesio.

- **Sólidos (Sólidos totales disueltos - TDS):** El agua tiene la capacidad de disolver una amplia gama de minerales inorgánicos y algunos orgánicos o sales como potasio, calcio, sodio, bicarbonatos, cloruros, magnesio, sulfatos, etc. Estos minerales producen un sabor no deseado y diluyen el color en apariencia del agua. Este es un parámetro importante para el uso del agua. El agua con un alto valor de TDS indica que el agua está muy mineralizada. El límite deseable para TDS es de 500 mg/l y el límite máximo es de 1000 mg/l que se prescribe para beber.

- **Cloraminas:** El cloro y la cloramina son los principales desinfectantes utilizados en los sistemas públicos de agua. Las cloraminas se forman normalmente cuando se añade amoníaco al cloro para tratar el agua potable. Los niveles de cloro de hasta 4 miligramos por litro (mg/L o 4 partes por millón (ppm)) se consideran seguros en el agua potable.

- **Sulfatos:** Los sulfatos son sustancias naturales que se encuentran en los minerales, el suelo y las rocas. Están presentes en el aire ambiente, las aguas subterráneas, las plantas y los alimentos. El principal uso comercial del sulfato es en la industria química. La concentración de sulfato en el agua de mar es de unos 2.700 miligramos por litro (mg/L). Oscila entre 3 y 30 mg/L en la mayoría de los suministros de agua dulce, aunque en algunas localizaciones geográficas se encuentran concentraciones mucho mayores (1000 mg/L).

- **Conductividad:** El agua pura no es un buen conductor de la corriente eléctrica, más bien es un buen aislante. El aumento de la concentración de iones aumenta la conductividad eléctrica del agua. Generalmente, la cantidad de sólidos disueltos en el agua determina la conductividad eléctrica. La conductividad eléctrica (CE) mide en realidad el proceso iónico de una solución que le permite transmitir la corriente. Según las normas de la OMS, el valor de la CE no debe superar los 400 μS/cm.

- **Carbono_orgánico:** El carbono orgánico total (COT) en las aguas de origen procede de la materia orgánica natural en descomposición (NOM), así como de fuentes sintéticas. El COT es una medida de la cantidad total de carbono en compuestos orgánicos en el agua pura. Según la US EPA, < 2 mg/L de COT en el agua tratada/potable y < 4 mg/L en el agua de origen que se utiliza para el tratamiento.

- **Trihalometanos:** Los THM son sustancias químicas que pueden encontrarse en el agua tratada con cloro. La concentración de THM en el agua potable varía según el nivel de materia orgánica en el agua, la cantidad de cloro necesaria para tratar el agua y la temperatura del agua que se está tratando. Los niveles de THM de hasta 80 ppm se consideran seguros en el agua potable.

- **Turbidez:** La turbidez del agua depende de la cantidad de materia sólida presente en estado de suspensión. Es una medida de las propiedades de emisión de luz del agua y la prueba se utiliza para indicar la calidad del vertido con respecto a la materia coloidal. El valor medio de turbidez obtenido para el Campus Wondo Genet (0,98 NTU) es inferior al valor recomendado por la OMS de 5,00 NTU.

- **Potabilidad:** Indica si el agua es segura para el consumo humano donde 1 significa Potable y 0 significa No potable.

## Dependencias

Para ejecutar la aplicación web y utilizar los scripts proporcionados, se necesitan las siguientes bibliotecas de Python:

- Flask
- Pandas
- NumPy
- Scikit-learn
- SQLAlchemy (para la conexión a la base de datos Postgres)

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local:


2. Instala las dependencias necesarias:


3. Ejecuta la aplicación web Flask utilizando el siguiente comando en la carpeta `app/`:


4. Accede a la aplicación web a través de tu navegador web e introduce los datos necesarios para realizar predicciones sobre el acceso al agua potable en una región específica.

5. Los registros de predicciones se almacenarán automáticamente en la base de datos Postgres.

## Resultados

El modelo final seleccionado ha demostrado una alta precisión en la predicción del acceso al agua potable en diferentes regiones, lo que puede ser de gran utilidad para la planificación de políticas de salud y desarrollo.

