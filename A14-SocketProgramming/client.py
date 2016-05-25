import socket, sys
HOST = '127.0.0.1'
PORT = 8888
import math
key = "rainclab.net"

def string_xor(data, key):
        repeat = math.ceil(len(data) / len(key))
        repeatKey = key * repeat
        return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(data, repeatKey))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while 1:
	data = input("message : ")
	encryptText = string_xor(data, key)
	s.send(encryptText.encode("utf-8"))
	data = s.recv(1024)
	if not data: break
	
	decryptText = string_xor( data, key)
	print("recv mesg:", decryptText.decode("utf-8"))

s.close()
