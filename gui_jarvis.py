import os
import sys
import time
import datetime
import threading
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>J.A.R.V.I.S. Core</title>
    <style>
        body { background-color: #030a16; color: #00f3ff; font-family: sans-serif; text-align: center; margin: 0; padding: 15px; }
        .arc-reactor { width: 120px; height: 120px; border: 4px solid #00f3ff; border-radius: 50%; margin: 20px auto; box-shadow: 0 0 20px #00f3ff, inset 0 0 20px #00f3ff; animation: pulse 2s infinite; }
        @keyframes pulse { 0% { transform: scale(1); opacity: 0.8; } 50% { transform: scale(1.05); opacity: 1; } 100% { transform: scale(1); opacity: 0.8; } }
        .title { font-size: 22px; font-weight: bold; letter-spacing: 2px; text-shadow: 0 0 10px #00f3ff; }
        .status { color: #00a8ff; font-size: 12px; margin-bottom: 15px; }
        .console { background: rgba(0, 20, 40, 0.9); border: 1px solid #00f3ff; border-radius: 10px; padding: 10px; height: 180px; overflow-y: auto; text-align: left; font-size: 14px; box-shadow: 0 0 10px rgba(0,243,255,0.2); }
        .input-box { margin-top: 15px; display: flex; gap: 5px; }
        input { flex: 1; padding: 12px; background: #001020; border: 1px solid #00f3ff; color: #00f3ff; border-radius: 5px; font-size: 15px; outline: none; }
        button { padding: 12px 18px; background: #00f3ff; color: #030a16; border: none; font-weight: bold; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="title">J.A.R.V.I.S.</div>
    <div class="status">SYSTEM: ONLINE | USER: STARK</div>
    <div class="arc-reactor"></div>
    <div class="console" id="console">🤖 [J.A.R.V.I.S.]: Arayüz aktif, efendim.</div>
    
    <div class="input-box">
        <input type="text" id="cmd" placeholder="Komut girin..." onkeypress="if(event.key==='Enter') sendCmd()">
        <button onclick="sendCmd()">GÖNDER</button>
    </div>

    <script>
        function sendCmd() {
            let input = document.getElementById("cmd");
            let consoleDiv = document.getElementById("console");
            if(!input.value) return;
            
            consoleDiv.innerHTML += "<br><b>[Siz]:</b> " + input.value;
            
            fetch('/api', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({command: input.value})
            })
            .then(res => res.json())
            .then(data => {
                consoleDiv.innerHTML += "<br>🤖 <b>[JARVIS]:</b> " + data.reply;
                consoleDiv.scrollTop = consoleDiv.scrollHeight;
            });
            
            input.value = "";
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api', methods=['POST'])
def api():
    cmd = request.json.get('command', '').lower()
    reply = "Emredersiniz, efendim."
    
    if "saat" in cmd:
        reply = f"Saat şu an {datetime.datetime.now().strftime('%H:%M')}, efendim."
    elif "durum" in cmd or "sistem" in cmd:
        reply = "Tüm çekirdek sistemler %100 kapasiteyle çalışıyor, efendim."
    elif "selam" in cmd or "merhaba" in cmd or "jarvis" in cmd:
        reply = "Sistemler çevrimiçi, efendim. Dinliyorum."

    os.system(f'termux-tts-speak "{reply}" &')
    return jsonify({'reply': reply})

def open_browser():
    time.sleep(1.5)
    os.system("termux-open-url http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Thread(target=open_browser).start()
    app.run(host='127.0.0.1', port=5000, debug=False)
