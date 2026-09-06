/**
 * Recibe las confirmaciones de la invitación y las escribe en la planilla.
 *
 * Columnas que genera:  NOMBRE | GRUPO | ADULTOS | ESTADO | FECHA
 *
 * IMPORTANTE — la invitación manda el cuerpo como 'text/plain' con un JSON
 * adentro. No cambiar eso a 'application/json': con ese encabezado el navegador
 * envía primero una petición OPTIONS de permiso (preflight CORS) que Apps
 * Script no responde, y las confirmaciones dejan de llegar sin ningún aviso.
 */

var GRUPOS = {
  pareja:  'Pareja',
  solo:    'Solo',
  brindis: 'Brindis'
};

var ESTADOS = {
  confirmed: 'Confirmado',
  declined:  'No asiste'
};

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var hoja = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];

    hoja.appendRow([
      d.guestName || '',
      // Si algún día llega un grupo nuevo, se escribe tal cual en vez de
      // quedar vacío: mejor un valor raro que perder el dato.
      GRUPOS[d.grupo] || d.grupo || '',
      Number(d.adults) || 0,
      ESTADOS[d.confirmation] || d.confirmation || '',
      new Date()
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ result: 'ok' }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', message: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
