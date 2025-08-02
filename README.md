# 📱 SystemUpdate – Educational Android Background Client

> ⚠️ **DISCLAIMER:** This project is intended for **educational and ethical testing purposes only**. It showcases how Android services and socket communication work. It’s **not stealthy malware**, and must **never be used for harmful or illegal purposes**.

---

## 🎬 Demo – Silent Install on Android 15

![Demo GIF](./1.gif)

> 🔍 This demo shows the APK being installed on an **Android 15 device** without any popups, warnings, or security prompts — even with the latest security patch (August 3, 2025). It blends in under the name "System Update".

---

## 🧪 VirusTotal Scan Results

The scan shows **minimal detection** by antivirus engines:

- ✅ Only **Google** (Android:Agent-GEN) and **IKARUS** (Trojan.AndroidOS.Agent) flagged it.
- ✅ **Google Play Protect did not block** the installation or execution.

![Scan 1](./1.jpeg)
![Scan 2](./2.jpeg)

> 🧠 These low detections are due to its simplicity and unknown signature — **not because it's stealthy**.

---

## 🔧 What It Does

SystemUpdate is a foreground Android service that mimics a system updater while performing remote command execution:

- Displays a persistent "System Update" notification
- Connects to a hardcoded IP and port
- Encrypts/decrypts messages using AES
- Executes shell commands received from the server
- Sends back encrypted output

---

## 🛠 How to Use

1. Clone this repository
2. Edit `SERVER_IP`, `SERVER_PORT`, and `SECRET_KEY` in `PayloadService.kt`
3. Build the APK in Android Studio
4. Install it on a test device (Android 13–15+)
5. Start a compatible TCP server to send commands

---

## 📜 License – GNU General Public License v3

This project is licensed under the **GNU GPL v3**.

> If you modify and distribute this code, your version must also remain open-source under the same license.

See [`LICENSE`](./LICENSE) for full terms.

---

## ❗ Final Thoughts

This project is a **basic educational tool**, not a hacking suite. Its low detection is due to novelty, not evasion. If you're studying Android internals, encryption, or services — this is a fun sandbox.

---

### ✅ Use it to learn  
### ❌ Don’t use it to harm  
### 🔧 Modify, break, and explore responsibly  

> Be curious, not malicious. 🎓
