from picamera import PiCamera
from time import sleep

camera = PiCamera()

#maximum resolution is 2592 x 1944 for still photos
#and 1920 x 1080 for video recording
#need to set the frame rate to 15 to enable this maximum resolution:
#minimum resolution allowed is 64 x 64
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()

#add text to your image
#camera.start_preview()
#camera.annotate_text = "Hello world!"
#sleep(5)
#camera.capture('/home/pi/Desktop/text.jpg')
#camera.stop_preview()

#alter the brightness setting, which can be set from 0 to 100.
#The default is 50.
#camera.start_preview()
#for i in range(100):
#    camera.annotate_text = "Brightness: %s" % i
#    camera.brightness = i
#    sleep(0.1)
#camera.stop_preview()

#same for the contrast:
#camera.start_preview()
#for i in range(100):
#    camera.annotate_text = "Contrast: %s" % i
#    camera.contrast = i
#    sleep(0.1)
#camera.stop_preview()

#annotation text size
#Valid sizes are 6 to 160. The default is 32
#camera.annotate_text_size = 50

#annotation colours
#from picamera import PiCamera, Color
#camera.start_preview()
#camera.annotate_background = Color('blue')
#camera.annotate_foreground = Color('yellow')
#camera.annotate_text = " Hello world "
#sleep(5)
#camera.stop_preview()

#You can use camera.image_effect to apply a particular image effect.
#The options are: none, negative, solarize, sketch, denoise, emboss,
#oilpaint, hatch, gpen, pastel, watercolor, film, blur, saturation,
#colorswap, washedout, posterise, colorpoint, colorbalance, cartoon,
#deinterlace1, and deinterlace2. The default is none.
#camera.start_preview()
#camera.image_effect = 'colorswap'
#sleep(5)
#camera.capture('/home/pi/Desktop/colorswap.jpg')
#camera.stop_preview()

#Try looping over the various image effects in a preview
#camera.start_preview()
#for effect in camera.IMAGE_EFFECTS:
#    camera.image_effect = effect
#    camera.annotate_text = "Effect: %s" % effect
#    sleep(5)
#camera.stop_preview()

#You can use camera.awb_mode to set the auto white balance to a preset
#mode to apply a particular effect. The options are: off, auto, sunlight,
#cloudy, shade, tungsten, fluorescent, incandescent, flash, and horizon.
#The default is auto.
#loop over the available auto white balance modes with camera.AWB_MODES
#camera.start_preview()
#camera.awb_mode = 'sunlight'
#sleep(5)
#camera.capture('/home/pi/Desktop/sunlight.jpg')
#camera.stop_preview()

#You can use camera.exposure_mode to set the exposure to a preset mode to
#apply a particular effect. The options are: off, auto, night, nightpreview,
#backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake,
#and fireworks. The default is auto.
#loop over the available exposure modes with camera.EXPOSURE_MODES.
#camera.start_preview()
#camera.exposure_mode = 'beach'
#sleep(5)
#camera.capture('/home/pi/Desktop/beach.jpg')
#camera.stop_preview()
