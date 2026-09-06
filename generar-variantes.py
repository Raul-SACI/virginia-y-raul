#!/usr/bin/env python3
"""
Genera solo.html y brindis.html a partir de index.html.

Hace falta un archivo por grupo porque WhatsApp no ejecuta JavaScript al armar
la vista previa del link: para que cada invitación tenga su propia tarjeta, el
título tiene que estar en el HTML crudo.

index.html es el único que se edita a mano. Después de cualquier cambio:

    python3 generar-variantes.py
"""

import io
import re
import sys

SITIO = 'https://virginia-y-raul.vercel.app'

VARIANTES = {
    'solo': {
        'archivo': 'solo.html',
        'titulo': 'Virginia &amp; Raúl - Civil (1)',
        'descripcion': 'Viernes 4 de diciembre · Civil y almuerzo. Entrá para ver los detalles y confirmar tu asistencia.',
        'url': SITIO + '/solo',
    },
    'brindis': {
        'archivo': 'brindis.html',
        'titulo': 'Virginia &amp; Raúl - Brindis Civil',
        'descripcion': 'Viernes 4 de diciembre · Brindis a las 15:00. Entrá para ver los detalles y confirmar tu asistencia.',
        'url': SITIO + '/brindis',
    },
}

AVISO = ('<!-- ARCHIVO GENERADO por generar-variantes.py a partir de index.html.\n'
         '     No editar a mano: cualquier cambio se pierde en la próxima generación. -->\n')

base = io.open('index.html', encoding='utf-8').read()

for grupo, v in VARIANTES.items():
    h = base

    def cambiar(patron, reemplazo, texto):
        texto, n = re.subn(patron, reemplazo, texto, count=1)
        if n != 1:
            sys.exit('No se pudo aplicar en %s: %s' % (v['archivo'], patron))
        return texto

    h = cambiar(r"var GRUPO_ARCHIVO = 'pareja';",
                "var GRUPO_ARCHIVO = '%s';" % grupo, h)
    h = cambiar(r'(<meta property="og:title" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['titulo'], h)
    h = cambiar(r'(<meta name="twitter:title" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['titulo'], h)
    h = cambiar(r'(<meta property="og:description" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['descripcion'], h)
    h = cambiar(r'(<meta name="twitter:description" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['descripcion'], h)
    h = cambiar(r'(<meta name="description" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['descripcion'], h)
    h = cambiar(r'(<meta property="og:url" content=")[^"]*(")',
                r'\g<1>%s\g<2>' % v['url'], h)
    h = cambiar(r'(<!DOCTYPE html>\n)', r'\g<1>' + AVISO, h)

    io.open(v['archivo'], 'w', encoding='utf-8').write(h)
    print('%-13s grupo=%-8s %s' % (v['archivo'], grupo, v['titulo'].replace('&amp;', '&')))
