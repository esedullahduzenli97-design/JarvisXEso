import os
import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

class JarvisApp(App):
    def build(self):
        self.title = "J.A.R.V.I.S. Core"
        
        main_layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        title_label = Label(
            text="[b]J.A.R.V.I.S. CORE[/b]\n[size=12]SYSTEM: ONLINE | USER: STARK[/size]",
            markup=True,
            size_hint=(1, 0.15),
            color=(0, 0.95, 1, 1),
            font_size='20sp',
            halign='center'
        )
        main_layout.add_widget(title_label)

        self.console = Label(
            text="🤖 [J.A.R.V.I.S.]: Uygulama aktif, efendim. Emirlerinizi bekliyorum.\n",
            size_hint_y=None,
            color=(0, 0.85, 1, 1),
            font_size='14sp',
            halign='left',
            valign='top'
        )
        self.console.bind(texture_size=self.console.setter('size'))
        
        scroll = ScrollView(size_hint=(1, 0.65))
        scroll.add_widget(self.console)
        main_layout.add_widget(scroll)

        input_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        
        self.cmd_input = TextInput(
            hint_text="Komut yazın, efendim...",
            multiline=False,
            background_color=(0, 0.08, 0.16, 1),
            foreground_color=(0, 0.95, 1, 1),
            cursor_color=(0, 0.95, 1, 1),
            font_size='16sp'
        )
        self.cmd_input.bind(on_text_validate=self.send_command)
        
        send_btn = Button(
            text="GÖNDER",
            size_hint=(0.3, 1),
            background_color=(0, 0.95, 1, 1),
            color=(0, 0.05, 0.1, 1),
            bold=True
        )
        send_btn.bind(on_press=self.send_command)

        input_layout.add_widget(self.cmd_input)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)

        return main_layout

    def send_command(self, instance):
        text = self.cmd_input.text.strip()
        if not text:
            return

        self.console.text += f"\n[Siz]: {text}"
        cmd = text.lower()
        reply = "Emredersiniz, efendim."

        if any(w in cmd for w in ["saat", "kaç"]):
            reply = f"Saat şu an {datetime.datetime.now().strftime('%H:%M')}, efendim."
        elif any(w in cmd for w in ["durum", "sistem"]):
            reply = "Tüm çekirdek sistemler stabl ve %100 kapasiteyle çalışıyor, efendim."
        elif any(w in cmd for w in ["selam", "merhaba", "jarvis"]):
            reply = "Sistemler çevrimiçi, efendim. Dinliyorum."

        self.console.text += f"\n🤖 [JARVIS]: {reply}\n"
        self.cmd_input.text = ""

if __name__ == "__main__":
    JarvisApp().run()
