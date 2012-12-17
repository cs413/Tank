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
		
def command(c):
	global over
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
		t.sRight()
		return 'Spin Right'
	elif c='=':
		if(over)
			over=False
			t.overoff()
			return 'Overide Off'
		else
			over=True
			t.overon()
			return 'Overide On'

def terminal():
	c = raw_input("Enter Command:")
	while c != 'exit':
		command(c)
		c = raw_input("Enter Command:")
	