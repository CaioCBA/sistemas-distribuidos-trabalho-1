import socket

def send_data(socketC, respostas):
    for resposta in respostas:
        socketC.sendto(resposta.encode(), ("localhost", 8000))
        resultado, aux = socketC.recvfrom(4096)
        print(resultado.decode())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

num_respostas = int(input("Quantas respostas você deseja enviar? "))
respostas = []

for i in range(num_respostas):
    questao = input(f"Digite o número da questão {i + 1}: ")
    num_opcoes = input(f"Digite o número de alternativas da questão {i + 1}: ")
    resposta = input(f"Digite as respostas da questão {i + 1} (V ou F): ")
    respostas.append(f"{questao};{num_opcoes};{resposta}")
    
send_data(client_socket, respostas)
    
client_socket.close()
