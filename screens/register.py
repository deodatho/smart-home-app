from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from assets import database

class RegisterScreen(MDScreen):
    def try_register(self):
        username = self.ids.new_username.text
        email = self.ids.new_email.text
        password = self.ids.new_password.text
        confirm = self.ids.confirm_password.text

        datas = database.Database(username, email, password)

        if not all([username, email, password, confirm]):
            self.show_error_dialog("Por favor, preencha todos os campos")
            return

        if password != confirm:
            self.show_error_dialog("As senhas não coincidem")
            return
        
        try:
            if datas.insert_user():
                self.show_success_dialog("Cadastro realizado com sucesso!")
                print(datas.get_email_by_user)
                self.manager.current = "login"
                self.clear_fields()
            else:
                self.show_error_dialog("Erro ao cadastrar usuário: Email já existe")
            
        except Exception as e:
            self.show_error_dialog(f"Erro ao cadastrar usuário: {e}")
            return

    def clear_fields(self):
        self.ids.new_username.text = ""
        self.ids.new_email.text = ""
        self.ids.new_password.text = ""
        self.ids.confirm_password.text = ""

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

    def show_success_dialog(self, message):
        dialog = MDDialog(
            title="Sucesso",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
