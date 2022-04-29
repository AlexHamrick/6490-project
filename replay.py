import socket
from encryption import decrypt
import argparse

def main():
    parser = argparse.ArgumentParser(description='Send commands to TPLink device')
    parser.add_argument('-i', '--ip', help="ip address of TPLink device")
    parser.add_argument('-f', '--file', help="The file with the (binary) bytes to replay")
    parser.add_argument('-p', '--port', help="The port number for the TPLink device", type=int, default=9999)
    args = parser.parse_args()

    ip = args.ip
    file = args.file
    port = args.port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with open(file, "rb") as f:
        content = f.read()
        # print(content_json)

    try:
        s.connect((ip, port))
        s.send(content)

        # Receive data from the server and shut down
        received = s.recv(1024)
        received = decrypt(received[4:])
        print(f'Received response: {received}')
    finally:
        s.close()

if __name__ == "__main__":
    main()

