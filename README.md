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
