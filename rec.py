#!/usr/bin/python2

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#rec_ip="10.42.0.1"
m#port=9999
#now connecting ip and port
s.bind(("10.42.0.1",9999))
#buffer size
while 4>2 :
	print s.recvfrom(100)



