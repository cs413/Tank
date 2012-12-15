import tank as t #Import the tank commands
t.overon() #Enable overide to prevent movement

del over = True

def main()
	n = raw_input("Enter Command:")
	while n.strip() != 'exit':
		command(n)
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
	