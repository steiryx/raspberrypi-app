#open a terminal window
#Type the following command and press Enter to play the video:
#omxplayer video.h264
#It may actually play slightly faster than it was recorded,
#due to omxplayer's fast frame rate.

from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
