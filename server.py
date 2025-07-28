import socket

HOST = '127.0.0.1' # My local machine
PORT = 65432 # Port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()
print(f"Server listening on {HOST}:{PORT}")