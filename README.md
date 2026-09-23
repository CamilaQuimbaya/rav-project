# Sitio Institucional RAV

Institución Educativa Rafael Argote Vega — Chiriguaná, Cesar.

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html                   sitio institucional (export de Claude Design, parcheado)
plataforma/index.html        la plataforma educativa (prototipo) — NO SE TOCA
assets/logo-rav.svg          escudo institucional fiel
assets/logo-rav-negativo.svg escudo fiel en blanco, para fondos oscuros
tools/instalar-portada.py    reaplica los parches tras cada reexportacion
.nojekyll                    evita que GitHub Pages procese el sitio con Jekyll
```

Los dos SVG de `assets/` no los carga el sitio: el export ya los trae embebidos.
Estan ahi como fuente de verdad del escudo, y `instalar-portada.py` los usa.

## Actualizar el sitio institucional

Exporta el standalone desde Claude Design y corre:

```bash
python3 tools/instalar-portada.py "/mnt/c/Users/camil/Documents/proyecto educativo/Sitio Institucional RAV.html"
git commit -am "Actualizar sitio institucional" && git push
```

El script reaplica tres parches que el export trae siempre en su estado original:

1. El enlace a la plataforma viene como `Plataforma RAV.dc.html` (ruta interna de
   Claude Design) y debe ser `plataforma/index.html`.
2. El logo del pie viene como un raster 270x100 que dice "PLATAFORMA EDUCATIVA";
   se reemplaza por el escudo institucional fiel, vectorial y en blanco.
3. El `<title>` viene como "Bundled Page".

## Actualizar la plataforma

```bash
cp "/mnt/c/Users/camil/Documents/proyecto educativo/Plataforma RAV.html" plataforma/index.html
sed -i 's|<title>Bundled Page</title>|<title>Plataforma RAV</title>|' plataforma/index.html
git commit -am "Actualizar plataforma" && git push
```

## Notas

La plataforma es un prototipo navegable: el ingreso no valida credenciales y trae
una barra DEMO para cambiar de perfil. No debe cargarse con datos reales.

El sitio institucional pesa ~8 MB porque embebe dos fotos en PNG de 3,1 y 2,7 MB.
Funciona, pero conviene pasarlas a JPEG o WebP antes de difundirlo.

Contenido pendiente de confirmar en el sitio: las tres noticias son de ejemplo, y
el telefono y el correo estan marcados como "por confirmar".
