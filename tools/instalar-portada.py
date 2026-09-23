#!/usr/bin/env python3
"""
Instala una exportacion nueva del Sitio Institucional como index.html.

Cada vez que reexportas desde Claude Design hay que reaplicar tres parches,
porque el export los trae siempre en su estado original:

  1. El enlace a la plataforma apunta a "Plataforma RAV.dc.html" (ruta interna
     de Claude Design). Aqui debe ser "plataforma/index.html".
  2. El logo del pie es un raster 270x100 que dice "PLATAFORMA EDUCATIVA".
     Va el escudo institucional fiel, en blanco y vectorial.
  3. El <title> sale como "Bundled Page".

Uso:
    python3 tools/instalar-portada.py "/ruta/al/Sitio Institucional RAV.html"
"""
import base64, gzip, json, re, sys, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent
NEGATIVO = REPO / "assets" / "logo-rav-negativo.svg"
DESTINO = REPO / "index.html"

ENLACE_VIEJO = "Plataforma RAV.dc.html"
ENLACE_NUEVO = "plataforma/index.html"
TITULO_VIEJO = "<title>Bundled Page</title>"
TITULO_NUEVO = "<title>Institución Educativa Rafael Argote Vega</title>"


def bloque(html, tipo):
    """Devuelve el match del contenido JSON de un <script type="__bundler/TIPO">."""
    m = re.search(r'(<script type="__bundler/%s">\s*)(.*?)(\s*</script>)' % tipo,
                  html, re.S)
    if not m:
        sys.exit(f"ERROR: no encontre el bloque __bundler/{tipo}")
    return m


def empotrar(html, m, obj):
    """Reemplaza el contenido del bloque por obj serializado a JSON seguro."""
    txt = json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")
    return html[:m.start(2)] + txt + html[m.end(2):]


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    origen = pathlib.Path(sys.argv[1])
    if not origen.is_file():
        sys.exit(f"ERROR: no existe {origen}")
    if not NEGATIVO.is_file():
        sys.exit(f"ERROR: falta {NEGATIVO}")

    html = origen.read_text(encoding="utf-8", errors="replace")

    # 1. enlace a la plataforma
    m = bloque(html, "template")
    tpl = json.loads(m.group(2))
    n = tpl.count(ENLACE_VIEJO)
    if n == 0:
        print("AVISO: no habia enlaces que reapuntar (¿ya lo cambiaste en el diseño?)")
    tpl = tpl.replace(ENLACE_VIEJO, ENLACE_NUEVO)
    html = empotrar(html, m, tpl)
    print(f"[1] enlace a la plataforma: {n} reapuntados a {ENLACE_NUEVO}")

    # 2. logo del pie
    m = bloque(html, "manifest")
    man = json.loads(m.group(2))
    svg = NEGATIVO.read_bytes()
    reemplazados = []
    for k, v in man.items():
        # el negativo es el unico PNG pequeño; las fotos pesan megas
        if v.get("mime") == "image/png" and len(v.get("data", "")) < 200_000:
            man[k] = {"mime": "image/svg+xml", "compressed": True,
                      "data": base64.b64encode(gzip.compress(svg, 9)).decode()}
            reemplazados.append(k[:8])
    if not reemplazados:
        print("AVISO: no encontre el logo raster del pie; revisa el export a mano")
    html = empotrar(html, m, man)
    print(f"[2] logo del pie: {len(reemplazados)} reemplazado(s) por el escudo fiel "
          f"{reemplazados}")

    # 3. titulo
    if TITULO_VIEJO in html:
        html = html.replace(TITULO_VIEJO, TITULO_NUEVO)
        print("[3] title corregido")
    else:
        print("[3] AVISO: el title no era 'Bundled Page', lo dejo como esta")

    DESTINO.write_text(html, encoding="utf-8")
    print(f"\nlisto: {DESTINO} ({len(html):,} bytes)")
    print("la carpeta plataforma/ no se toca en ningun paso")


if __name__ == "__main__":
    main()
