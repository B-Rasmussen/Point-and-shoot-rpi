from time import sleep
from picamera import PiCamera
import Adafruit_CharLCD as LCD
from subprocess import call

lcd = LCD.Adafruit_CharLCDPlate()
camera = PiCamera()
camera.resoultion = (1920,1080)

time = 0
x = 'menu'

#for saving multiple camera(c), and video(v)
c = 0
v = 0

def MenuReturnFunc():
	global x
  	x = 'menu'
  	lcd.clear()
  	lcd.message('Returning to\nMainmenu')


def CameraFunc():
  	global c
  	c = c + 1
  	sleep(2)
  	lcd.clear()
  	lcd.set_color(1,0,0)
  	lcd.message('Taking Photo!')
  	sleep(2)
  	camera.capture('/home/pi/Desktop/Point-And-Shoot-Cam/Image/Image{0:04d}.jpg'.format(c))
  	lcd.clear()
  	lcd.message('Photo taken')
  	lcd.set_color(0,0,1)
  
def VideoRecFunc():
  	global v
  	v = v + 1
  	lcd.clear()
  	lcd.message('Filming!')
  	lcd.set_color(0,0,1)
  	camera.start_recording('/home/pi/Desktop/Point-And-Shoot-Cam/Video/video_{0:04d}.h264'.format(v))
  	camera.wait_recording(time)
  	camera.stop_recording()
  	lcd.clear()
  	lcd.mesage('Done Filming!')
  
def VideoINCFunc():
  	global time
  	time = time + 5
  	lcd.clear()
  	sleep(1)
  	lcd.message('Total time {0}'.format(time))

def VideoDECFunc():
	global time
  	time = time - 5
  	lcd.clear()
  	if 0 <time:
  		pass
  	else:
    	time = 0
  	sleep(1)
  	lcd.message('Total time {0}'.format(time))

def ShutDownFunc():
	lcd.clear()
	lcd.message('Shutting Down')
	call("sudo shutdown -h now", shell = True)

#Main Menu Starting Text
lcd.message('Main Menu\n<-vid      pic->')
lcd.set_color(1,1,1)

While True:

	#Main Menu
	while x == "menu":
		lcd.set_color(1,1,1)
		sleep(1)
		#camera
		if lcd.is_pressed(LCD.RIGHT):
			lcd.clear()
			lcd.message('Selected:\nCamera')
			x = "camera"
		#video
		elif lcd.is_pressed(LCD.LEFT):
			lcd.clear()
			lcd.message('Selected:\nVideo')
			x = "video"
		#Shut down
		elif lcd.is_pressed(LCD.SELECT):
			lcd.clear()
			lcd.message('Selected:\nShut Down')
			x = "ShutDown"
		else:
			lcd.clear()
			lcd.message('Main menu\n<-vid      pic->'
			sleep(1)
			lcd.clear()
			lcd.message('Press SEL to\nSHUT DOWN')
	
	#Camera
	while x == "camera":
		sleep(1)
		if lcd.is_pressed(LCD.SELECT):
			MenuReturnFunc()
		elif lcd.is_pressed(LCD.RIGHT):
			CameraFunc()
		else:
			lcd.clear()
			lcd.message('Press SEL to RTN\n-> for photo')
	
	#Video
	while x == "video":
		sleep(1)
		if lcd.is_pressed(LCD.SELECT):
			MenuReturnFunc()
		elif lcd.is_pressed(LCD.UP):
			VideoINCFunc()
		elif lcd.is_pressed(LCD.DOWN):
			VideoDECFunc()
		elif lcd.is_pressed(LCD.RIGHT):
			VideoRecFunc()
		else:
			sleep(1)
			lcd.clear()
			lcd.message('press UP/DOWN to\nINC/DCR vid LGTH')
			sleep(2)
			lcd.clear()
			lcd.message('Press SEL to RTN\n-> to record')
	
	while x == "ShutDown":
		sleep(1)
		lcd.set_color(1,0,0)
		if lcd.is_pressed(LCD.LEFT):
			MenuReturnFunc()
		elif lcd.is_pressed(LCD.RIGHT):
			ShutDownFunc()
		else:
			sleep(2)
			lcd.clear()
			lcd.message('Confirm shutdown?\n<-No       Yes->')
