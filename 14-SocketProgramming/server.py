import socket, sys
import math

keystr = "rainclab.net"

def string_xor(data, key):
	repeat = math.ceil(len(data) / len(key))
	repeatKey = key * repeat
	return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(data, repeatKey))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(1)

print("Socket listen start")

connector, addr = s.accept()

while 1:
	data = connector.recv(1024)
	if not data: break
	decryptText = string_xor(data , keystr)
	
	print("Recv Mesg : " , decryptText.decode("utf-8"))
	
	senddata = input("Message : ")
	encryptText = string_xor(senddata, keystr)
	connector.send(encryptText.encode("utf-8"))

s.close()
