
<p align="center">
  <img src="https://github.com/Mvepla/desafio_tripulaciones/blob/main/images/the-bridge-edem.png" alt="the-bridge-edem">
</p>


# Data Science - Proyecto final Bootcamp.

## Desafio tripulaciones.

El desafio de tripulaciones es la práctica integrada en la que trabajamos los estudiantes de todas las disciplinas a través de un proyecto real diseñado conjuntamente con un partner. Con esta práctica los estudiantes nos enfrentamos al día a día de nuestro futuro profesional trabajando de principio a fin en un proyecto en el que nos involucramos como miembros del departamento de una empresa.

<p align="center">
  <img src="https://github.com/Mvepla/desafio_tripulaciones/blob/main/images/herramientas.png" alt="metodologia">
</p>

Desde el primer momento del proyecto se crea un tablero a través de la aplicación Trello para coordinarnos dentro del mismo equipo y sobre todo entre las diferentes verticales. Revisándolo cada mañana durante el daily, creando nuevas tareas y marcando las finalizadas.

## Desafío cliente.

El proyecto sobre el que trabajamos las tres verticales es una web-app para el Colegio de Administradores de Fincas Valencia-Castellón. El enfoque del proyecto es mejorar la forma de trabajo de los administradores para poder ser mas eficientes en su trabajo. El proyecto se lleva a cabo junto a las otras 2 verticales, UX/UI y Fullstack.

## Objetivos Data Science.

La parte de proyecto del grupo de Data Science se centra en realizar una API-REST para realizar un tratamiento de las actas de las reuniones de comunidad.

La aplicación está en producción en Amazon Web Service. Dicha aplicacion contiene 4 endpoints:

1- <u>**./:**</u> Se muestra un formulario html donde se muestran los diferentes endpoints documentados para que los compañeros de Fullstack sepan que hace cada endpoint a la hora de poder usarlos y plasmarlos en la app.

2- <u>**./subir_pdf:**</u> Endpoint tipo POST en el cual se sube un acta en formato .pdf, este acta se transforma en texto y pasa a un modelo de Huggingface (facebook/bart-large.cnn) el cual hace un resumen. Una vez obtenido el resumen, para transcribirlo a audio pasa por un modelo Google Text-to-Speech (gTTs) que devuelve el contenido del resumen en un archivo mp3. Cuando ya tenemos los tres archivos, se suben a la BBDD. Para la BBDD se usa MongoDB Atlas, que es un servicio de Cloud Database (o Base de Datos en la Nube).

3- <u>**./resumen:**</u> Endpoint tipo GET que hace un llamado a la base de datos y devuelve el contenido del resumen en un json.

4- <u>**./audio:**</u> Endpoint tipo GET que hace un llamado a la base de datos, transforma el archivo de binario que viene de la BBDD a mp3 y devuelve el archivo mp3 del audio.


## Roadmap

1-<u>**Gestión de incidencias:**</u> Gestión automatizada de incidencias de la comunidad.

El propietario realiza una foto de la incidencia y la sube a la app, a continuación esa foto pasa por un modelo de image to text para que describa la imagen para que una vez obtenida la descripción en texto, pueda pasar por un modelo de clasificación de incidencias que la clasifica como urgente o no urgente. Una vez clasificada se abren dos caminos:

- Urgente: manda un mensaje automático, via email creado con GPT-3 al técnico asociado por la comunidad al tipo de incidencia clasificada para que realice la reparación y otro email al administrador para que pueda hacer un seguimiento, una vez realizada la reparación el tecnico la marca como tal y se envia una confirmación de reparación al administrador y al propietario.

- No urgente: se envia aviso al tecnico para realizar la reparación, cuando el técnico recibe la incidencia se envía automáticamente un email al propietario avisando que el técnico esta en marcha y una vez confirmada la reparación se envia automáticamente un email al propietario.


<p align="center">
  <img src="https://github.com/Mvepla/desafio_tripulaciones/blob/main/images/Diagrama.PNG" alt="grafico incidencias">
</p>


2-<u>**Pre-trabajo de actas:**</u> En el desarrollo del trabajo nos hemos centrado en el procesamiento de actas ya en formato .pdf, pero a futuro la idea es que el administrados grabe la junta, con el consentimiento de los vecinos, esta pase por un modelo Google Cloud Speech-to-Text para pasarlo a texto y ahi ya entra el modelo implementado.

3- <u>**Asistente virtual:**</u> Creación de un Chatbot con Google Dialogflow que haga las funciones de asistente virtual y tenga implementadas las preguntas tipicas de Q&A.

## 👥Contribuidores.

El éxito de este proyecto es gracias al esfuerzo y dedicación de todo el equipo. Cada contribución ha sido valiosa y nos ha llevado más cerca de nuestros objetivos.

Miguel Vela            [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/miguel-vela/)

Cristina Ponce         [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cristinapl/)

Alvaro Lozano          [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/%C3%A1lvaro-lozano-7212a642/)


Beatriz Minguez        [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/beatrizminguezpastor/)





