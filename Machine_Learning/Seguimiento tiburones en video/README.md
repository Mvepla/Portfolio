📚 Contexto

Proyecto de seguimiento de animales, en este caso tiburones, en video. La idea de este proyecto es llegar a combinarlo con el anterior de identificacion de tiburones para que una vez identificada la especie, el nombre de la especie se inserte donde actualmente pone "tiburon".

📝 Contenido

Para este proyecto se ha utilizado la libreria OpenCV para Python, la cual permite analizar un video frame a frame y poder identificar formas, en nuestro caso tiburones, y marcar las zonas donde ha identificado a un tiburon o parte de el con un cuadrado y la etiqueta "tiburon", para ello se realiza una sustraccion de fondo, resalta los objetos en movimiento y detecta y filtra los contornos.

Al ser el video muy pesado y no poder subirlo a Github, a continuacion dejo un pequeño clip de como funciona el modelo.

![Gif tiburones](https://github.com/Mvepla/Portfolio/blob/main/Machine_Learning/Seguimiento%20tiburones%20en%20video/demo.gif)