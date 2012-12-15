import piface.pfio as pfio # Import the piface emulators to allow running of the tank
pfio.init()

pfio.digital_write(5,1) # Both Tracks Disabled

# Overide Disabled
def overoff():
	pfio.digital_write(5,0)
	return True

# Overide Enable
def overon():
	pfio.digital_write(5,1)
	return True

# Forward
def forward():
	right(1)
	left(3)
	return True

# Reverse
def reverse():
	right(2)
	left(4)
	return True

# Stop
def stop():
	right(0)
	left(0)
	return True

# Turn Left
def tLeft():
	right(1)
	left(0)
	return True

# Turn Right
def tRight():
	right(0)
	left(3)
	return True

# Spin Left
def sLeft():
	right(2)
	left(3)
	return True

# Spin Right
def sRight():
	right(1)
	left(4)
	return True

# Method for Right Track
def right(val):
	if val == 1:
		pfio.digital_write(2,0)
		pfio.digital_write(1,1)
	elif val == 2:
		pfio.digital_write(1,0)
		pfio.digital_write(2,1)
	elif val == 0:
		pfio.digital_write(1,0)
		pfio.digital_write(2,0)
	return True

# Method for Left Track
def left(val):
	if val == 3:
		pfio.digital_write(4,0)
		pfio.digital_write(3,1)
	elif val == 4:
		pfio.digital_write(3,0)
		pfio.digital_write(4,1)
	elif val == 0:
		pfio.digital_write(3,0)
		pfio.digital_write(4,0)
	return True


