###################################################################
# CS413 - Tank Project - 2012/2013                                #
# GROUP 2 - Colin , Iain, Mathew, Gary                            #
# REF: http://www.tutorialspoint.com/python/python_networking.htm #
###################################################################

import socket

s = socket.socket()
host = socket.gethostname()
port = 40000
s.bind((host,port))

s.listen(5)
while True:
	c, addr = s.accept()
	while


