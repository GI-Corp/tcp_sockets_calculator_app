DEST_IP_ADDR =  '127.0.0.1'
DEST_PORT = 8000
BUF_SIZE = 100

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect((DEST_IP_ADDR, DEST_PORT))    
while True:
    try:

        data  = input("Input command for calculation: ")

        s.send(data.encode())
        # print(f"Data sent to server: {data}")
        result = ""

        while len(result) < len(data):
            recv_data = s.recv(BUF_SIZE)
            result += recv_data.decode()
            print(f"Result: {result}")
            break

    except KeyboardInterrupt:
        print('User is quit')
        s.close()
        break
