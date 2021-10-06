import pyvjoy
import time

MAX_VJOY = 32767
MIN_VJOY = -32767

j = pyvjoy.VJoyDevice(1)


def increase_throttle():
	n = j.data.wAxisZRot
	print(n)
	j.data.wAxisZRot = n+1
	j.update()

def decreare_throttle():
	n = j.data.wAxisZRot
	print(n)
	j.data.wAxisZRot = n-1
	j.update()

def throttle(speed = int(MAX_VJOY/2)): #speed range 0 - 32767
	j.data.wAxisZRot = speed
	j.update()

def steer(r):
	j.data.wAxisXRot =r
	j.update()




if __name__ == '__main__':

	


	
	#j.data.wAxisX = int(MAX_VJOY/2)
	##j.data.wAxisY = int(MAX_VJOY/2)
	j.data.wAxisZ = MAX_VJOY


	#j.data.wAxisXRot = int(MAX_VJOY/2)
	#j.data.wAxisYRot = int(MAX_VJOY/2)
	#j.data.wAxisZRot = 0
	j.update()


