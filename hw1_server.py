IP_ADDR = '127.0.0.1' # loopback interface address (localhost)
PORT = 8000 # port to listen on
BUF_SIZE = 100 # buffer size

from socket import socket, AF_INET, SOCK_STREAM

# 1. Create a TCP socket
# 2. Bind the socket to address and port
# 3. Start listening to port

def addNumbers(input, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*':
        result = num1 * num2

    return result

def checkType(value1, value2):
    confirm = False

    try:
        value1 = int(value1)
        value2 = int(value2)
        confirm = True
    except ValueError:
        confirm = False

    return confirm

def doOperations(operator, value1, value2):
    operators_int = ['+', '-', '/', '*']
    operators_str = ['+']

    if operator in operators_int:
        if checkType(value1, value2):
            result = addNumbers(operator, value1, value2)
        else:
            if operator in operators_str:
                result = value1 + value2
            else:
                result = 'Cannot do this operation on strings.'

    return result


with socket(AF_INET, SOCK_STREAM) as s:
    s.bind((IP_ADDR, PORT))
    s.listen()
    
    # 4. Accept a new connection from a client
    # 5. Receive data from client
    # 6. Process the data
    # 7. Send the data to client
    # 8. Close the connection
    
    print('Waiting for a new connection')
    while True:
        conn, add = s.accept()
        print(f"Accepted con req from ({add})")
        while True:
            data = conn.recv(BUF_SIZE)
            if data:
                data = data.decode()

                content = data.split(" ")
                operator = content[0]
                num1 = content[1]
                num2 = content[2]
                result = doOperations(operator, num1, num2)

                print(f"Result at {add}: {result}")
                conn.send(str(result).encode())
            else:
                break
        print(f"Closing the current port {add}.")
        conn.close()
