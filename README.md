# 📱 SystemUpdate – Educational Android Background Client

> ⚠️ **DISCLAIMER:** This project is for **educational and testing purposes only**. It’s meant to demonstrate how Android services and socket communication work. It’s not advanced malware, and **you must not use it for unethical or illegal purposes**.

---

## 🎬 Demo (Android 15 Silent Install)

![1.mp4](./1.mp4)

> 🔍 This short video shows the APK being installed on an **Android 15 device** with **no popup, warnings, or security restrictions**, even with the latest patch (August 3, 2025). It installs like a normal app, blending in as a "System Update".

---

## 🧪 VirusTotal Scan Results

- **1.png** & **2.png** show the VirusTotal scan results.
- Only **2 engines ( Google and IKARUS anti.virus )** detect it as a generic "agent".
- **Google Play Protect did NOT block** the install or execution.

![1.png](./1.jpeg)
![2.png](./2.jpeg)

> ⚠️ These low detections are **not due to stealth**, but because it’s unknown and simple.

---

## 🔧 What It Does

SystemUpdate is a foreground Android service disguised as a system update. It:
- Shows a persistent notification ("Updating system...")
- Connects to a hardcoded IP/port
- Uses AES encryption to send/receive shell commands
- Executes commands and sends back encrypted output

---

## 🛠 How to Use

1. Clone the repo
2. Edit IP, Port, and Key in `PayloadService.kt`
3. Build the APK
4. Install on a test device (Android 13–15+)
5. Run your TCP server and connect

---

## 📜 License – GNU GPL v3

This code is licensed under the **GNU General Public License v3**.  
If you share modified versions, you must also open-source them under the same license.

> See `LICENSE` for full terms.

---

## ❗ Final Words

This project is a **learning tool** for Android foreground services, socket communication, and simple encryption. It **does not bypass modern detection on purpose**, and its low detection is just due to obscurity.

### ✅ Use it to learn.  
### ❌ Don’t use it to harm.  
### 🤖 Modify and experiment responsibly.

> Be curious, not malicious. 🎓
