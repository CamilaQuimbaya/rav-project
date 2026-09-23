# Sitio Institucional RAV

Institución Educativa Rafael Argote Vega — Chiriguaná, Cesar.

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html                    sitio institucional, HTML y CSS a mano
assets/
  logo-rav.svg                composicion maestra (escudo + nombre + descriptor)
  escudo.svg                  escudo solo, en color
  escudo-blanco.svg           escudo solo, blanco, para fondos azules
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

## Marca

El sitio sigue el Manual de Marca RAV v1.0 (septiembre 2026), opción escudo.
Decisiones que vienen de ahí y conviene no deshacer sin releerlo:

- **Escudo solo, no la composición completa.** El manual pide 400 px de ancho
  mínimo para la versión con nombre y descriptor (p.4). En un encabezado web no
  caben, así que se usa la variante "escudo / avatar e icono", en sus tres
  tamaños documentados: 96 px en el pie, 72 px en el encabezado, 56 px en la
  barra flotante. El escudo solo tampoco arrastra el bajante "PLATAFORMA
  EDUCATIVA", que identifica a la plataforma y no al colegio (p.2).
- **Área de protección** de 1/4 del ancho del escudo, como padding del enlace.
- **Turquesa.** `#178C91` es el color de marca y se usa en superficies y
  trazos. Para texto, y para fondos que llevan texto blanco, va `#0F6E72`: el
  manual lo indica en la p.6 y se verificó que `#178C91` con blanco da 4,04:1,
  que no alcanza el AA de la WCAG. `#0F6E72` da 6,01:1.
- **Marfil `#F7F5EF` como fondo dominante**, azul para estructura y texto,
  turquesa para acción, dorado sólo en acentos (p.6).
- **Tipografía**: Sora en titulares (600), Work Sans en cuerpo (400, 16-18 px) y
  etiquetas (600, 14 px, 0,14 em). DejaVu Sans y Arial de respaldo (p.7).
- **Componentes**: radio 14 px en tarjetas, 999 px en botones, altura táctil
  mínima 44 px, foco visible con contorno turquesa de 2 px (p.8).

Caveat, la manuscrita del lema, no está en el manual: viene del diseño original
y se conservó a propósito.

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
