from src.modelo.vo.LoginVO import LoginVO
from src.modelo.vo.LoginBBDD import LoginBD
from src.controlador.utils import Utils
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ControladorPrincipal:
    def __init__(self, vista):
        self._vista = vista
        self._modelo = LoginBD("bbdd")  # Instancia del modelo
        self._vista.botonaceptar.clicked.connect(self.on_login_clicked)

    def on_login_clicked(self):
        correo = self._vista.lineEdit.text()
        contraseña = self._vista.lineEdit_2.text()
        self.login(correo, contraseña)

    def on_register_clicked(self):
        correo = self._vista.lineEdit.text()
        contraseña = self._vista.lineEdit_2.text()
        self.registro(correo, contraseña)

    def on_recupPsw_clicked(self):
        correo = self._vista.lineEdit.text()
        ##TODO el metodo para recuperar contraseña
        self.registro(correo)


    def login(self, correo, contraseña):
        if len(correo) > 3:
            loginVO = LoginVO(correo, contraseña)
            if self._modelo.validar_email(loginVO.correo):
                if self._modelo.encontrar_contraseña(loginVO.correo, loginVO.contraseña):
                    print("Login exitoso")
                else:
                    print("Contraseña incorrecta")
            else:
                print("Usuario no registrado")
        else:
            print("Correo demasiado corto")

    def mostrarLogin(self):
        self._vista.show()

    def ocultarLogin(self):
        self._vista.hide()

    def eliminarLogin(self):
        self._vista.close()
    ##Funcion para generar codigo de longitud 6
    def generar_codigoVerf(longitud=6):
        codigo = ''
        for _ in range(longitud):
            digito = random.randint(0, 9)
            codigo += str(digito)
            return codigo

    def registro(self, correo, contraseña):
       if self._modelo.registrar_usuario(correo, contraseña) :
           codigo = self.generar_codigoVerf
           self.enviar_correo_confirmacion(correo,codigo)
        

         

    ##hacemos función para mandar correo
    def enviar_correo_confirmacion(destinatario, codigo):
        remitente = "aplicacion@gmail.com" ##Correo de la app
        contraseña = "1234" ##la ctrñ del correo de la app  

        asunto = "Confirmación de cuenta"
        cuerpo = f"""
        ¡Hola!
        
        Gracias por registrarte. Tu código de confirmación es: {codigo}
        
        
        """

        
        mensaje = MIMEMultipart()
        mensaje['From'] = remitente
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
                servidor.starttls() 
                servidor.login(remitente, contraseña)
                servidor.send_message(mensaje)
                print("Correo enviado correctamente.")
        except Exception as e:
            print(f"Error al enviar correo: {e}")
