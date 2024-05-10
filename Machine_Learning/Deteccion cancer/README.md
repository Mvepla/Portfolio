# Predicción de Tumores Benignos y Malignos

Este proyecto utiliza técnicas de Machine Learning para predecir si un tumor es benigno o maligno basándose en una serie de parámetros médicos. Se ha utilizado un conjunto de datos ampliamente conocido en la comunidad de Machine Learning, el conjunto de datos de cáncer de mama de Wisconsin, que contiene características calculadas a partir de imágenes digitalizadas de aspiración con aguja fina (FNA) de tumores mamarios.

## Estructura del Repositorio

- `data/`: Carpeta que contiene el conjunto de datos utilizado en formato CSV.
- `notebooks/`: Carpeta que contiene los cuadernos Jupyter utilizados para el análisis de datos, la construcción y evaluación de modelos.
- `models/`: Carpeta que contiene el modelo entrenado guardados en formato `.pkl`.
- `README.md`: Este archivo README que proporciona una descripción general del proyecto y cómo ejecutarlo.

## Dependencias

Para ejecutar los cuadernos de Jupyter y utilizar los scripts proporcionados, se necesitan las siguientes bibliotecas de Python:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Instrucciones de Uso

1. Clona este repositorio en tu máquina local.


2. Instala las dependencias necesarias.


3. Explora los cuadernos Jupyter en la carpeta `notebooks/` para entender el proceso de análisis de datos, construcción y evaluación de modelos.


4. El modelo entrenado se guarda en la carpeta `models/`. Puedes cargarlo y utilizarlo en tus propias aplicaciones mediante el uso de la biblioteca `joblib` de Python.

## Resultados

El modelo final entrenado ha alcanzado una precisión del 97% en la clasificación de tumores como benignos o malignos en el conjunto de datos de prueba. Se han realizado análisis adicionales para comprender la importancia de las características en la predicción, como obtener el score y accuracy de todos los modelos entrenados, el feature importance del mejor modelo y se han tomado medidas para abordar el posible desequilibrio de clases obteniendo al matriz de confusion el modelo elegido, con TP=41, FP= 2, FN= 1, TN= 70, lo que nos indica que el modelo tiene una tasa de acierto lo suficientemente alta para el conjunto de datos y que no hay desequilibrio de clases, se puede observar en los porcentajes de TP, FP, FN y TN a continuación.

![c_matrix](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Deteccion%20cancer/images/c.matrix.png)


