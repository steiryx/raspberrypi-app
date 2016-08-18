#Note that the camera preview only works when a monitor is connected to the Pi,
#so remote access (such as SSH and VNC) will not allow you to see the camera preview

from picamera import PiCamera
from time import sleep

camera = PiCamera()

#If your preview was upside-down, you can rotate it with the following code:
#You can rotate the image by 90, 180, or 270 degrees, or you can set it to 0 to reset.
#camera.rotation = 180

#You can alter the transparency of the camera preview by setting an alpha level:
#alpha can be any value between 0 and 255.
#camera.start_preview(alpha=200)
camera.start_preview()

sleep(10)
camera.stop_preview()
