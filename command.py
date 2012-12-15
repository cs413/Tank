import tank as t #Import the tank commands
t.overon() #Enable overide to prevent movement

del over = True

n = raw_input("Enter Command:")
while n.strip() != 'exit':
    n = raw_input("Enter Command:")


def command(c):
	if c=='w':
		t.forward()
		return 'Forward'
	elif c=='s':
		t.stop()
		return 'Stop'
	elif c=='x'
		t.reverse()
		return 'Reverse'
	elif c=='a'
		t.tLeft()
		return 'Turn Left'
	elif c=='d'
		t.tRight()
		return 'Turn Right'
	elif c=='q'
		t.sLeft()
		return 'Spin Left'
	elif c=='e'
		t.sRIght()
		return 'Spin Right'
	elif c='#'
		if(over)
			over=False
			t.overoff()
			return 'Overide Off'
		else
			over=True
			t.overon()
			return 'Overide On'		
	