from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from assets import database

class LoginScreen(MDScreen):
    def try_login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if not username or not password:
            self.show_error_dialog("Por favor, preencha todos os campos")
            return
        
        datas = database.Database(username, "", password)

        if datas.verify_password() is None:
            self.show_error_dialog("Erro ao verificar senha")
            return
        
        if not datas.verify_password():
            self.show_error_dialog("Usuário ou senha incorretos")
            return

        # Simulação de login bem-sucedido
        self.manager.current = "home"
        self.ids.username.text = ""
        self.ids.password.text = ""

    def show_error_dialog(self, message):
        dialog = MDDialog(
            title="Erro",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
