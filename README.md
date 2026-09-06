# Invitación — Civil de Virginia y Raúl

Sitio estático de una sola página. No requiere build.

- `index.html` — la invitación completa (música y formulario incluidos, sin dependencias externas salvo Google Fonts).
- `vercel.json` — evita que el navegador cachee la página, para que cualquier cambio que publiques se vea al instante.

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
