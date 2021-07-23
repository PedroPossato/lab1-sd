import socket

HOST = 'localhost' # maquina onde esta o par passivo
PORTA = 5000        # porta que o par passivo esta escutando

# cria socket
sock = socket.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
sock.connect((HOST, PORTA))


while True:
	# envia uma mensagem para o par conectado
	while True:
		send_msg = input('Digite aqui sua mensagem: [Para terminar, digite "fim"]\n')
		if len(send_msg):
			break
		else:
			print("Tente novamente!")
	sock.send(send_msg.encode('utf-8'))

	#espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
	msg = sock.recv(1024) # argumento indica a qtde maxima de bytes da mensagem
	if send_msg == 'fim':
		print("\nFim!")
		break

	else:
		# imprime a mensagem recebida
		print("\nMensagem recebida: {}\n".format(str(msg, encoding='utf-8')))

# encerra a conexao
sock.close() 