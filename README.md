Reporte Técnico: Implementación de Agente Conversacional Web (Proyecto Wattson)
1. Introducción
El presente proyecto consiste en el desarrollo de una aplicación web de chat que integra el modelo de lenguaje GPT de OpenAI con una interfaz de usuario personalizada.
El objetivo principal fue crear una experiencia de usuario inmersiva basada en el personaje Wattson (Apex Legends), asegurando una comunicación fluida entre el cliente y el servidor.

2. Desafíos Técnicos y Soluciones
A. Gestión de Contexto y Persistencia de Personalidad (Lógica)
Desafío: Los modelos de lenguaje por sí mismos no poseen memoria de corto plazo entre peticiones HTTP, lo que provocaba que la IA perdiera su personalidad de "Wattson" tras el primer mensaje.
Solución: Se implementó una estructura de datos tipo lista en el backend para almacenar el historial de la conversación. En cada petición al endpoint /preguntar, el sistema envía el historial
completo junto con un System Prompt específico. Esto garantiza que el modelo mantenga la coherencia narrativa y el contexto de la charla en todo momento.

B. Integración Asíncrona Frontend-Backend (Atención al Detalle)
Desafío: Las peticiones a APIs externas pueden demorar varios segundos. Una petición síncrona bloquearía la interfaz de usuario, degradando la experiencia.
Solución: Se desarrolló un flujo de comunicación asíncrona mediante AJAX (API Fetch). Esto permite:
Inyectar el mensaje del usuario de forma instantánea en el DOM.
Mostrar un indicador visual de "Escribiendo..." mientras se procesa la respuesta.
Actualizar la interfaz dinámicamente sin recargar la página, optimizando el rendimiento percibido.

C. Transición de Entorno de Ejecución (Creatividad)
Desafío: Adaptar una lógica de control de flujo basada en consola (while True) a un entorno web basado en eventos.
Solución: Se realizó una migración hacia el microframework Flask, transformando el bucle infinito en un endpoint RESTful. 
Se diseñó una interfaz visual con CSS responsivo que incluye una "burbuja" de chat interactiva, mejorando la accesibilidad y el atractivo visual respecto a una terminal de comandos.

3. Stack Tecnológico
Backend: Python 3, Flask (Manejo de rutas y lógica de servidor).
Frontend: HTML5, CSS3 (Diseño responsivo), JavaScript Vanilla (Manipulación del DOM y Fetch).
IA: OpenAI API (Modelo GPT), Python-Dotenv (Gestión de seguridad y variables de entorno).

4. Conclusión
Este challenge permitió demostrar capacidades de atención al detalle mediante la validación de inputs y el manejo de estados de carga,
así como creatividad en la personificación de un servicio técnico. La solución final es un producto funcional, seguro (gracias a la separación de credenciales)
y listo para ser escalado a entornos de producción o integraciones más complejas de IA.
