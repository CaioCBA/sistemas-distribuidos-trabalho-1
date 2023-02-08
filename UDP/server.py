import socket
import threading

def handler_client(data, address, socketC):
    print(f"Cliente conectado no endereço: {address}")
    resultado = calc_results(data.decode())
    socketC.sendto(resultado.encode(), address)

def calc_results(data):
    questao, num_opcoes, respostas = data.split(";")
    print(data)
    questao = int(questao)
    num_opcoes = int(num_opcoes)
    certa_resposta = "V" * num_opcoes
    num_corretos = sum([1 for a, b in zip(respostas, certa_resposta) if a == b])
    num_incorretos = num_opcoes - num_corretos
    return f"Questão {questao};Número de acertos: {num_corretos}; Número de erros: {num_incorretos}"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 8000))
    print("Servidor pronto para receber conexões")
    while True:
        data, address = server_socket.recvfrom(4096)
        client_thread = threading.Thread(target=handler_client, args=(data, address, server_socket))
        client_thread.start()

start_server()
