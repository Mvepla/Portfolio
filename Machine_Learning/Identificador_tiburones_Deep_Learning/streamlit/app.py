import streamlit as st
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.inception_v3 import preprocess_input


st.set_page_config(
    page_title="Clasificador de tiburones",
    page_icon=':ocean:',
    layout="wide",
    initial_sidebar_state="expanded",
)

st.header('Bienvenid@ al clasificador de tiburones')
st.subheader("Después de la imagen tienes un boton para cargar la foto del tiburon que quieres saber la especie")
image_url = './logo-oceanografic-min.png'
#image_url = 'https://ih1.redbubble.net/image.5013157049.6884/bg,f8f8f8-flat,750x,075,f-pad,750x1000,f8f8f8.jpg'
st.image(image_url)

def reconocer_foto(imagen):
    model = tf.keras.models.load_model('my_keras_model_line2.h5')

    IMAGE_SIZE = (250, 250)
    img = Image.open(imagen).convert('L').resize(IMAGE_SIZE)
    img_array = img_to_array(img)
    img_array = preprocess_input(img_array.reshape((1,) + img_array.shape))

    prediccion = model.predict(img_array)
    clase_predicha = prediccion.argmax(axis=1)[0]

    nombres_clases = {
        0: 'Tiburón azul o Tintorera (Prionace glauca)',
        1: 'Tiburón ballena (Rhincodon typus)',
        2: 'Tiburón blanco (Carcharodon carcharias)',
        3: 'Tiburón lamia (Carcharhinus leucas)',
        4: 'Tiburón limon (Negaprion brevirostris)',
        5: 'Tiburón mako o Marrajo (Isurus oxyrinchus)',
        6: 'Tiburón martillo (Sphyrna mokarran)',
        7: 'Tiburón nodriza (Ginglymostoma cirratum)',
        8: 'Tiburón peregrino (Cethorhinus maximus)',
        9: 'Tiburón punta blanca oceanico (Carcharhinus longimanus)',
        10: 'Tiburón punta negra (Carcharhinus limbatus)',
        11: 'Tiburón tigre (Galeocerdo cuvier)',
        12: 'Tiburón toro (Carcharias taurus)',
        13: 'Tiburón zorro (Alopias vulpinus)'
    }

    nombre_clase_predicha = nombres_clases[clase_predicha]

    return nombre_clase_predicha, img


imagen = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])


if imagen is not None:
    
    nombre_clase_predicha, img = reconocer_foto(imagen)
    st.subheader("Resultado del modelo:")
    st.image(imagen, use_column_width=True)
    st.write(f'El tiburón de la foto es: {nombre_clase_predicha}')
