import numpy as np
import pandas as pd
import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.inception_v3 import decode_predictions, preprocess_input



st.set_page_config(
    page_title="Clasificador de tiburones",
    page_icon=':ocean:',
    layout="wide",
    initial_sidebar_state="expanded",)

st.header('Bienvenid@ al clasificador de tiburones')
image_url = 'https://ih1.redbubble.net/image.5013157049.6884/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg'
st.image(image_url)
imagen = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

def reconoc_foto(imagen):
    model = tf.keras.models.load_model('my_keras_model_line2.h5')

    imagen = image_path

    IMAGE_SIZE = (250,250)

    img= load_img(image_path, target_size=IMAGE_SIZE,color_mode='grayscale')

    img_array = img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = img_array.reshape((1,) + img_array.shape) 

    prediccion = model.predict(img_array)

    clase_predicha = prediccion.argmax(axis=1)[0]

    nombres_clases= {0:'Tiburon azul o Tintorera (Prionace glauca)',
                 1:'Tiburon ballena (Rhincodon typus)',
                 2: 'Tiburon blanco (Carcharodon carcharias)',
                 3: 'Tiburon lamia (Carcharhinus leucas)',
                 4: 'Tiburon limon (Negaprion brevirostris)',
                 5:'Tiburon mako o Marrajo (Isurus oxyrinchus)',
                 6: 'Tiburon martillo (Sphyrna mokarran)',
                 7: 'Tiburon nodriza (Ginglymostoma cirratum)',
                 8:'Tiburon peregrino (Cethorhinus maximus)',
                 9: 'Tiburon punta blanca oceanico (Carcharhinus longimanus)',
                 10: 'Tiburon punta negra (Carcharhinus limbatus)',
                 11: 'Tiburon tigre (Galeocerdo cuvier)',
                 12: 'Tiburon toro (Carcharias taurus)',
                 13: 'Tiburon zorro (Alopias vulpinus)'}
    
    nombre_clase_predicha = nombres_clases[clase_predicha]

    return nombre_clase_predicha


reconoc_foto(imagen)

st.image(imagen)

st.text(print(f'el tiburon de la foto es: {nombre_clase_predicha}'))

