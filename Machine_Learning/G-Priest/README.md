# G-Priest: Chatbot Simulador de Cura Católico

G-Priest es un chatbot que simula ser un cura católico, utilizando la API de Cohere para el procesamiento del lenguaje natural y técnicas de prompt engineering. Esta aplicación está desplegada en Render.

## Estructura del Proyecto

```plaintext
G-Priest/
│
├── templates/
│   └── index.html
├── app.py
├── README.md
└── requirements.txt
```

- **templates/**: Carpeta que contiene las plantillas HTML.
  - **index.html**: La plantilla principal para la interfaz de usuario.
- **app.py**: El script principal de la aplicación.
- **README.md**: Este archivo, que proporciona una visión general del proyecto.
- **requirements.txt**: Archivo que lista las dependencias necesarias para ejecutar la aplicación.

## Requisitos

Para ejecutar esta aplicación, necesitas tener instalados los siguientes componentes:

- Python 3.x
- Las librerías listadas en `requirements.txt`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone <URL del repositorio>
   cd G-Priest
   ```

2. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Configuración

Antes de ejecutar la aplicación, asegúrate de configurar las variables necesarias para la API de Cohere.

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando:
```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`.

## Despliegue

La aplicación está desplegada en Render. Puedes acceder a la versión en vivo en [https://g-priest.onrender.com/](https://g-priest.onrender.com/).

## Uso

Abre `http://localhost:5000` en tu navegador. La interfaz principal te permitirá interactuar con el chatbot que simula ser un cura católico. El chatbot utiliza la API de Cohere para procesar y responder a tus preguntas o comentarios.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva característica'`).
4. Sube tus cambios (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

## Contacto

Para más información o preguntas, por favor contacta a [miguel.vela.planas@gmail.com](mailto:miguel.vela.planas@gmail.com).

