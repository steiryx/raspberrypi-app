from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 90

camera.start_preview()
#It's important to sleep for at least 2 seconds before capturing,
#to give the sensor time to set its light levels.
sleep(5)
camera.capture('/home/pi/Documents/raspberrypi-app/image.jpg')
camera.stop_preview()

#adding a loop to take five pictures in a row:
camera.start_preview()
for i in range(5):
    sleep(5)
    #The variable i contains the current iteration number, from 0 to 4,
    #so the images will be saved as image0.jpg, image1.jpg and so on.
    camera.capture('/home/pi/Documents/raspberrypi-app/image%s.jpg' % i)
camera.stop_preview()
