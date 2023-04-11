# Atividade 01 - Protocolo HTTP
# Aluna: Larissa Teixeira da Silva

#importa o módulo socket
from socket import *
import sys

# Cria servidor TCP com protocolo IPv4
serverSocket = socket(AF_INET, SOCK_STREAM)

# 1. Preparar um soquete TCP para receber pedidos de conexão de um cliente (navegador)
HOSTNAME = 'localhost'
serverPort = 8081

# Vincula o socket ao endereço e PORTa do servidor
serverSocket.bind((HOSTNAME, serverPort))

# Aguarda conexão 
serverSocket.listen(1) 
print("Servidor está pronto, na porta: ", serverPort)

while True:

	# 2. Estabelecer conexão TCP atendendo a pedido recebido por este soquete;
	print ('Estabelecendo conexão...')
	connectionSocket, addr = serverSocket.accept()
	try:
		 # 3. Receber dessa conexão requisição HTTP de um arquivo localizado no sistema do servidor;
		message = connectionSocket.recv(1024)
		print ("Mensagem: ", message)
		filename = message.split()[1]

		# 4. Obter o arquivo requisitado de seu sistema de arquivos;
		print ("Arquivo: ", filename) 
		f = open(filename[1:])
		outputdata = f.read()

		#Envia uma linha de cabeçalho HTTP para o soquete
		connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode()) #envia uma linha de cabeçalho 200 OK
		
		#Envia o conteúdo do arquivo solicitado para o cliente
		print ("Comprimento:  ", len(outputdata))
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.close() 
		print ('Arquivo enviado com sucesso!')

	# 5. Se o arquivo requisitado não estiver disponível, retornar mensagem de erro;
	# 6. Utilizar Try/Except	
	except IOError:
		# 7. Criar uma mensagem de resposta HTTP incluindo o arquivo requisitado;
		# 8. Enviar resposta e arquivo pela conexão TCP ao navegador requisitante;
		connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
		connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
		
		# 9. Fechar a conexão TCP e aguardar por novo pedido de conexão.
		connectionSocket.close() 
		break
serverSocket.close() #Fecha o soquete do servidor
sys.exit()