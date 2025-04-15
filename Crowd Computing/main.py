import socket
import threading
import queue
import random
import time
import subprocess
import sys

# Aufgabenliste (große Zahlen zum Faktorisieren)
task_queue = queue.Queue()
results = []

# Beispielhafte große Zahlen (semi-prime)
for _ in range(10):
    p = random.randint(100000, 200000)
    q = random.randint(100000, 200000)
    task_queue.put(p * q)

HOST = '127.0.0.1'
PORT = 65432


# Thread für jeden Client
def handle_client(conn, addr):
    print(f"[VERBUNDEN] {addr} verbunden.")
    while not task_queue.empty():
        try:
            number = task_queue.get_nowait()
        except queue.Empty:
            break
        try:
            conn.sendall(str(number).encode())
            data = conn.recv(1024).decode()
            results.append((number, data))
            print(f"[ERGEBNIS] {addr}: {number} => {data}")
        except:
            task_queue.put(number)  # Wenn der Client ausfällt, Aufgabe zurücklegen
            break
    conn.close()
    print(f"[GETRENNT] {addr} getrennt.")

# Server starten
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[SERVER] Läuft auf {HOST}:{PORT}")

        while not task_queue.empty():
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

# Simuliere Clients lokal als Prozesse
def start_clients(n):
    for _ in range(n):
        subprocess.Popen([sys.executable, 'client.py'])

if __name__ == '__main__':
    threading.Thread(target=start_server).start()
    time.sleep(1)  # kurze Pause, bis der Server bereit ist
    start_clients(5)  # Simuliere 5 Clients
