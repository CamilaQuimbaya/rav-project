# Sitio Institucional RAV

Institución Educativa Rafael Argote Vega — Chiriguaná, Cesar.

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html                    sitio institucional, HTML y CSS a mano
assets/
  logo-rav.svg                escudo institucional (fiel)
  logo-rav-negativo.svg       el mismo escudo en blanco, para fondos oscuros
  comunidad-1600/800.jpg      foto de portada
  sede-1600/800.jpg           foto de la franja de historia
  hojas / estrellas / mision-libro / vision-meta /
  oferta / proyectos / valores .svg        ilustraciones de marca
plataforma/index.html         la plataforma educativa (prototipo) — NO SE TOCA
.nojekyll                     evita que GitHub Pages procese el sitio con Jekyll
```

El sitio se edita directamente en `index.html`. No hay paso de compilación: se
abre, se cambia y se sube. Todo el CSS va en un `<style>` al inicio del archivo,
organizado por secciones con comentarios.

## Origen de los recursos

Las ilustraciones y las fotos salieron del diseño hecho en Claude Design
(proyecto "Sitio Institucional RAV v3"). Las fotos venían como PNG de 3,2 y
2,7 MB; aquí están como JPEG progresivo en dos tamaños (1600px y 800px), que es
lo que sirve `srcset`. El sitio completo pesa 1,4 MB en vez de 8,1 MB.

El escudo es el mismo archivo que usa la plataforma: se verificó comparando la
geometría de los 69 trazados.

## Pendientes de contenido

- Las tres noticias son de muestra y están marcadas como tales.
- Teléfono y correo sin confirmar.
- Las tarjetas de Oferta, Proyectos y Comunidad, y los tres accesos a
  documentos, dicen "Próximamente": no hay páginas destino todavía. Cuando
  existan, se convierten en enlaces.
- Las dos fotos parecen generadas por IA. La de la sede muestra un edificio con
  el nombre del colegio pintado que no es la sede real.

## Actualizar la plataforma

```bash
cp "/mnt/c/Users/camil/Documents/proyecto educativo/Plataforma RAV.html" plataforma/index.html
sed -i 's|<title>Bundled Page</title>|<title>Plataforma RAV</title>|' plataforma/index.html
git commit -am "Actualizar plataforma" && git push
```

La plataforma es un prototipo navegable: el ingreso no valida credenciales y
trae una barra DEMO para cambiar de perfil. No debe cargarse con datos reales.
