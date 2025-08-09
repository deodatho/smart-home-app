from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from assets import send as sending_datas

class HomeScreen(MDScreen):
    def logout(self):
        self.manager.current = "login"

    def show_settings(self):
        dialog = MDDialog(
            title="Configurações",
            text="Configurações do aplicativo",
            buttons=[
                MDRaisedButton(
                    text="Fechar",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def toggle_lamps_manual(self, active):
        if active:
            sending_datas.ligar_out()
            status = "LIGADAS"
        else:
            sending_datas.desligar_out()
            status = "DESLIGADAS"

        self.ids.lamp_status.text = f"Status: Manual - Lâmpadas {status}"
        print(f"Lâmpadas do quintal {status.lower()} manualmente")

    def toggle_gate(self, active):
        if active:
            status = "Aberto"
            sending_datas.abrir_porta()
        else:
            status = "Fechado"
            sending_datas.fechar_porta()
        
        print(f"Portão {status}")
        self.ids.gate_status.text = f"Status: Portão {status}"

    def show_window_control_dialog(self):
        dialog = MDDialog(
            title="Controle Manual de Janelas",
            text="Deseja abrir ou fechar as janelas manualmente?",
            buttons=[
                MDRaisedButton(
                    text="Abrir",
                    on_release=lambda x: self.control_windows(True, dialog)
                ),
                MDRaisedButton(
                    text="Fechar",
                    on_release=lambda x: self.control_windows(False, dialog)
                ),
                MDRaisedButton(
                    text="Cancelar",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def control_windows(self, open, dialog):
        if open:
            action = "abertas"
            sending_datas.abrir_janelas()
        else:
            action = "fechadas"
        print(f"Janelas {action} manualmente")
        dialog.dismiss()
