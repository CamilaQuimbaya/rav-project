# Sitio Institucional RAV

Institución Educativa Rafael Argote Vega — Chiriguaná, Cesar.

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html                    sitio institucional, HTML y CSS a mano
assets/
  logo-rav.svg                composicion maestra (escudo + nombre + descriptor)
  logo-nombre.svg             escudo + nombre, sin descriptor ni ubicacion
  logo-nombre-blanco.svg      la misma, blanca, para fondos azules
  escudo.svg                  escudo solo, en color
  escudo-blanco.svg           escudo solo, blanco, para fondos azules
  rav-logo.js                 <rav-logo> animado, usado en la intro
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

- **Versión "nombre + símbolo", no la composición completa.** El manual pide
  400 px de ancho para la versión con descriptor y ubicación, que en un
  encabezado web no caben. Se usa la versión reducida documentada en la p.4
  (escudo + nombre, sin descriptor ni ubicación), cuyo mínimo es 280 px; aquí va
  a 300 px en el encabezado y en el pie. De paso no arrastra el bajante
  "PLATAFORMA EDUCATIVA", que identifica a la plataforma y no al colegio (p.2).
- **Escudo solo** donde no caben esos 280 px: la barra flotante (56 px), el
  encabezado y el pie por debajo de 1100 px, y el favicon. Son los tamaños
  documentados para "escudo / avatar e icono" (96 · 56 · 32 px).
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

## Intro animada

Al entrar se muestra una vez por sesión el logo animándose (`<rav-logo>`, 2,8 s),
y luego aparece el sitio. El componente viene del diseño "Logo RAV Animado" y no
tiene dependencias; dibuja el escudo, el nombre y "Chiriguaná · Cesar", sin el
bajante "PLATAFORMA EDUCATIVA".

Se decide antes del primer pintado, en un script en el `<head>`, para que el
sitio no parpadee. No se muestra si el visitante pide reducir movimiento, ni en
la segunda carga de la misma sesión — y en esos casos tampoco se descargan los
64 KB del componente. Si el componente no carga, la intro se cierra sola a los
4 segundos. Sin JavaScript no aparece y el sitio funciona igual.

Para quitarla: borrar el bloque `.intro` del CSS, el `<div class="intro">` del
HTML, el script del `<head>` y el bloque de la intro en el script del final.

La pantalla de carga de la plataforma es otra cosa y no se toca.

## Contenido

Casi todo el contenido sale del Manual de Convivencia de la institución: los
ocho valores, los cinco niveles, los siete proyectos transversales, las cuatro
sedes con sus direcciones y jornadas, y los ocho hitos de la línea de tiempo
(1925, 1945, 1979, 1997, 2000, 2003, 2005 y 2009). La misión y la visión están
condensadas de los artículos 12 y 13.

Los rangos de grados de cada nivel (1.º a 5.º, 6.º a 9.º, 10.º y 11.º) siguen la
estructura estándar del sistema educativo colombiano; el manual los menciona
parcialmente pero no los enumera.

## Pendientes de contenido

- Las tres noticias son de muestra y están marcadas como tales.
- Teléfono y correo sin confirmar.
- Los accesos a documentos no tienen todavía archivo destino.
- El manual dice que "la sede No 2 ofrece preescolar a quinto en ambas
  jornadas", pero las sedes que enumera son la 1, la 5 y la 6. Esa frase se
  omitió por la inconsistencia; conviene verificarla con la institución.
- Las dos fotos parecen generadas por IA. La de la sede muestra un edificio con
  el nombre del colegio pintado que no es la sede real.

## Fondos

El ritmo cromático sigue la proporción de la p.6 del manual de marca: marfil
domina, azul da estructura, turquesa acompaña y el dorado va solo en acentos
(nunca como fondo de sección).

    portada        marfil   #F7F5EF
    esencia        blanco
    oferta         marfil
    historia       azul     #173653
    proyectos      menta    #E6F4F3
    noticias       blanco
    sedes          marfil
    pie            azul     #173653

## Actualizar la plataforma

```bash
cp "/mnt/c/Users/camil/Documents/proyecto educativo/Plataforma RAV.html" plataforma/index.html
sed -i 's|<title>Bundled Page</title>|<title>Plataforma RAV</title>|' plataforma/index.html
git commit -am "Actualizar plataforma" && git push
```

La plataforma es un prototipo navegable: el ingreso no valida credenciales y
trae una barra DEMO para cambiar de perfil. No debe cargarse con datos reales.
