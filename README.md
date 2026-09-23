# Sitio Institucional RAV

Institución Educativa Rafael Argote Vega — Chiriguaná, Cesar.

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html                    el sitio entero: HTML, CSS y JS a mano, sin compilar
assets/
  logo-rav.svg                composicion maestra (escudo + nombre + descriptor)
  logo-nombre.svg             escudo + nombre, sin descriptor ni ubicacion
  logo-nombre-blanco.svg      la misma, blanca, para fondos azules
  escudo.svg                  escudo solo, en color
  escudo-blanco.svg           escudo solo, blanco
  rav-logo.js                 <rav-logo>, el logo animado de la intro
  comunidad-*.jpg             foto de la portada (1600 y 800 px)
  sede-*.jpg                  foto de la seccion de historia
  il-*.png                    ilustraciones grandes
  hojas / estrellas / ramas / mision-libro / vision-meta /
  oferta / proyectos / valores .svg     ilustraciones de marca
plataforma/index.html         la plataforma educativa (prototipo) — NO SE TOCA
.nojekyll                     evita que GitHub Pages procese el sitio con Jekyll
```

Se edita directamente en `index.html`. Todo el CSS va en un `<style>` al inicio
y el JS en un `<script>` al final, ambos organizados por secciones.

## Marca

El sitio sigue el Manual de Marca RAV v1.0 (septiembre 2026), opcion escudo.
Decisiones que vienen de ahi:

- **Turquesa.** `#178C91` en superficies y trazos. Para texto, y para fondos que
  llevan texto blanco, va `#0F6E72`: el manual lo indica en la p.6 y se verifico
  que `#178C91` con blanco da 4,04:1, por debajo del AA de la WCAG.
- **Marfil `#F7F5EF` como fondo dominante**, azul para estructura, turquesa para
  accion, dorado solo en acentos (p.6).
- **Tipografia**: Sora en titulares (600), Work Sans en cuerpo (400, 16-18px) y
  etiquetas (600, 14px, 0,14em). DejaVu Sans y Arial de respaldo (p.7).
- **Componentes**: radio 14px en tarjetas, 999px en botones, altura tactil
  minima 44px, foco visible con contorno turquesa de 2px (p.8).
- **Logo**: version "nombre + simbolo" (sin el bajante "PLATAFORMA EDUCATIVA",
  que identifica a la plataforma y no al colegio, p.2). Escudo solo donde no
  caben los 280px que pide esa version: movil y favicon.

### Desviaciones conscientes

- **Logo de la barra fija a 200px**, por debajo de los 280px que propone la p.4.
  A 280px la barra media 121px de alto y comia demasiada pantalla; a 200px mide
  88px y el nombre sigue legible.
- **Caveat** (la manuscrita del lema y de la nota de historia) no esta en el
  manual: viene del diseño original y se conservo a proposito.

## Como esta construido

**Separadores de seccion.** El borde entre secciones no es una linea recta: es
una curva, con tres arcos paralelos encima en turquesa y dorado. Es el mismo
grafismo del fondo del login de la plataforma. El SVG se estira con
`preserveAspectRatio="none"`, y los trazos llevan `vector-effect:non-scaling-stroke`
para que el estirado no les cambie el grosor.

**Recortes con curva.** La foto de la portada y el velo llevan mascaras SVG con
`feGaussianBlur` en el borde: sin ese desenfoque la curva se veria como un filo
duro atravesando la imagen.

**Contraste verificado.** Cada vez que hay texto sobre foto o sobre una capa
semitransparente, la opacidad se eligio midiendo la luminancia real de la imagen
y calculando el ratio, no a ojo. La foto de historia va al 26% porque la mascara
la apaga justo donde vive el texto; sin esa mascara el maximo seria 16%.

**Movimiento.** Aparicion al entrar en pantalla (en los dos sentidos del scroll,
con la direccion del desplazamiento segun por donde salio el bloque), parallax en
cuatro capas y barra de progreso. Todo con `transform` y `opacity` dentro de
`requestAnimationFrame`. Con `prefers-reduced-motion` no se ejecuta nada de esto
y el contenido aparece visible de entrada.

**Intro.** Al entrar se muestra una vez por sesion el logo animandose (2,8s). Se
decide en un script del `<head>` para que el sitio no parpadee, el componente solo
se descarga si se va a usar, y hay una red de seguridad a los 4 segundos por si
no carga. La pantalla de carga de la plataforma es otra cosa y no se toca.

## Contenido

Casi todo sale del Manual de Convivencia: los ocho valores, los cinco niveles,
los siete proyectos transversales, las cuatro sedes con direcciones y jornadas, y
los ocho hitos de la linea de tiempo (1925, 1945, 1979, 1997, 2000, 2003, 2005 y
2009). Mision y vision estan condensadas de los articulos 12 y 13.

Los rangos de grados de cada nivel siguen la estructura estandar del sistema
educativo colombiano; el manual los menciona parcialmente pero no los enumera.

Las ilustraciones `il-*.png` venian en laminas de tres sobre fondo marfil. Se
separaron, se les quito el fondo con relleno por inundacion desde los bordes
(para no vaciar los blancos interiores de paginas y bombilla) y se redujeron a
paleta indexada. Pesaban 1,5 MB y quedaron en 84 KB.

## Pendientes

- Las tres noticias son de muestra y estan marcadas como tales.
- Telefono y correo sin confirmar.
- Los accesos a documentos no tienen todavia archivo destino.
- El manual dice que "la sede No 2 ofrece preescolar a quinto en ambas
  jornadas", pero las sedes que enumera son la 1, la 5 y la 6. Esa frase se
  omitio por la inconsistencia; conviene verificarla con la institucion.
- Las dos fotos parecen generadas por IA. La de la sede muestra un edificio con
  el nombre del colegio pintado que no es la sede real.

## Actualizar la plataforma

```bash
cp "/mnt/c/Users/camil/Documents/proyecto educativo/Plataforma RAV.html" plataforma/index.html
sed -i 's|<title>Bundled Page</title>|<title>Plataforma RAV</title>|' plataforma/index.html
git commit -am "Actualizar plataforma" && git push
```

La plataforma es un prototipo navegable: el ingreso no valida credenciales y trae
una barra DEMO para cambiar de perfil. No debe cargarse con datos reales.
