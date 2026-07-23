import os
import sys
import time
import datetime

class JarvisNativeVoice:
    def __init__(self):
        self.identity = "J.A.R.V.I.S."
        self.user_title = "efendim"
        self.is_active = True

    def speak(self, text):
        print(f"\n🤖 [{self.identity}]: {text}")
        try:
            # Telefonun kendi yerel TTS (Text-to-Speech) motorunu kullanır
            # gTTS veya internet bağımlılığı yoktur, hata vermez
            os.system(f'termux-tts-speak "{text}"')
        except Exception as e:
            print(f"⚠️ [Ses Hatası]: {e}")

    def process(self, cmd):
        cmd_lower = cmd.strip().lower()
        if not cmd_lower:
            return

        if any(w in cmd_lower for w in ["merhaba", "selam", "jarvis"]):
            self.speak(f"Sistemler çevrimiçi, {self.user_title}. Dinliyorum.")
        elif any(w in cmd_lower for w in ["saat", "kaç"]):
            now = datetime.datetime.now().strftime("%H:%M")
            self.speak(f"Saat şu an {now}, {self.user_title}.")
        elif any(w in cmd_lower for w in ["kapat", "çık", "sonlandır"]):
            self.speak(f"Sistem kapatılıyor. İyi günler, {self.user_title}.")
            self.is_active = False
        else:
            self.speak(f"Emredersiniz, {self.user_title}.")

    def run(self):
        os.system("clear")
        self.speak(f"Yerel ses modülü aktif. Hizmetinizdeyim, {self.user_title}.")
        
        while self.is_active:
            try:
                user_input = input(f"\n[Stark]: ")
                self.process(user_input)
            except (KeyboardInterrupt, EOFError):
                break

if __name__ == "__main__":
    jarvis = JarvisNativeVoice()
    jarvis.run()
