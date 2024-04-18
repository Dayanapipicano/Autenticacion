import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_correo():
    # Configurar los detalles del servidor SMTP de Mailtrap
    servidor_smtp = 'smtp.mailtrap.io'
    puerto = 2525
    usuario = 'tu_usuario_de_mailtrap'
    contraseña = 'tu_contraseña_de_mailtrap'

    # Construir el mensaje de correo electrónico
    mensaje = MIMEMultipart()
    mensaje['From'] = 'from@example.com'
    mensaje['To'] = 'to@example.com'
    mensaje['Subject'] = 'Prueba de conexión con Mailtrap'
    cuerpo = 'Este es un correo de prueba enviado desde Python utilizando Mailtrap.'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Iniciar conexión con el servidor SMTP de Mailtrap
    with smtplib.SMTP(servidor_smtp, puerto) as servidor:
        servidor.starttls()
        servidor.login(usuario, contraseña)
        servidor.sendmail('from@example.com', 'to@example.com', mensaje.as_string())

    print("Correo electrónico enviado correctamente.")

# Llamar a la función para enviar el correo electrónico
enviar_correo()
