import socket
import time

esp_ip = '192.168.38.27'
esp_port = 80

def send_to_esp(message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = 20 if 'janelas' in message or 'porta' in message else 5
        s.settimeout(timeout)
        
        s.connect((esp_ip, esp_port))
        
        # Send HTTP request
        request = f'GET /{message} HTTP/1.1\r\nHost: {esp_ip}\r\nConnection: close\r\n\r\n'
        s.sendall(request.encode())
        
        # Receive complete response
        response = b''
        while True:
            try:
                chunk = s.recv(1024)
                if not chunk:
                    break
                response += chunk
            except socket.timeout:
                print("Warning: Partial response received")
                break
        
        decoded_resp = response.decode()
        print('Full response:', decoded_resp)
        
        return '200 OK' in decoded_resp
        
    except socket.error as e:
        print(f"Connection error: {e}")
        return False
    finally:
        s.close()

def ligar_out():
    send_to_esp('ligar_out')

def desligar_out():
    send_to_esp('desligar_out')

def abrir_porta():
    return True if send_to_esp('abrir_porta') else False

def fechar_porta():
    return True if send_to_esp('fechar_porta') else False
