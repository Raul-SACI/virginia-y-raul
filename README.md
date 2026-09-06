# Invitación — Civil de Virginia y Raúl

Sitio estático de una sola página. No requiere build.

- `index.html` — la invitación completa (formulario incluido).
- `portada.jpg` — la foto de la portada. Va como archivo aparte porque WhatsApp
  y las demás redes no leen imágenes incrustadas en base64: la vista previa al
  compartir el link necesita una URL absoluta a un archivo real.
- `musica.mp3` — la música de fondo. Va como archivo aparte, no incrustada en el
  HTML: así la página se muestra enseguida y el audio se descarga en paralelo,
  en vez de hacer esperar al invitado hasta tener la canción entera.
  Si algún día se cambia la canción, conviene subirla con **otro nombre**: el
  archivo se sirve con caché de un año, así que un reemplazo con el mismo
  nombre lo seguirían escuchando viejo quienes ya visitaron la invitación.
- `vercel.json` — evita que el navegador cachee la página, para que cualquier cambio que publiques se vea al instante.

## Los tres grupos

Hay un archivo por grupo de invitados:

| Link | Archivo | Quién |
|---|---|---|
| `/`        | `index.html`   | Parejas — civil, almuerzo, 1 o 2 adultos |
| `/solo`    | `solo.html`    | Invitados solos — civil, almuerzo, 1 adulto fijo |
| `/brindis` | `brindis.html` | Brindis de las 15:00 |

Están separados porque WhatsApp no ejecuta JavaScript al armar la vista previa
del link: para que cada invitación tenga su propia tarjeta, el título tiene que
estar en el HTML crudo.

**Sólo se edita `index.html`.** `solo.html` y `brindis.html` se generan:

    python3 generar-variantes.py

Correr eso después de cada cambio, antes de publicar, o los tres archivos
quedan desincronizados.

Los links viejos con `?i=solo` y `?i=brindis` siguen funcionando: el parámetro
tiene prioridad sobre el archivo, así que lo ya repartido no se rompe.

## Publicar

Importar el repositorio en Vercel. No hace falta configurar nada:
Framework Preset `Other`, sin Build Command, sin Output Directory.

## Confirmaciones

El formulario envía a un Google Apps Script (`GOOGLE_SHEETS_URL` dentro de `index.html`),
que escribe las respuestas en la planilla de cálculo.

El envío usa `Content-Type: text/plain`. **No cambiar a `application/json`**: eso dispara
una petición OPTIONS de preflight que Apps Script no responde, y las confirmaciones
dejan de llegar sin ningún aviso.

## Autoría de los commits (importante)

Los commits de este repo deben ir firmados con una dirección registrada en la
cuenta de GitHub **Raul-SACI**, que es la dueña del repositorio y la conectada
a Vercel:

    git config user.name  "Raul-SACI"
    git config user.email "279264035+Raul-SACI@users.noreply.github.com"

Si se firma con otra dirección —por ejemplo `raulemilianodc@gmail.com`, que
pertenece a la cuenta `raulemilianodc-cloud`— GitHub atribuye el commit a esa
otra cuenta. Vercel lo lee como un colaborador externo, y como el plan Hobby no
admite colaboradores en repositorios privados, **bloquea el despliegue**
(«Deployment Blocked: the commit author did not have contributing access»).

El sitio sigue publicado con la versión anterior y el bloqueo no deja ningún
log de build, porque la compilación nunca llega a arrancar.
