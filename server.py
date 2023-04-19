import socket
import threading
import time

clients = []
answers = [None, None]

def handleClient(sock, addr, player):
    print(f'starting new thread for {addr} for player {player}')
    while True:
        data = sock.recv(1024)
        if not data:
            break
        print(f'data from {addr}: {data}')
        answers[player] = data

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 6060))
sock.listen()

playerNumber = 0
while len(clients) < 2:
    [client, addr] = sock.accept()
    clients.append(client)
    print(f'client connected {addr}')
    threading.Thread(target=handleClient, args=(client,addr,playerNumber,)).start()
    playerNumber += 1

print('phase 2 started')
while True:
    if answers[0] is None or answers[1] is None:
        time.sleep(0.1)
        continue
    print(f'answers: {answers[0]} / {answers[1]}')
    def jokenpo(answers):
        if answers[0] == answers[1]:
            return "Empate!"
        elif answers[0] == b'pedra' and answers[1] == b'tesoura':
            return "Player 1 Ganhou!"
        elif answers[0] == b'papel' and answers[1] == b'pedra':
            return "Player 1 Ganhou!"
        elif answers[0] == b'tesoura' and answers[1] == b'papel':
            return "Player 1 Ganhou!"
        else:
            return "Player 2 Ganhou!"
    winner = jokenpo(answers)

    
    for client in clients:
        client.send(bytes(f'Resultado: {winner}', 'ascii'))
    answers = [None, None]