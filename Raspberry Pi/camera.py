from picamera import PiCamera
from time import sleep

pictures_dir_filepath = '/home/pi/Desktop/sia_pictures/'

camera = PiCamera()
counter = 0
#camera.exposure_mode = 'sports'
camera.shutter_speed = 0

while True:
    raw_input("Press any key to take a picture: ")
    print(camera.zoom)    
    camera.start_preview()
    camera.start_recording(pictures_dir_filepath+'hello1.mjpeg')
    sleep(10)
    camera.stop_recording()
    #camera.capture(pictures_dir_filepath + str(counter) + '.jpg')
    counter += 1
    camera.stop_preview()

