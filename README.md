# Plataforma RAV

Sitio de la Institución Educativa Rafael Argote Vega (Chiriguaná, Cesar).

Publicado en: https://camilaquimbaya.github.io/rav-project/

## Estructura

```
index.html             portada pública → botón "Entrar" lleva a /plataforma/
assets/logo-rav.svg    escudo institucional (también se usa como favicon)
plataforma/index.html  la aplicación, exportada tal cual desde el diseño
.nojekyll              evita que GitHub Pages procese el sitio con Jekyll
```

La portada es un archivo independiente y editable a mano. La aplicación se
reemplaza completa en cada exportación, por eso no se le edita nada adentro.

## Actualizar la aplicación

```bash
cp "/mnt/c/Users/camil/Documents/proyecto educativo/Plataforma RAV.html" plataforma/index.html
sed -i 's|<title>Bundled Page</title>|<title>Plataforma RAV</title>|' plataforma/index.html
git commit -am "Actualizar plataforma" && git push
```

## Nota

La aplicación es un prototipo navegable: el ingreso no valida credenciales y
trae una barra DEMO para cambiar de perfil (Estudiante, Acudiente, Docente,
Coordinación). No debe cargarse con datos reales de estudiantes.
