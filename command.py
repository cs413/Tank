###################################################################
# CS413 - Tank Project - 2012/2013                                #
# GROUP 2 - Colin , Iain, Mathew, Gary                            #
# REF: http://www.tutorialspoint.com/python/python_networking.htm #
###################################################################

import tank as t #Import the tank commands
import socket #Import Sockets to allow remote control
from ftplib import ftp #Import ftp to allow uploading of ip address
t.overon() #Enable overide to prevent movement

over = True

def main():
	a = 'n'
	if a.strip().lower() == 'y':
		remoteConnection()
	else
		terminal()
	
def remoteConnection():
	s = socket.socket()
	host = socket.gethostname()
	port = 40000
	ftpIp(host)
	s.bind((host,port))
	s.listen(5)
	while True:
		c, addr = s.accept()
		while n.strip !='exit':
			command(n.strip())
			n = s.recv(1024)
		s.close()

def ftpIp(host):
	file = '192.168.2.1' #host New IP
	ftp.connect('stream.2x1.co.uk') # Connet to Host
	ftp.login('u67918920-CS413','password123') # Login to Host
	ftp.delete('connection.html') # Delete Old Connection File
	ftp.storlines('STOR connection.html', file) # Upload new Connection File
	ftp.quit()
	
def terminal():
	n = raw_input("Enter Command:")
	while n.strip() != 'exit':
		command(n.strip())
		n = raw_input("Enter Command:")
		
def command(c):
	if c=='w' or c=='8':
		t.forward()
		return 'Forward'
	elif c=='s' or c=='5':
		t.stop()
		return 'Stop'
	elif c=='x' or c=='2':
		t.reverse()
		return 'Reverse'
	elif c=='a' or c=='4':
		t.tLeft()
		return 'Turn Left'
	elif c=='d' or c=='6':
		t.tRight()
		return 'Turn Right'
	elif c=='q' or c=='7':
		t.sLeft()
		return 'Spin Left'
	elif c=='e' or c=='9':
		t.sRIght()
		return 'Spin Right'
	elif c='#':
		if(over)
			over=False
			t.overoff()
			return 'Overide Off'
		else
			over=True
			t.overon()
			return 'Overide On'		
	