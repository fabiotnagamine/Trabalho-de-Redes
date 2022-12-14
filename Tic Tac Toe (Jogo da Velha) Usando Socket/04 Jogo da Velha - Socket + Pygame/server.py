import socket
import pickle
import time

s = socket.socket()
host = ""
port = 9999
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(matrix)

playerOne = 1
playerTwo = 2

playerConn = list()
playerAddr = list()       


def get_input(currentPlayer):
    if currentPlayer == playerOne:
        player = "Vez de Jogador 1"
        conn = playerConn[0]
    else:
        player = "Vez de Jogador 2"
        conn = playerConn[1]
    print(player)
    send_common_msg(player)
    try:
        conn.send("Input".encode())
        data = conn.recv(2048 * 10)
        conn.settimeout(20)
        dataDecoded = data.decode().split(",")
        x = int(dataDecoded[0])
        y = int(dataDecoded[1])
        matrix[x][y] = currentPlayer
        send_common_msg("Matrix")
        send_common_msg(str(matrix))
    except:
        conn.send("Error".encode())
        print("Error occured! Try again..")

def check_rows():
    # print("Checking rows")
    result = 0
    for i in range(3):
        if matrix[i][0] == matrix[i][1] and matrix[i][1] == matrix[i][2]:
            result = matrix[i][0]
            if result != 0:
                break
    return result

def check_columns():
    # print("Checking cols")
    result = 0
    for i in range(3):
        if matrix[0][i] == matrix[1][i] and matrix[1][i] == matrix[2][i]:
            result = matrix[0][i]
            if result != 0:
                break
    return result

def check_diagonals():
    # print("Checking diagonals")
    result = 0
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2]:
        result = matrix[0][0]
    elif matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
        result = matrix[0][2]
    return result

def check_winner():
    result = 0
    result = check_rows()
    if result == 0:
        result = check_columns()
    if result == 0:
        result = check_diagonals()
    return result

#Socket program
def start_server():
    #Binding to port 9999
    #Only two clients can connect 
    try:
        s.bind((host, port))
        print("Tic Tac Toe server started \nBinding to port", port)
        s.listen(2) 
        accept_players()
    except socket.error as e:
        print("Server binding error:", e)
    

#Accept player
#Send player number
def accept_players():
    try:
        for i in range(2):
            conn, addr = s.accept()
            msg = "<<< Voc?? ?? o jogador {} >>>".format(i+1)
            conn.send(msg.encode())

            playerConn.append(conn)
            playerAddr.append(addr)
            print("Jogador {} - [{}:{}]".format(i+1, addr[0], str(addr[1])))
    
        start_game()
        s.close()
    except socket.error as e:
        print("Erro na conex??o com o jogador", e)
    except KeyboardInterrupt:
            print("\nKeyboard Interrupt")
            exit()
    except Exception as e:
        print("ERRO: ", e)

def start_game():
    result = 0
    i = 0
    while result == 0 and i < 9 :
        if (i%2 == 0):
            get_input(playerOne)
        else:
            get_input(playerTwo)
        result = check_winner()
        i = i + 1
        # print("Current count", i ,result == 0 and i < 9, "Result = ", result)
    
    send_common_msg("Over")

    if result == 1:
        lastmsg = "Jogador 1 Ganhou!!"
    elif result == 2:
        lastmsg = "Jogador 2 Ganhou!!"
    else:
        lastmsg = "Empate!"

    send_common_msg(lastmsg)
    time.sleep(10)
    for conn in playerConn:
        conn.close()
    

def send_common_msg(text):
    playerConn[0].send(text.encode())
    playerConn[1].send(text.encode())
    time.sleep(1)

start_server()
