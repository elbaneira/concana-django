# 🛒 Proyecto Concana - Aplicación Web en Django

Aplicación web desarrollada con el framework **Django** para la gestión y presentación de servicios del emprendimiento **Concana**. El proyecto incluye integración con archivos estáticos, generación dinámica de códigos QR y despliegue continuo en la nube a través de Render.

---

Autora: Elba Neira Arévalo

---

## 🚀 Enlaces Directos del Proyecto en Producción

* **Página Principal (Inicio):** [https://concana-django.onrender.com/](https://concana-django.onrender.com/)
* **Módulo de Caja:** [https://concana-django.onrender.com/caja/](https://concana-django.onrender.com/caja/)
* **Módulo de Cocina:** [https://concana-django.onrender.com/cocina/](https://concana-django.onrender.com/cocina/)
* **Registro e Cierre de Ventas:** [https://concana-django.onrender.com/cierre/](https://concana-django.onrender.com/cierre/)
* **Código QR Fijo de Acceso Rápido:** [https://concana-django.onrender.com/qr/](https://concana-django.onrender.com/qr/)

---

## 📋 Módulos y Rutas Principales

| Módulo / Ruta | Descripción |
| :--- | :--- |
| `/` | Catálogo y presentación web principal de Concana. |
| `/caja/` | Panel de gestión y registro de ventas para el cajero. |
| `/cocina/` | Vista de comanda y pedidos activos para el área de cocina. |
| `/historial/` | Registro, reporte e historial detallado de ventas realizadas. |
| `/qr/` | Generador dinámico del código QR de acceso rápido. |
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