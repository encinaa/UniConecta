"""como no me iba PyQt5, puse PyQt6. si no va. Cambios:
- sustituir PyQt6 por PyQt5
- añadir _ al exec del main: app.exec_
"""

from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5 import uic
from src.vista.Login import Login
from src.modelo.vo.LoginBBDD import LoginBD
from src.controlador.ControladorPrincipal import ControladorPrincipal


#wkejsdfh
if __name__ == "__main__":
    app = QApplication([])
    ventana = Login()
    ventana.show()
    modelo = LoginBD("bbdd")
    controlador = ControladorPrincipal(ventana, modelo)
    controlador.mostrarLogin()
    app.exec()
