from time import sleep
from picamera import PiCamera

def set_cam_param(camera):
    camera.iso = 100
    #wait for gain
    sleep(2)
    #fix values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
 
if __name__ == "__main__":
    camera = PiCamera(resolution = (1280,720), framerate = 30)
    #Set ISO
    set_cam_param(camera)
    #take pics
    for i in range(10):
        camera.capture_sequence(['image%02d.jpg' %i for j in range(1)])
        sleep(2)
        print(i)

