import tkinter as tk
import os
import datetime

class JarvisTkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. Core")
        self.root.configure(bg='#030a16')
        self.root.geometry("400x600")

        # Başlık
        self.title_label = tk.Label(root, text="J.A.R.V.I.S. CORE\nSYSTEM: ONLINE", font=("Courier", 16, "bold"), fg="#00f3ff", bg="#030a16")
        self.title_label.pack(pady=15)

        # Konsol Ekranı
        self.console = tk.Text(root, bg="#001020", fg="#00f3ff", font=("Courier", 11), wrap=tk.WORD, height=18)
        self.console.pack(padx=15, pady=10, fill=tk.BOTH, expand=True)
        self.console.insert(tk.END, "🤖 [J.A.R.V.I.S.]: Grafiksel arayüz aktif, efendim.\n")

        # Giriş Kutusu
        self.entry = tk.Entry(root, bg="#001020", fg="#00f3ff", font=("Courier", 12), insertbackground="#00f3ff")
        self.entry.pack(padx=15, pady=5, fill=tk.X)
        self.entry.bind("<Return>", self.send_command)

        # Gönder Butonu
        self.btn = tk.Button(root, text="GÖNDER", font=("Courier", 11, "bold"), bg="#00f3ff", fg="#030a16", command=self.send_command)
        self.btn.pack(pady=10)

        os.system('termux-tts-speak "Grafiksel arayüz aktif, efendim." &')

    def send_command(self, event=None):
        cmd = self.entry.get().strip()
        if not cmd:
            return

        self.console.insert(tk.END, f"\n[Siz]: {cmd}\n")
        cmd_lower = cmd.lower()
        reply = "Emredersiniz, efendim."

        if any(w in cmd_lower for w in ["saat", "kaç"]):
            reply = f"Saat şu an {datetime.datetime.now().strftime('%H:%M')}, efendim."
        elif any(w in cmd_lower for w in ["durum", "sistem"]):
            reply = "Tüm çekirdek sistemler %100 kapasiteyle çalışıyor, efendim."
        elif any(w in cmd_lower for w in ["selam", "merhaba", "jarvis"]):
            reply = "Sistemler çevrimiçi, efendim. Dinliyorum."

        self.console.insert(tk.END, f"🤖 [JARVIS]: {reply}\n")
        self.console.see(tk.END)
        os.system(f'termux-tts-speak "{reply}" &')
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisTkApp(root)
    root.mainloop()
