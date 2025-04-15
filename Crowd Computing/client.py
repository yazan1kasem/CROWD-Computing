import socket

HOST = '127.0.0.1'
PORT = 65432

# Faktorisierungsfunktion (einfach, reicht für Demo)
def factorize(n):
    n = int(n)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return f"{i} * {n // i}"
    return f"{n} * 1"

def main():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                number = data.decode()
                result = factorize(number)
                s.sendall(result.encode())
    except ConnectionRefusedError:
        print("Server nicht erreichbar.")
    except Exception as e:
        print(f"Fehler im Client: {e}")

if __name__ == '__main__':
    main()
