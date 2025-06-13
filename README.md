# Portafolio Web con Videojuegos

Este es un proyecto de portafolio personal diseñado para mostrar información sobre mí y destacar una sección de videojuegos con imágenes, títulos, precios y botones de compra. El sitio está construido utilizando **HTML**, **CSS** y **JavaScript puro (Vanilla JS)**.

## Estructura del Proyecto

```
portfolio-videojuegos/
├── index.html         # Página principal del portafolio
├── style.css          # Estilos personalizados del sitio
└── README.md          # Documentación del proyecto
```

##  Características

-  Sección "Sobre mí" con descripción personal.
-  Efecto acordeón para mostrar u ocultar contenido al hacer clic.
-  Lista de videojuegos con imágenes, títulos, precios y botones de compra.
-  Diseño responsivo que se adapta a dispositivos móviles.
-  Iconos y animaciones en flechas para mejorar la experiencia de usuario.

##  Tecnologías utilizadas

- HTML5
- CSS3
- JavaScript (Vanilla JS)
- Media Queries para diseño responsivo

##  Detalle de la sección de videojuegos

Cada videojuego se muestra con los siguientes elementos:

- Imagen del juego (con soporte para alta y baja resolución mediante `srcset`)
- Nombre del videojuego
- Precio aproximado
- Botón "Comprar"

Ejemplo:

```html
<div class="juego">
  <img srcset="imagenes/juego1-baja.jpg 300w, imagenes/juego1.jpg 600w" 
       sizes="(max-width: 600px) 300px, 600px" 
       src="imagenes/juego1.jpg" alt="Videojuego 1">
  <h3>Nombre del Videojuego</h3>
  <p>Precio: $XXX.XX</p>
  <button>Comprar</button>
</div>
```

##  Funcionalidad JavaScript

- **Acordeones**: Las secciones se abren y cierran dinámicamente al hacer clic.
- **Rotación de flechas**: Las flechas apuntan hacia abajo cuando se abre una sección, y hacia la derecha cuando está cerrada.

```javascript
const acordeonToggles = document.querySelectorAll('.acordeon-toggle');

acordeonToggles.forEach(toggle => {
  toggle.addEventListener('click', () => {
    const content = toggle.nextElementSibling;
    const arrow = toggle.querySelector('.arrow');

    if (content.style.display === 'block') {
      content.style.display = 'none';
      arrow.classList.remove('rotate');
    } else {
      content.style.display = 'block';
      arrow.classList.add('rotate');
    }
  });
});
```

## Responsive Design

El sitio está optimizado para dispositivos móviles utilizando media queries. Los elementos se reorganizan verticalmente en pantallas pequeñas para una mejor visualización.

```css
@media (max-width: 600px) {
  .videojuegos {
    flex-direction: column;
    align-items: center;
  }

  .juego {
    width: 90%;
  }
}
```

## Cómo ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/portfolio-videojuegos.git
   ```
2. Abre el archivo `index.html` en tu navegador favorito.

##  Ideas para mejoras futuras

- Conectar con una API para obtener videojuegos dinámicamente.
- Agregar animaciones CSS más avanzadas.
- Implementar modo oscuro.
- Agregar una sección de contacto o formulario.


> Este proyecto fue creado como práctica para mejorar mis habilidades en desarrollo web usando HTML, CSS y JavaScript.
