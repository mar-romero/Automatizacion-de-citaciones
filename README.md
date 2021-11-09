# Automatizacion-de-citaciones

Bot creado para automatizar las citaciones de ocasa.

Se tiene que actualzdar los ID de WhatsApp(HTML) ya que se cambian constantemente y el chrome drivers tambien ya que tiene que ir de acuerdo con su version de chrome. 

Funcionamiento:

Se carga un archivo cvs por unica vez con los transportistas a citar y su disponibilidad y crea una base de datos unica, luego va creando una base de datos dependiendo de los choferes citados, el dia, la planta, disponibilidad del chofer, horario y Mensaje, una vez creada dicha base, se prosigue a enviar la citacion por medio de Whatsapp, en la cual envia un mensaje personalizado y al responder el bot levanta su respuesta y contesta. Al contestar que no va a estar disponible para el dia de la citación este indica en la base de datos y cita algun transportista que no fue citado.

Al terminar crea una Archivo CVS para poder analizarlo y modificarlo.
