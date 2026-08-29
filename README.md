# 🛒 Proyecto Concana - Aplicación Web en Django

Aplicación web desarrollada con el framework **Django** para la gestión y presentación de servicios del emprendimiento **Concana**. El proyecto incluye integración con archivos estáticos, generación dinámica de códigos QR y despliegue continuo en la nube a través de Render.

---

Autora: Elba Neira Arévalo

---

## 🚀 Enlaces del Proyecto

* **Sitio Web en Producción:** [https://concana-django.onrender.com/](https://concana-django.onrender.com/)
* **Código QR Fijo de Acceso Rápido:** [https://concana-django.onrender.com/qr/](https://concana-django.onrender.com/qr/)
* **Repositorio en GitHub:** [https://github.com/elbaneira/concana-django](https://github.com/elbaneira/concana-django)

---

## 🛠️ Tecnologías y Librerías Utilizadas

* **Lenguaje:** Python 3.x
* **Framework Web:** Django 6.1
* **Librerías Principales:**
  * `qrcode`: Generación dinámica de códigos QR en memoria.
  * `Pillow`: Procesamiento y manipulación de imágenes para la salida del QR.
  * `gunicorn`: Servidor HTTP WSGI para entorno de producción.
  * `whitenoise`: Gestión optimizada de archivos estáticos en producción.

---

## 📋 Funcionalidades Principales

1. **Catálogo / Página Principal:** Presentación web de los productos y servicios de Concana.
2. **Generador de QR Fijo (`/qr/`):** Genera dinámicamente un código QR en formato PNG que apunta a la URL principal de la app en Render, diseñado para su impresión y uso en carteles de acceso rápido.
3. **Despliegue Automático:** Integrado con GitHub y Render mediante integración continua (CI/CD).

---

## 💻 Instrucciones para Ejecución Local

Si deseas clonar y ejecutar este proyecto de forma local en tu máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/elbaneira/concana-django.git](https://github.com/elbaneira/concana-django.git)
   cd concana-django
---
© 2026 Elba Neira Arévalo

---